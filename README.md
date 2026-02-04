# Agentic AI: Data Integrity & Sanitization Service (MCP)
Built by: **V Sai Mahesh**

This repository focuses on building high-performance **Agentic AI infrastructure** using the Model Context Protocol (MCP). I am developing a "Sanitization Layer" that automates the pre-processing burden for Data Engineers by catching errors and sensor glitches before they enter production-ready pipelines.

## The Mission
While LLMs are excellent at reasoning, they struggle with precise mathematical data validation. This service provides a deterministic "Safety Layer" that ensures AI agents are working with clean, verified datasets.

---

## Toolset: The Data Refinery

### 1. Bulk ETL Pipeline (`process_data_batch`) — **NEW**
* **Problem:** Manual data entry is slow; processing data one-by-one is inefficient for enterprise-scale datasets.
* **Solution:** Integrated **Pandas** to extract data from CSV files, transform it using existing logic, and load it into a centralized vault.
* **Efficiency:** Uses **Hashing-based deduplication** to ensure $O(n)$ performance during ingestion.

### 2. In-Memory Vault (`get_clean_record`) — **NEW**
* **Purpose:** Acts as a high-speed cache for sanitized data.
* **Efficiency:** Achieves **$O(1)$ Retrieval Time**, allowing AI agents to fetch clean records instantly without re-processing the raw file.

### 3. ID Validation (`validate_id`)
* **Problem:** Corrupted or tampered record identifiers can cause data leakage or storage errors.
* **Solution:** A **Two-Pointer** symmetry algorithm that validates ID integrity (checks for structural corruption) without using extra memory.
* **Efficiency:** $O(n)$ Time | $O(1)$ Space.

### 4. Sensor Data Scrubbing (`sanitize_data_record`)
* **Problem:** Sensor "spikes" or malfunctions create "dirty data" that ruins Machine Learning model accuracy.
* **Solution:** A **Sliding Window** filter that identifies and removes outliers based on local averages.

---

## Engineering Insights
* **Stateful Storage:** Introduced an in-memory **Hash Map (Dictionary)** to store processed data. This prevents redundant computations and provides a "Source of Truth" for AI agents querying the service.
* **Modular Architecture:** Separated "Core Logic" from "MCP Tool Wrappers," making the code testable and reusable for web or mobile backends.
* **Memory Optimization:** Prioritized algorithms like Two-Pointer to achieve **constant space complexity ($O(1)$)** where possible.

---

## Tech Stack
* **Language:** Python 3.11+
* **Framework:** FastMCP (Model Context Protocol)
* **Libraries:** Pandas (Batch Processing)
* **Testing:** Verified via Node.js v22 (LTS) & MCP Inspector

---

## How to Run
To see the pipeline in action without screenshots:

1. **Setup:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   pip install pandas fastmcp