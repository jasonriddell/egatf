# Support Bundle Manifest Improvements for Evidence-Grounded Analysis

## Summary

Improve the support bundle manifest so support bundles are self-describing evidence packages for humans, deterministic analysis tools, and AI-assisted troubleshooting workflows.

The current `manifest.json` provides useful collection metadata such as bundle UUID, path, scope UUID, requested start and end time, selected components, and selected metrics types. However, it does not yet provide enough context to reliably interpret all collected material, especially when different parts of the bundle represent different effective times.

This request proposes extending the support bundle manifest, or adding companion manifest files, to include richer collection context, versioning, timing semantics, environment identity, component descriptions, and an index of included files.

---

## Relationship to EGATF Three-Loop Model

This feature supports the EGATF Evidence Loop.

The Evidence Sufficiency Gate asks:

> Do we understand the evidence well enough to reason from it?

A richer support bundle manifest helps answer that question by making collection context, timing semantics, schema version, environment identity, component descriptions, and file indexes explicit.

---

## Problem

Support bundles are increasingly used by humans, automated parsers, and AI-assisted workflows to diagnose customer issues.

However, a support bundle is not simply a bag of files. It is a time-bounded evidence package created by a particular version of YBA, from a particular universe, using a particular support bundle collector, with different evidence sources captured using different timing semantics.

For example:

- Universe logs may represent the requested support bundle duration.
- Metrics may represent a specific metric export duration, resolution, and retention behavior.
- Tablet metadata may represent the state at support bundle creation time.
- Consensus metadata may represent the state at support bundle creation time.
- Tablet report may represent the state at support bundle creation time.
- Some YBA metadata may represent the current YBA state at collection time rather than the requested diagnostic window.

This can cause confusion during analysis.

Example risk:

```text
Support bundle created at:
T

Logs collected for:
T - 7 days to T - 5 days

Tablet metadata collected at:
T

Tablet report collected at:
T
```

Without explicit collection context, a human or AI-assisted analysis tool may incorrectly use tablet state collected at T to explain log events from T - 7 to T - 5.

That is a false correlation caused by missing timing semantics.

---

## Why This Matters

### 1. Safer AI-assisted analysis

As AI is used more often to analyse support bundles, the bundle should provide explicit context that prevents the model from guessing.

AI should not need to infer:

- What each directory means
- Which version created the bundle
- Which YBDB version the universe was running
- Which YBA version produced the bundle
- Whether a file represents the requested time range or collection time
- Why some metrics are present and others are missing
- Whether all expected master, tserver, controller, or node agent directories are present

Explicit collection context reduces hallucination risk and prevents unsupported correlations.

### 2. Better deterministic tooling

Automated parsers need to know which support bundle schema version they are reading.

As YBA moves toward a model where YBA is ideally always on the latest released version, while YBDB universes may run different versions, the support bundle collector can evolve more safely if format changes are versioned.

If support bundle schema and collector versions are explicit, tools can select the correct parser.

Example behavior:

```text
If supportBundleSchemaVersion is 1.x:
    use parser family v1

If supportBundleSchemaVersion is 2.x:
    use parser family v2

If supportBundleSchemaVersion is unknown:
    fail safely or run best-effort mode with warnings
```

This allows collection formats to improve over time without silently breaking downstream automated analysis.

### 3. Faster human diagnosis

Support engineers should be able to quickly understand:

- What was collected
- What is missing
- Which universe and YBA instance the bundle came from
- Which versions were involved
- What time period each component represents
- Which directories contain master, tserver, controller, YBA, and node agent evidence
- Which metrics were requested and why some may be absent

### 4. Better evidence chains

Support bundle analysis should preserve a clear evidence chain.

A richer manifest helps distinguish:

```text
Reported issue
    ↓
Collection context
    ↓
Raw source material
    ↓
Prepared evidence
    ↓
Information
    ↓
Insight
    ↓
Decision
```

This is important for both human RCA and AI-assisted workflows.

---

## Goals

Add enough collection context to the support bundle manifest so that humans, deterministic tools, and AI-assisted analysis can answer:

1. What created this bundle?
2. Which schema describes this bundle?
3. When was the bundle created?
4. What time window was requested?
5. What time window does each component actually represent?
6. Which universe did the bundle come from?
7. Which YBDB version was the universe running?
8. Which YBA instance and version created the bundle?
9. What deployment type and infrastructure does the universe use?
10. What components are included?
11. Which files and directories are present?
12. Which files or components are missing or partially collected?
13. What does each component mean?
14. What should AI and humans be careful about when interpreting each component?

---

## Non-Goals

This change should not attempt to diagnose the issue.

The manifest should not say:

```text
The root cause was compaction.
The failing node was tserver-2.
The customer impact was caused by master leader movement.
```

The manifest should describe collection context, not conclusions.

---

## Proposed Implementation Options

### Option A: Expand `manifest.json`

Add the new fields directly to the existing support bundle `manifest.json`.

Advantages:

- Single obvious place to look
- Existing tools already expect a manifest
- Easier for AI and humans to find context

Disadvantages:

- Manifest may become larger
- Operational metadata and AI-friendly context may become mixed

### Option B: Add companion context files

Keep the existing `manifest.json`, but add companion files:

```text
manifest.json
bundle_context.json
file_index.json
```

Advantages:

- Cleaner separation
- Easier to evolve AI-friendly descriptions independently
- File index can be generated and consumed separately

Disadvantages:

- More files
- Tools need to know which files are authoritative

### Recommendation

Use `manifest.json` for required collection facts and schema versioning.

Optionally add companion sections or files for larger descriptions and file indexes.

A simple first implementation could extend `manifest.json` and later split if needed.

---

## Proposed Manifest Structure

### 1. Bundle Provenance

Add metadata describing what created the bundle.

Example:

```json
{
  "bundleUUID": "1a233260-4402-4ea2-9442-9678694bd281",
  "supportBundleVersion": "2026.1.0",
  "supportBundleSchemaVersion": "1.0",
  "supportBundleCollectorVersion": "2026.1.0",
  "createdAt": "2025-05-13T09:58:45Z",
  "createdBy": "YBA",
  "collectorName": "yba-support-bundle"
}
```

Suggested fields:

- `supportBundleVersion`
- `supportBundleSchemaVersion`
- `supportBundleCollectorVersion`
- `createdAt`
- `createdBy`
- `collectorName`

Rationale:

- Enables version-aware parsing.
- Supports intentional format changes.
- Allows tools to fail safely on unsupported bundle formats.

---

### 2. Environment Identity

Add metadata describing the source universe and YBA instance.

Example:

```json
{
  "universe": {
    "uuid": "3167f47d-0596-4931-887b-85c678e8f693",
    "name": "yb-tms-rf3",
    "ybdbVersion": "2024.2.3.1",
    "replicationFactor": 3,
    "masterCount": 3,
    "tserverCount": 6,
    "deploymentType": "k8s",
    "infrastructureType": "cloud",
    "provider": "gcp"
  },
  "yba": {
    "instanceId": "yba-prod-01",
    "version": "2025.1.1.1",
    "nodeAgentEnabled": true
  }
}
```

Suggested fields:

- Universe UUID
- Universe name
- Universe YBDB version at time of collection
- Universe replication factor at time of collection
- Master count at time of collection
- TServer count at time of collection
- Deployment type: `vm` or `k8s`
- Infrastructure type: `cloud` or `on_prem`
- Provider
- YBA instance ID or name
- YBA version at time of collection
- Node Agent enabled state

Rationale:

- Prevents confusion between YBA version and YBDB version.
- Helps tools choose version-aware parsing logic.
- Helps AI and humans interpret topology and deployment-specific files.

---

### 3. Collection Windows and Timing Semantics

Add component-specific timing context.

Example:

```json
{
  "collectionWindows": {
    "requestedBundleWindow": {
      "start": "2025-05-12T09:58:42Z",
      "end": "2025-05-13T09:58:42Z"
    },
    "UniverseLogs": {
      "windowType": "requested_duration",
      "start": "2025-05-12T09:58:42Z",
      "end": "2025-05-13T09:58:42Z"
    },
    "ApplicationLogs": {
      "windowType": "requested_duration",
      "start": "2025-05-12T09:58:42Z",
      "end": "2025-05-13T09:58:42Z"
    },
    "Metrics": {
      "windowType": "metrics_duration",
      "start": "2025-05-12T09:58:42Z",
      "end": "2025-05-13T09:58:42Z",
      "resolution": "configured_in_yba",
      "retention": "configured_in_yba"
    },
    "TabletMeta": {
      "windowType": "collection_time_snapshot",
      "collectedAt": "2025-05-13T09:58:45Z"
    },
    "ConsensusMeta": {
      "windowType": "collection_time_snapshot",
      "collectedAt": "2025-05-13T09:58:45Z"
    },
    "TabletReport": {
      "windowType": "collection_time_snapshot",
      "collectedAt": "2025-05-13T09:58:45Z"
    },
    "YbaMetadata": {
      "windowType": "mixed",
      "note": "Some values describe current YBA state at collection time; some may relate to requested bundle window."
    }
  }
}
```

Recommended `windowType` values:

```text
requested_duration
metrics_duration
collection_time_snapshot
mixed
unknown
not_applicable
```

Rationale:

- Prevents false time-window correlations.
- Makes it explicit which files represent history and which represent collection-time state.
- Helps AI avoid using collection-time state to explain older log events.

---

### 4. Metric Collection Context

Add YBA metric collection settings.

Example:

```json
{
  "metrics": {
    "configuredCollectionLevel": "normal",
    "requestedMetricTypes": [
      "MASTER_EXPORT",
      "NODE_EXPORT",
      "PLATFORM",
      "PROMETHEUS",
      "TSERVER_EXPORT",
      "CQL_EXPORT",
      "YSQL_EXPORT"
    ],
    "duration": {
      "start": "2025-05-12T09:58:42Z",
      "end": "2025-05-13T09:58:42Z"
    },
    "knownLimitations": [
      "Metric availability depends on YBA configuration and Prometheus retention.",
      "Not all metric types may be present for all nodes."
    ]
  }
}
```

Suggested fields:

- Configured metric collection level
- Requested metric types
- Metric start and end time
- Metric resolution if known
- Metric retention if known
- Known limitations

Rationale:

- Explains why not all metrics are available.
- Prevents analysis from treating missing metrics as proof that a condition did not occur.
- Helps compare metric duration with log duration.

---

### 5. Component Descriptions

Add human- and AI-friendly descriptions of each component.

Example:

```json
{
  "componentDescriptions": {
    "UniverseLogs": {
      "description": "Logs from universe nodes, including master and tserver logs where available.",
      "aiGuidance": "Master leadership can change over time. Examine all master logs and identify the leader at relevant times before drawing conclusions about master actions."
    },
    "TServerLogs": {
      "description": "YB-TServer logs. TServers host tablets and serve read/write traffic.",
      "aiGuidance": "Relevant for tablet activity, RPC errors, transaction activity, compaction, local resource issues, and per-node failures."
    },
    "MasterLogs": {
      "description": "YB-Master logs. Masters manage cluster metadata and tablet assignments.",
      "aiGuidance": "A single master may not show all relevant history if leadership changed. Consider all masters."
    },
    "YbaMetadata": {
      "description": "YBA platform metadata about universes, tasks, providers, and configuration.",
      "aiGuidance": "Some metadata reflects collection-time platform state rather than the requested diagnostic window."
    },
    "TabletMeta": {
      "description": "Tablet metadata collected at bundle creation time.",
      "aiGuidance": "Do not assume this reflects tablet state during a historical log window."
    },
    "ConsensusMeta": {
      "description": "Consensus metadata collected at bundle creation time.",
      "aiGuidance": "Do not assume this reflects raft state during a historical log window."
    },
    "Metrics": {
      "description": "Prometheus metrics exported according to YBA configuration.",
      "aiGuidance": "Availability, resolution, and duration depend on configured collection level and retention."
    }
  }
}
```

Rationale:

- Makes support bundles more self-describing.
- Helps AI interpret files correctly.
- Helps newer engineers understand bundle contents.
- Reduces repeated tribal knowledge.

---

### 6. File Index

Add an index of included directories and files.

Example:

```json
{
  "fileIndex": {
    "masters": [
      {
        "nodeName": "yb-master-0",
        "path": "UniverseLogs/yb-master-0/",
        "files": [
          "yb-master.INFO",
          "yb-master.WARNING",
          "yb-master.ERROR"
        ]
      }
    ],
    "tservers": [
      {
        "nodeName": "yb-tserver-0",
        "path": "UniverseLogs/yb-tserver-0/",
        "files": [
          "yb-tserver.INFO",
          "yb-tserver.WARNING",
          "yb-tserver.ERROR"
        ]
      }
    ],
    "controllers": [],
    "nodeAgents": [],
    "yba": []
  }
}
```

Suggested sections:

- Masters
- TServers
- Controllers
- Node Agents
- YBA logs
- Metrics
- Core files
- GFlags
- K8s information
- Tablet metadata
- Consensus metadata
- Tablet reports

Rationale:

- Helps tools validate expected files.
- Helps humans quickly inspect bundle completeness.
- Helps AI understand what exists before analysis.
- Helps distinguish "not collected" from "collected but empty".

---

## Proposed Acceptance Criteria

### Schema and versioning

- Support bundle manifest includes `supportBundleSchemaVersion`.
- Support bundle manifest includes `supportBundleCollectorVersion` or equivalent.
- Support bundle manifest includes `createdAt`.

### Environment identity

- Manifest includes universe UUID and name.
- Manifest includes universe YBDB version at time of collection.
- Manifest includes YBA version at time of collection.
- Manifest includes deployment type, infrastructure type, and provider.
- Manifest includes RF, master count, and tserver count where available.
- Manifest includes Node Agent enabled state.

### Collection windows

- Manifest includes requested bundle start and end.
- Manifest includes per-component `windowType`.
- Logs are identified as requested-duration evidence where applicable.
- Metrics are identified with metric-specific duration and collection settings.
- Tablet metadata, consensus metadata, and tablet report are identified as collection-time snapshots where applicable.
- Mixed sources are identified as mixed with explanatory notes.

### Component descriptions

- Manifest or companion context file includes descriptions for major components.
- Descriptions include AI/human guidance for interpreting master logs, tserver logs, metrics, YBA metadata, tablet metadata, consensus metadata, and tablet reports.

### File index

- Manifest or companion file includes an index of major directories and files.
- Index includes master directories.
- Index includes tserver directories.
- Index includes controller directories where applicable.
- Index includes node agent directories where applicable.
- Index includes YBA directories where applicable.

### Backward compatibility

- Older bundles without the new fields remain parseable.
- New fields are optional initially if needed.
- Unknown schema versions cause tools to fail safely or run best-effort with warnings.

---

## Suggested Implementation Phases

### Phase 1: Provenance and environment identity

Add:

- `supportBundleSchemaVersion`
- `supportBundleCollectorVersion`
- `createdAt`
- universe UUID/name
- universe YBDB version
- YBA version
- deployment type
- infrastructure type
- provider
- RF
- master/tserver counts
- Node Agent enabled state

### Phase 2: Collection windows

Add:

- requested bundle window
- per-component window type
- metric duration and collection settings
- collection-time snapshot markers for tablet metadata, consensus metadata, and tablet report

### Phase 3: File index

Add generated file index for major component directories.

### Phase 4: Component descriptions

Add human- and AI-friendly component descriptions.

This could be embedded in the bundle or referenced by support bundle schema version.

### Phase 5: JSON Schema and validation

Add JSON Schema validation for the manifest format.

---

## Example Top-Level Shape

```json
{
  "bundleUUID": "1a233260-4402-4ea2-9442-9678694bd281",
  "supportBundleVersion": "2026.1.0",
  "supportBundleSchemaVersion": "1.0",
  "supportBundleCollectorVersion": "2026.1.0",
  "createdAt": "2025-05-13T09:58:45Z",
  "scopeUUID": "3167f47d-0596-4931-887b-85c678e8f693",
  "requestedBundleWindow": {
    "start": "2025-05-12T09:58:42Z",
    "end": "2025-05-13T09:58:42Z"
  },
  "universe": {
    "uuid": "3167f47d-0596-4931-887b-85c678e8f693",
    "name": "yb-tms-rf3",
    "ybdbVersion": "2024.2.3.1",
    "replicationFactor": 3,
    "masterCount": 3,
    "tserverCount": 6,
    "deploymentType": "k8s",
    "infrastructureType": "cloud",
    "provider": "gcp"
  },
  "yba": {
    "instanceId": "yba-prod-01",
    "version": "2025.1.1.1",
    "nodeAgentEnabled": true
  },
  "collectionWindows": {
    "UniverseLogs": {
      "windowType": "requested_duration",
      "start": "2025-05-12T09:58:42Z",
      "end": "2025-05-13T09:58:42Z"
    },
    "Metrics": {
      "windowType": "metrics_duration",
      "start": "2025-05-12T09:58:42Z",
      "end": "2025-05-13T09:58:42Z"
    },
    "TabletMeta": {
      "windowType": "collection_time_snapshot",
      "collectedAt": "2025-05-13T09:58:45Z"
    },
    "ConsensusMeta": {
      "windowType": "collection_time_snapshot",
      "collectedAt": "2025-05-13T09:58:45Z"
    },
    "TabletReport": {
      "windowType": "collection_time_snapshot",
      "collectedAt": "2025-05-13T09:58:45Z"
    }
  },
  "bundleDetails": {
    "components": [
      "UniverseLogs",
      "OutputFiles",
      "ErrorFiles",
      "CoreFiles",
      "GFlags",
      "Instance",
      "ConsensusMeta",
      "TabletMeta",
      "YbcLogs",
      "K8sInfo",
      "NodeAgent",
      "YbaMetadata",
      "ApplicationLogs"
    ],
    "prometheusMetricsTypes": [
      "MASTER_EXPORT",
      "NODE_EXPORT",
      "PLATFORM",
      "PROMETHEUS",
      "TSERVER_EXPORT",
      "CQL_EXPORT",
      "YSQL_EXPORT"
    ]
  },
  "componentDescriptions": {},
  "fileIndex": {}
}
```

---

## Expected Benefits

- Better human understanding of support bundle contents.
- Safer AI-assisted analysis.
- Reduced time-window confusion.
- Reduced version confusion.
- Better deterministic parser selection.
- Easier support bundle format evolution.
- Easier validation of missing or partial data.
- Better evidence traceability for support, engineering escalation, and RCA.

---

## Risks and Considerations

### Manifest size

Adding file indexes and descriptions may increase manifest size.

Mitigation:

- Keep core facts in `manifest.json`.
- Optionally split larger sections into companion files.

### Sensitive data

Some environment fields may be sensitive.

Mitigation:

- Review fields for redaction requirements.
- Avoid adding secrets or credentials.
- Consider hashing or omitting sensitive values.

### Backward compatibility

Older support bundles will not include new fields.

Mitigation:

- Treat new fields as optional initially.
- Update parsers to handle missing fields.
- Use schema version to identify capabilities.

### Accuracy of context

Incorrect collection context could be worse than missing context.

Mitigation:

- Generate fields from authoritative sources.
- Add schema validation.
- Include collection errors and partial failures.

---

## Suggested Jira Title

Improve support bundle manifest with collection context, schema versioning, timing semantics, and AI-friendly content descriptions
