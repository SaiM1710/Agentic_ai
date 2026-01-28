# Agentic AI: Data Integrity Service (MCP)

This repository focuses on building high-performance **Agentic AI infrastructure** using the Model Context Protocol (MCP). By bridging the gap between LLMs and deterministic Python logic, I am creating tools that allow AI agents to verify data integrity with mathematical precision.

## The Core Tool: Hashing-Based Duplicate Detection
While LLMs are excellent at reasoning, they struggle with accurate data validation in large datasets. This service provides a "Safety Layer" for AI agents.

### Tool: `identify_duplicates`
* **Problem:** Identifying duplicates in large lists is prone to error when handled by an LLM's context window alone.
* **Solution:** An optimized **Hashing** algorithm that scans the dataset in a single pass.
* **Efficiency:** $O(n)$ Time Complexity | $O(n)$ Space Complexity.
* **Impact:** Ensures 100% accuracy in data validation before the AI performs further analysis.



## Tech Stack
* **Language:** Python 3.11+
* **Framework:** FastMCP (Model Context Protocol)
* **Testing:** Verified via Node.js v22 (LTS) & MCP Inspector
* **Version Control:** Git/GitHub

## Setup & Local Testing
1. **Clone & Environment:**
   ```powershell
   git clone [https://github.com/SaiM1710/Agentic_ai.git](https://github.com/SaiM1710/Agentic_ai.git)
   cd Agentic_ai
   python -m venv venv
   .\venv\Scripts\activate
   pip install fastmcp

## Verification & Debugging
To ensure the Python backend and the MCP interface are communicating correctly, I use the **MCP Inspector**. This allows for real-time testing of the tool's JSON-RPC responses.

### Test Case: Duplicate Detection
* **Input:** `[10,20,30,10,10,40]`
* **Expected Output:** `Duplicate detected: 10`
* **Status:** Verified 

![MCP Inspector Verification](app_inspector_verified.png)
