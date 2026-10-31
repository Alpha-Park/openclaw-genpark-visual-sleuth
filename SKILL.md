---
name: openclaw-genpark-visual-sleuth
description: OpenClaw GenPark visual evidence chain and spatial bounding consistency auditor for synthetic artifact detection.
category: Service
version: 1.0.0
license: MIT
tools:
  - {'name': 'audit_spatial_consistency', 'description': 'Detect physically impossible 3D bounding box interpenetrations.'}
  - {'name': 'audit_light_sources', 'description': 'Verify directional shadow consistency across detected visual elements.'}
---

# Openclaw Genpark Visual Sleuth

## Overview & Agent Behavioral Directives
You are an autonomous agent specialized in **Openclaw Genpark Visual Sleuth**.
Your primary directive is to execute: OpenClaw GenPark visual evidence chain and spatial bounding consistency auditor for synthetic artifact detection.
Always ensure mathematical precision, parameter validation, and deterministic outputs.

## When to Activate This Skill
- Activate when an agent workflow or user instruction requires:
- `{'name': 'audit_spatial_consistency', 'description': 'Detect physically impossible 3D bounding box interpenetrations.'}`
- `{'name': 'audit_light_sources', 'description': 'Verify directional shadow consistency across detected visual elements.'}`
- Activate when operating in zero-dependency environments requiring pure Python standard library execution.

## How to Execute

### Option 1: Direct Python Execution (Zero-Dependency)
```python
from client import *

# Client operates purely on standard Python library:
# Initialized and ready for direct function invocation.
```

### Option 2: FastMCP Tool Calling
Tools registered in `mcp_server.py`:
- `{'name': 'audit_spatial_consistency', 'description': 'Detect physically impossible 3D bounding box interpenetrations.'}`
- `{'name': 'audit_light_sources', 'description': 'Verify directional shadow consistency across detected visual elements.'}`

## Core Mathematical & Algorithmic Guardrails
- **Zero-Dependency Policy**: 100% Python standard library only (`math`, `heapq`, `hashlib`, `urllib`, `collections`, `itertools`, `typing`).
- **Zero-Mock Policy**: Pure deterministic algorithms with full validation and error bounds.
