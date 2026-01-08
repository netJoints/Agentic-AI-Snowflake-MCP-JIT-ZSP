# Securing Agentic AI and MCP Access for Enterprises using JIT/ZSP Approach

## Overview
This project shows how to build a **production-ready agentic AI workflow** on **Snowflake AI Data Cloud** using the **Model Context Protocol (MCP)** and enforcing **just-in-time (JIT) access** with **zero standing privileges (ZSP)**. The goal is to enable AI agents to securely discover tools, query governed data (both structured and unstructured), and orchestrate multi-step tasks—**without long-lived credentials or broad, static permissions**.

- **MCP** standardizes how agents discover and invoke tools across systems, including Snowflake’s Cortex Search, Cortex Analyst, and Cortex Agents.
- **Snowflake MCP server** exposes these capabilities over a consistent interface to MCP clients (e.g., Claude Desktop), supporting SQL execution, object management, and semantic views.
- **JIT/ZSP** authorization patterns remove hard-coded secrets and grant narrowly scoped, time-bound access for agent workflows—addressing key MCP runtime security gaps.

## Design Flow
```
+---------------------------+         +-----------------------------------+
| MCP Client (Agent UI)     |  --->   | Snowflake-managed MCP Server      |
| e.g., Claude Desktop      |         | - Cortex Search (unstructured)    |
|                           |         | - Cortex Analyst (structured)     |
| - Tool discovery          |         | - Cortex Agents (orchestration)   |
| - Invocation              |         | - SQL / Object mgmt / Semantics    |
+---------------------------+         +-----------------------------------+
            |                                      |
            | OAuth 2.1 access tokens              | RBAC, masking, row policies
            v                                      v
+---------------------------+         +-----------------------------------+
| JIT Credential Broker     |  --->   | Snowflake Account (Governed Data) |
| (Zero Standing Privileges)|         | - Tables, docs, vectors           |
| - Short-lived session     |         | - Policies & tags                 |
| - Least privilege         |         | - Observability                   |
+---------------------------+         +-----------------------------------+
```

# Architecture

<img width="558" height="603" alt="image" src="https://github.com/user-attachments/assets/a2ab8191-0b69-4064-b47c-04d23e14744c" />

## Demo Recorded Video
Watch the walkthrough and end-to-end flow in the **demo video**: https://youtu.be/j6x30dqqnYs

## Prerequisites
- A Snowflake account with **Cortex** features enabled and roles to create/manage MCP server objects.
- An **MCP client** (e.g., Claude Desktop) or a compatible agent runtime.
- A **JIT/ZSP** broker (e.g., your enterprise access platform) capable of issuing short-lived credentials to Snowflake.

## What can you do for your implementation
- Ask the agent to answer questions over **structured data** via **Cortex Analyst** (semantic models).
- Retrieve insights from **unstructured content** via **Cortex Search** (RAG-style retrieval).
- Run **multi-step plans** with **Cortex Agents**, choosing the right tool and reflecting on intermediate outputs.
- Execute **scoped SQL** with server-side enforcement and audit, avoiding broad access.


## Potential Production Setup (High level)
1. **Configure Snowflake MCP server**: register Cortex Search/Analyst/Agents services and (optionally) SQL/object tools in the server configuration.
2. **Enable OAuth** between MCP client and server; avoid underscores in hostnames and prefer least-privileged roles.
3. **Wire JIT/ZSP**: integrate the credential broker to mint **time-bound** Snowflake access per agent task; remove hard-coded tokens.
4. **Govern data**: apply masking, row policies, and tags to sensitive columns; index vectors for retrieval where needed.

## Configuration tips
- Keep MCP tool descriptions **mutually exclusive** and **highly descriptive** to reduce tool confusion and poisoning risks.
- Verify third-party MCP servers before use; prefer **OAuth** over programmatic tokens; set PAT roles to **least privilege**.

## Security: JIT + ZSP
- **Zero Standing Privileges**: no permanent secrets; agents get **just-enough**, **just-in-time** access with full audit.
- **Runtime enforcement** complements MCP: OAuth secures the channel, JIT/ZSP governs **what** the agent can do **right now**.


## References
- Snowflake Documentation — *Snowflake-managed MCP server (OAuth 2.1, RBAC, recommendations)*
- Snowflake-Labs Open Source MCP Server — *Cortex tools, SQL orchestration, semantic views*
- Snowflake Blog — *MCP servers unify & extend data agents; Cortex Agents orchestration*
- netJoints Whitepaper — *Runtime security for MCP servers; JIT/ZSP controls*
- Britive Blog — *Securing MCP workflows; OAuth 2.1 & eliminating hard-coded creds*

## License
Unless otherwise noted, content is provided under the repository’s license. See `LICENSE` if present.


https://youtu.be/j6x30dqqnYs
