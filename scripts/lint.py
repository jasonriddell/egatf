#!/usr/bin/env python3
"""EGATF repository consistency checks.

Applies the framework's own discipline to its artefacts:

1. Schemas are loadable and use standard JSON Schema keywords.
2. Every Diagnostic Knowledge Pattern validates against the pattern schema.
3. The semantic observation vocabulary validates against its schema.
4. Every observation kind referenced in a pattern's evidence_requirements
   exists in the vocabulary (strict).
5. Every evidence class used in patterns and vocabulary is one of the
   canonical values.
6. No document reintroduces the retired Wisdom stage into the EGATF chain.
7. Every directory listed in the README repository structure exists.
8. Exactly the three canonical gates are defined as gates.
9. Contradicting and missing evidence kinds in patterns exist in the vocabulary
   (strict), and time_relation refs resolve to evidence requirement ids.
10. Case records (schemas/examples/ and cases/) validate against the case-record
    schema, every edge references existing nodes, and edge types connect
    compatible node types.

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

# Node-type prefixes used in case-record IDs, and the (from, to) prefix pairs
# each edge type may connect.
EDGE_RULES = {
    "supports": {("EV", "H"), ("INF", "H"), ("KN", "H")},
    "contradicts": {("EV", "H"), ("INF", "H"), ("KN", "H")},
    "derived_from": {("INF", "EV"), ("EV", "RS"), ("EV", "EV"), ("H", "INF"), ("H", "KN")},
    "produced_by": {("EV", "PE")},
    "described_by": {("RS", "CC")},
    "guided_by": {("H", "R"), ("INF", "R"), ("EV", "R")},
    "validated_against": {("KN", "CC"), ("KN", "RS")},
    "alternative_to": {("H", "H")},
    "justifies": {("J", "H")},
    "decided_on": {("D", "J"), ("M", "H")},
    "executed_as": {("A", "D"), ("A", "M")},
    "measured": {("O", "A")},
    "tests": {("O", "H"), ("CH", "H")},
    "yields": {("L", "O")},
}

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
        if re.search(rf"^\s*{re.escape(bad)}", text, re.M):
            err(f"{path}: uses non-standard keyword {bad} (use {bad[1:]})")


def check_case_record(path, schema):
    doc = load_yaml(path)
    if not isinstance(doc, dict) or doc.get("kind") != "case_record":
        return
    name = path.relative_to(ROOT)
    try:
        jsonschema.validate(doc, schema)
    except jsonschema.ValidationError as e:
        err(f"{name}: schema validation failed: {e.message} at {list(e.absolute_path)}")
        return
    nodes = {}
    for section, prefix in (("reported_claims", "R"), ("collection_context", "CC"), ("raw_sources", "RS"),
                            ("preparation", "PE"), ("evidence", "EV"), ("information", "INF"),
                            ("knowledge", "KN"), ("hypotheses", "H"), ("challenges", "CH"),
                            ("judgments", "J"), ("mitigations", "M"), ("decisions", "D"),
                            ("actions", "A"), ("outcomes", "O"), ("learnings", "L")):
        for n in doc.get(section, []) or []:
            if n["id"] in nodes:
                err(f"{name}: duplicate id {n['id']}")
            nodes[n["id"]] = (prefix, n)
    for e in doc.get("edges", []) or []:
        for end in ("from", "to"):
            if e[end] not in nodes:
                err(f"{name}: edge {e['from']} -[{e['type']}]-> {e['to']}: unknown node {e[end]}")
        if e["from"] in nodes and e["to"] in nodes:
            pair = (nodes[e["from"]][0], nodes[e["to"]][0])
            if pair not in EDGE_RULES[e["type"]]:
                err(f"{name}: edge {e['from']} -[{e['type']}]-> {e['to']}: {pair[0]} to {pair[1]} is not allowed for '{e['type']}'")
            src = nodes[e["from"]][1]
            if e["type"] == "supports" and src.get("window_semantics") == "collection_time_snapshot" and not e.get("note"):
                warn(f"{name}: {e['from']} is a collection-time snapshot supporting {e['to']} without a note on time compatibility")
    contradicted = {e["to"] for e in doc.get("edges", []) if e["type"] == "contradicts"}
    for hid, (pfx, n) in nodes.items():
        if pfx == "H" and n["status"] == "strengthened":
            tested = any(e["type"] == "tests" and e["to"] == hid and nodes.get(e["from"], ("",))[0] == "CH" for e in doc["edges"])
            if not tested:
                err(f"{name}: {hid} is strengthened but no challenge (CH) tests it")
            alts = any(e["type"] == "alternative_to" and hid in (e["from"], e["to"]) for e in doc["edges"])
            if not alts:
                warn(f"{name}: {hid} is strengthened but no alternative hypothesis is recorded")
    for jid, (pfx, n) in nodes.items():
        if pfx == "J" and n.get("claim_level") in ("supported_cause", "established_cause"):
            ok = any(e["type"] == "justifies" and e["from"] == jid for e in doc["edges"])
            if not ok:
                err(f"{name}: {jid} claims a cause but justifies no hypothesis")


def main():
    dkp_schema_path = ROOT / "schemas" / "diagnostic-knowledge-pattern.schema.yaml"
    vocab_schema_path = ROOT / "schemas" / "semantic-observation.schema.yaml"
    case_schema_path = ROOT / "schemas" / "case-record.schema.yaml"
    vocab_path = ROOT / "vocabulary" / "semantic-observations.yaml"

    # 1. Schemas
    for p in (dkp_schema_path, vocab_schema_path, case_schema_path):
        if not p.exists():
            err(f"missing schema: {p}")
            return
        check_schema_keywords(p)
    dkp_schema = load_yaml(dkp_schema_path)
    vocab_schema = load_yaml(vocab_schema_path)
    case_schema = load_yaml(case_schema_path)
    for name, s in (("pattern", dkp_schema), ("vocabulary", vocab_schema), ("case-record", case_schema)):
        try:
            jsonschema.Draft202012Validator.check_schema(s)
        except jsonschema.SchemaError as e:
            err(f"{name} schema is not a valid JSON Schema: {e.message}")

    # 3. Vocabulary validates
    vocab = load_yaml(vocab_path)
    known_kinds = set()
    contradiction_kinds = set()
    missing_kinds = set()
    if vocab and vocab_schema:
        try:
            jsonschema.validate(vocab, vocab_schema)
        except jsonschema.ValidationError as e:
            err(f"{vocab_path}: schema validation failed: {e.message} at {list(e.absolute_path)}")
        known_kinds = set(vocab.get("observation_kinds", {}).keys())
        contradiction_kinds = set((vocab.get("contradiction_kinds") or {}).keys())
        missing_kinds = set((vocab.get("missing_evidence_kinds") or {}).keys())
        no_contract = [k for k, v in vocab.get("observation_kinds", {}).items() if "contract" not in v]
        if no_contract:
            warn(f"{len(no_contract)} of {len(known_kinds)} observation kinds have no operational contract "
                 f"(definition, baseline, threshold, coverage): add one when a case needs the kind")
        provisional = [k for k, v in vocab.get("observation_kinds", {}).items()
                       if (v.get("contract") or {}).get("status") == "provisional"]
        if provisional:
            warn(f"{len(provisional)} of {len(known_kinds)} observation contracts are provisional "
                 f"(illustrative thresholds, not validated against a case)")
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
        req_ids = {i.get("id") for g in ("required", "optional") for i in reqs.get(g, []) or []}
        for group in ("required", "optional"):
            for item in reqs.get(group, []) or []:
                tr = item.get("time_relation") or {}
                if isinstance(tr, dict):
                    if tr.get("relation") == "overlaps_or_precedes" and tr.get("ref") not in req_ids:
                        err(f"{pf.name}: {item.get('id', '?')}: time_relation ref {tr.get('ref')!r} is not an evidence requirement id")
                    if tr.get("ref") and tr.get("ref") not in req_ids:
                        err(f"{pf.name}: {item.get('id', '?')}: time_relation ref {tr.get('ref')!r} is not an evidence requirement id")
                kind = item.get("kind")
                if kind and known_kinds and kind not in known_kinds:
                    err(f"{pf.name}: evidence_requirements.{group}: kind '{kind}' not in vocabulary")
                for ec in item.get("evidence_classes", []) or []:
                    if ec not in CANONICAL_EVIDENCE_CLASSES:
                        err(f"{pf.name}: {item.get('id', '?')}: unknown evidence class '{ec}'")
        for group, allowed in (("contradicting_evidence", contradiction_kinds | known_kinds),
                               ("missing_evidence", missing_kinds | known_kinds)):
            for item in doc.get(group, []) or []:
                kind = item.get("kind")
                if kind and kind not in allowed:
                    err(f"{pf.name}: {group}: kind '{kind}' not in vocabulary")
        versions = (doc.get("applies_to") or {}).get("versions") or {}
        if doc.get("status") != "draft" and versions.get("min") is None and versions.get("max") is None \
                and not versions.get("known_affected"):
            err(f"{pf.name}: status '{doc.get('status')}' requires explicit version applicability")
        if doc.get("status") != "draft" and not doc.get("last_reviewed"):
            err(f"{pf.name}: status '{doc.get('status')}' requires last_reviewed")
        for tr in doc.get("time_relationships", []) or []:
            for role in ("subject", "object"):
                kind = tr.get(role)
                if kind and known_kinds and kind not in known_kinds:
                    err(f"{pf.name}: time_relationships: {role} '{kind}' not in vocabulary")

    # 10. Case records
    case_files = sorted((ROOT / "schemas" / "examples").glob("*.yaml")) + sorted((ROOT / "cases").glob("**/*.case.yaml"))
    for cf in case_files:
        check_case_record(cf, case_schema)

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
