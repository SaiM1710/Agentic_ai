# Agentic AI: Data Integrity & Sanitization Service (MCP)
Built by: **V Sai Mahesh**

This repository focuses on building high-performance **Agentic AI infrastructure** using the Model Context Protocol (MCP). I am developing a "Sanitization Layer" that automates the pre-processing burden for Data Engineers by catching errors and sensor glitches before they enter production-ready pipelines.

## The Mission
While LLMs are excellent at reasoning, they struggle with precise mathematical data validation. This service provides a deterministic "Safety Layer" that ensures AI agents are working with clean, verified datasets.

---

## Toolset: The Data Refinery

### 1. Range-Based Search (`get_records_by_range`)
* **Problem:** Searching for a block of records (e.g., "all entries between ID 100-200") in a Hash Map requires a linear scan, which is slow ($O(n)$).
* **Solution:** Implemented a **Sorted Index** sidecar to maintain order.
* **Efficiency:** Uses **Binary Search** via the `bisect` module to achieve **$O(\log n)$** boundary detection, allowing the AI to "jump" to relevant data slices instantly.

### 2. Bulk ETL Pipeline (`process_data_batch`)
* **Problem:** Processing data one-by-one is inefficient for enterprise-scale datasets.
* **Solution:** Integrated **Pandas** for batch ingestion and transformation.
* **Efficiency:** Combined with **Hashing-based deduplication** for $O(n)$ ingestion speed.

### 3. In-Memory Vault (`get_clean_record`)
* **Purpose:** Acts as a high-speed cache for sanitized data.
* **Efficiency:** Achieves **$O(1)$ Point Retrieval**, allowing AI agents to fetch specific records instantly.

### 4. ID Validation (`validate_id`)
* **Solution:** A **Two-Pointer** symmetry algorithm that validates ID integrity without using extra memory.
* **Efficiency:** $O(n)$ Time | $O(1)$ Space.

### 5. Sensor Data Scrubbing (`sanitize_data_record`)
* **Solution:** A **Sliding Window** filter that identifies and removes outliers based on local averages to prevent "dirty data" from reaching ML models.

---

## Engineering Insights
* **Dual-Indexing Strategy:** I implemented a hybrid storage architecture. A **Hash Map** handles individual record lookups ($O(1)$), while a **Sorted List** acts as a search index for range queries ($O(\log n)$). This mimics how production databases like PostgreSQL optimize performance.
* **Stateful Search:** By maintaining an in-memory index, I’ve reduced the compute cost for AI agents that need to analyze specific windows of data.
* **Memory Optimization:** Prioritized in-place algorithms and constant space complexity ($O(1)$) where possible to ensure the service remains lightweight.

---

## Tech Stack
* **Language:** Python 3.11+
* **Framework:** FastMCP (Model Context Protocol)
* **Libraries:** Pandas (Batch Processing), Bisect (Binary Search)
* **Testing:** Verified via Node.js v22 (LTS) & MCP Inspector

---

## How to Run
1. **Setup:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   pip install pandas fastmcp