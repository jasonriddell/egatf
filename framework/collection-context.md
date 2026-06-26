# Collection Context

**Document type:** Framework detail  
**Status:** Draft v0.6  
**Repository path:** `framework/collection-context.md`

---

## Relationship to the Three-Loop Model

Collection Context belongs to the Evidence Loop. Its purpose is to prevent reasoning from starting until the evidence package scope, timing, version, and limitations are understood.

---

## Purpose

This document defines Collection Context within EGATF.

Collection Context is metadata describing how an evidence package was created, what it contains, what time periods its contents represent, and how those contents should be interpreted.

For support bundle analysis, this matters because a support bundle is not simply a bag of files. It is a time-bounded evidence package created by a particular collector version, from a particular environment, with different data sources captured from different effective times.

---

## Core Principle

Evidence packages should describe their own collection context.

AI should not be asked to infer timing, scope, source meaning, version compatibility, or collection limitations from raw files alone.

---

## Placement in EGATF

Collection Context sits inside the Evidence stage:

```text
Reported Context
    ↓
Collection Context
    ↓
Raw Source Material
    ↓
Evidence Preparation
    ↓
Prepared Evidence Base
    ↓
Information
```

It is not diagnosis.

It constrains how raw source material and prepared evidence may safely be interpreted.

---

## Why Collection Context Matters

A support bundle may be created at one time while containing logs or metrics from an earlier requested window.

Example:

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

Without Collection Context, AI may incorrectly correlate tablet state at T with log events from T - 7 to T - 5.

Correct interpretation:

> Tablet metadata and tablet reports are collection-time snapshots and may not represent tablet state during the requested log window.

---

## Evidence Package Manifest

An Evidence Package Manifest is a machine-readable description of the collected evidence package.

For support bundles, this may be implemented as an expanded `manifest.json`, or as a combination of:

```text
manifest.json
bundle_context.json
file_index.json
```

The manifest should help humans, deterministic tools, and AI understand:

- What was collected
- When each component was collected
- Which system versions are represented
- Which collection software produced the bundle
- What each component means
- Which files and directories are present
- Which evidence sources reflect the requested time window
- Which evidence sources reflect collection time
- Which evidence sources have known limitations

The manifest should not attempt to diagnose the issue.

---

## Recommended Manifest Sections

### 1. Bundle Provenance

Bundle Provenance describes what created the bundle and which schema should be used to interpret it.

Example fields:

```json
{
  "bundleUUID": "1a233260-4402-4ea2-9442-9678694bd281",
  "supportBundleVersion": "2026.1.0",
  "supportBundleSchemaVersion": "1.0",
  "createdAt": "2025-05-13T09:58:45Z",
  "createdBy": "YBA",
  "collectorName": "yba-support-bundle",
  "collectorVersion": "2026.1.0"
}
```

Why this matters:

- Automated tools can select the correct parser.
- Collection formats can evolve safely.
- Breaking format changes can be tied to explicit schema changes.
- AI can be told which schema describes the package.

---

### 2. Environment Identity

Environment Identity describes the system represented by the evidence package.

Example fields:

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

Why this matters:

- YBA and YBDB versions may differ.
- YBA may always be latest while universes run older YBDB versions.
- AI and deterministic tools must avoid applying behavior from the wrong version.
- Deployment type affects expected files and interpretation.

---

### 3. Collection Windows

Collection Windows describe what time period each evidence source represents.

Example fields:

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

Why this matters:

- Prevents false correlations.
- Clarifies whether a file describes history or current state.
- Helps AI interpret time-sensitive evidence safely.
- Helps deterministic tools enforce time-window compatibility.

---

### 4. Metric Collection Context

Metric Collection Context describes metric availability, resolution, and duration.

Example fields:

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

---

### 5. Component Descriptions

Component Descriptions provide AI-friendly and human-friendly descriptions of bundle contents.

Example fields:

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

---

### 6. File Index

The File Index lists important directories and files included in the evidence package.

Example fields:

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

---

## What the Manifest Should Not Do

The Evidence Package Manifest should not state the root cause.

Avoid:

```text
The issue was caused by compaction.
The failing node is tserver-2.
The customer impact was due to master leader change.
```

Prefer:

```text
TServer logs are present for nodes A, B, and C.
Tablet metadata was collected at bundle creation time.
Metrics cover this specific window.
Master logs should be reviewed across all masters because leadership can change.
```

The manifest describes collection context. It does not perform diagnosis.

---

## Design Recommendation

Prefer adding explicit schema and collector versions.

Recommended fields:

```json
{
  "supportBundleSchemaVersion": "1.0",
  "supportBundleCollectorVersion": "2026.1.0"
}
```

This allows future parser selection such as:

```text
If schema version is 1.x, use parser family v1.
If schema version is 2.x, use parser family v2.
If schema version is unknown, fail safely or use best-effort mode.
```

This supports intentional support bundle format evolution without silently breaking automated analysis tools.

---

## Open Questions

1. Should collection context remain in `manifest.json`, or be split into `bundle_context.json` and `file_index.json`?
2. Should component descriptions be embedded in every bundle or referenced by schema version?
3. Should the manifest include expected versus actual files?
4. Should the manifest include collection errors and partial failures?
5. Should each component have a `windowType`?
6. Should metrics have separate retention, resolution, and scrape-level metadata?
7. Should the manifest include parser compatibility hints?
8. Should AI guidance be considered part of the schema or documentation?
9. Should sensitive fields be omitted, hashed, or redacted?
10. Should manifests be validated against a JSON Schema?
