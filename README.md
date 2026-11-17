# openclaw-genpark-visual-sleuth

[![Organization](https://img.shields.io/badge/AlphaPark-OpenSource-blue.svg)](https://github.com/Alpha-Park)
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard-orange.svg)](https://modelcontextprotocol.io)
[![MCP SDK](https://img.shields.io/badge/MCP-SDK_Required-blue.svg)](requirements.txt)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](#)
[![Security Rating](https://img.shields.io/badge/Status-Grade_A_Production-success.svg)](#)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Production-hardened OpenClaw GenPark Agent skill with a standard-library client and an MCP SDK server. Provides high-throughput deterministic execution, cryptographic security, and game-theoretic optimization via the Model Context Protocol (MCP).

---

## Architecture & Data Flow

```mermaid
flowchart TD
    Input[Incoming Agent Telemetry / Task Input] --> Core["OpenClawGenParkVisualSleuth"]
    Core --> Model[Mathematical Logic Engine]
    Model --> MCPResponse[Deterministic JSON Output / MCP Tool Result]
```

---

## Quickstart & Usage

### 1. Direct Python Client Execution
```bash
python example_usage.py
```

### 2. Standalone MCP Server Launch

The core Python client uses only the standard library. Running the MCP server requires **Python 3.10+** and the official **`mcp>=1.0.0,<2` SDK**. From the repository directory:

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

On Windows, use `.venv\Scripts\python.exe` instead. Configure the MCP client to use this environment's Python executable. The server runs locally over stdio; the GitHub repository URL is not a remote MCP endpoint.

Run the native STDIO MCP server:
```bash
.venv/bin/python mcp_server.py
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
