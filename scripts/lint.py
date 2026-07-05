#!/usr/bin/env python3
"""EGATF repository consistency checks.

Applies the framework's own discipline to its artefacts:

1. Schemas are loadable and use standard JSON Schema keywords.
2. Every Diagnostic Knowledge Pattern validates against the pattern schema.
3. The semantic observation vocabulary validates against its schema.
4. Every observation kind referenced in a pattern's evidence_requirements
   exists in the vocabulary (strict). Kinds in contradicting_evidence and
   missing_evidence produce warnings only, since they are often free-form.
5. Every evidence class used in patterns and vocabulary is one of the
   canonical values.
6. No document reintroduces the retired Wisdom stage into the EGATF chain.
7. Every directory listed in the README repository structure exists.
8. Exactly the three canonical gates are defined as gates.

Exit code 0 on success, 1 on any error. Warnings do not fail the run.

Requires: pyyaml, jsonschema
"""

import re
import sys
from pathlib import Path

import yaml

try:
    import jsonschema
except ImportError:
    print("ERROR: jsonschema not installed. pip install jsonschema")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent

CANONICAL_EVIDENCE_CLASSES = {
    "structured_source_material",
    "extracted_evidence",
    "derived_evidence",
    "correlated_evidence",
    "collection_context",
    "knowledge_validation",
}

CANONICAL_GATES = {
    "Evidence Sufficiency Gate",
    "Challenge Confidence Gate",
    "Outcome Validation Gate",
}

BANNED_CHAIN_PATTERNS = [
    r"Challenge\s*(?:->|→)\s*Wisdom",
    r"Insight\s*(?:->|→)\s*Challenge\s*(?:->|→)\s*Wisdom",
]

errors = []
warnings = []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def load_yaml(path):
    try:
        return yaml.safe_load(path.read_text())
    except yaml.YAMLError as e:
        err(f"{path}: YAML parse error: {e}")
        return None


def check_schema_keywords(path):
    text = path.read_text()
    for bad in ("$title:", "$type:"):
        if re.search(rf"^\s*\{bad[1:]}", text, re.M) and bad in text:
            err(f"{path}: uses non-standard keyword {bad} (use {bad[1:]})")


def main():
    dkp_schema_path = ROOT / "schemas" / "diagnostic-knowledge-pattern.schema.yaml"
    vocab_schema_path = ROOT / "schemas" / "semantic-observation.schema.yaml"
    vocab_path = ROOT / "vocabulary" / "semantic-observations.yaml"

    # 1. Schemas
    for p in (dkp_schema_path, vocab_schema_path):
        if not p.exists():
            err(f"missing schema: {p}")
            return
        check_schema_keywords(p)
    dkp_schema = load_yaml(dkp_schema_path)
    vocab_schema = load_yaml(vocab_schema_path)

    # 3. Vocabulary validates
    vocab = load_yaml(vocab_path)
    known_kinds = set()
    if vocab and vocab_schema:
        try:
            jsonschema.validate(vocab, vocab_schema)
        except jsonschema.ValidationError as e:
            err(f"{vocab_path}: schema validation failed: {e.message} at {list(e.absolute_path)}")
        known_kinds = set(vocab.get("observation_kinds", {}).keys())
        # 5. vocabulary evidence classes
        for kind, spec in vocab.get("observation_kinds", {}).items():
            for ec in spec.get("evidence_classes", []):
                if ec not in CANONICAL_EVIDENCE_CLASSES:
                    err(f"{vocab_path}: {kind}: unknown evidence class '{ec}'")

    # 2, 4, 5. Patterns
    pattern_files = sorted((ROOT / "knowledge-patterns").glob("*.yaml"))
    if not pattern_files:
        warn("no diagnostic knowledge patterns found in knowledge-patterns/")
    for pf in pattern_files:
        doc = load_yaml(pf)
        if doc is None:
            continue
        if dkp_schema:
            try:
                jsonschema.validate(doc, dkp_schema)
            except jsonschema.ValidationError as e:
                err(f"{pf.name}: schema validation failed: {e.message} at {list(e.absolute_path)}")
        reqs = doc.get("evidence_requirements", {}) or {}
        for group in ("required", "optional"):
            for item in reqs.get(group, []) or []:
                kind = item.get("kind")
                if kind and known_kinds and kind not in known_kinds:
                    err(f"{pf.name}: evidence_requirements.{group}: kind '{kind}' not in vocabulary")
                for ec in item.get("evidence_classes", []) or []:
                    if ec not in CANONICAL_EVIDENCE_CLASSES:
                        err(f"{pf.name}: {item.get('id', '?')}: unknown evidence class '{ec}'")
        for group in ("contradicting_evidence", "missing_evidence"):
            for item in doc.get(group, []) or []:
                kind = item.get("kind")
                if kind and known_kinds and kind not in known_kinds:
                    warn(f"{pf.name}: {group}: kind '{kind}' not in vocabulary (free-form allowed)")
        for tr in doc.get("time_relationships", []) or []:
            for role in ("subject", "object"):
                kind = tr.get(role)
                if kind and known_kinds and kind not in known_kinds:
                    err(f"{pf.name}: time_relationships: {role} '{kind}' not in vocabulary")

    # 6. Wisdom drift (framework docs, cases, README, diagrams; research/ is exempt
    # because it legitimately quotes DIKW literature and records history)
    scan_dirs = ["framework", "cases", "diagrams"]
    scan_files = [ROOT / "README.md"]
    for d in scan_dirs:
        scan_files.extend(sorted((ROOT / d).glob("**/*")))
    for f in scan_files:
        if not f.is_file() or f.suffix not in (".md", ".mmd", ".yaml"):
            continue
        text = f.read_text(errors="replace")
        for pat in BANNED_CHAIN_PATTERNS:
            for m in re.finditer(pat, text):
                line = text[: m.start()].count("\n") + 1
                # allow explicit historical references in the changelog
                if f.name == "changelog.md":
                    continue
                err(f"{f.relative_to(ROOT)}:{line}: retired 'Wisdom' stage in chain: {m.group(0)!r}")

    # 7. README structure directories exist
    readme = (ROOT / "README.md").read_text()
    m = re.search(r"## Repository Structure\n(.*?)\n(?:---|## )", readme, re.S)
    if m:
        for dm in re.finditer(r"^- `([a-z0-9-]+)/`", m.group(1), re.M):
            d = ROOT / dm.group(1)
            if not d.is_dir():
                err(f"README.md: repository structure lists '{dm.group(1)}/' but it does not exist")
    else:
        warn("README.md: could not locate Repository Structure section")

    # 8. Gate inventory in framework docs
    gate_headings = set()
    for f in sorted((ROOT / "framework").glob("*.md")):
        for m in re.finditer(r"^###+\s+(?:Gate \d+:\s*)?(.+ Gate)\s*$", f.read_text(), re.M):
            gate_headings.add(m.group(1).strip())
    unknown_gates = gate_headings - CANONICAL_GATES
    if unknown_gates:
        err(f"non-canonical gate heading(s) found: {sorted(unknown_gates)}. EGATF defines exactly three gates.")
    missing_gates = CANONICAL_GATES - gate_headings
    if missing_gates:
        warn(f"canonical gate(s) not found as headings in framework/: {sorted(missing_gates)}")

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s) "
          f"across {len(pattern_files)} pattern(s) and {len(known_kinds)} vocabulary kind(s).")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
