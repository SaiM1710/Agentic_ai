# Agentic AI: Data Integrity & Sanitization Service (MCP)
Built by: **V Sai Mahesh**

This repository focuses on building high-performance **Agentic AI infrastructure** using the Model Context Protocol (MCP). I am developing a "Sanitization Layer" that automates the pre-processing burden for Data Engineers by catching errors and sensor glitches before they enter production-ready pipelines.

## The Mission
While LLMs are excellent at reasoning, they struggle with precise mathematical data validation. This service provides a deterministic "Safety Layer" that ensures AI agents are working with clean, verified datasets.

---

## Toolset: The Data Refinery

### 1. Duplicate Detection (`identify_duplicates`)
* **Problem:** Large datasets are prone to entry errors that LLMs cannot reliably catch within a limited context window.
* **Solution:** An optimized **Hashing** algorithm that scans for duplicates in a single pass.
* **Efficiency:** $O(n)$ Time Complexity | $O(n)$ Space Complexity.

### 2. ID Validation (`validate_id`)
* **Problem:** Corrupted or tampered record identifiers can cause data leakage or storage errors.
* **Solution:** A **Two-Pointer** symmetry algorithm that validates ID integrity (checks for structural corruption) without using extra memory.
* **Efficiency:** $O(n)$ Time | $O(1)$ Space.

### 3. Sensor Data Scrubbing (`sanitize_data_record`)
* **Problem:** Sensor "spikes" or malfunctions create "dirty data" that ruins Machine Learning model accuracy.
* **Solution:** A **Sliding Window** filter that identifies and removes outliers based on local averages.
* **Impact:** Delivers "Clean" data to downstream engineering teams, reducing the need for manual debugging.

---

## Engineering Insights
* **Modular Architecture:** I refactored the code to separate "Core Logic" from "MCP Tool Wrappers." This makes the code more testable and allows the math logic to be reused in other applications (web, mobile, etc.).
* **Memory Optimization:** In the ID validation tool, I chose a Two-Pointer approach specifically to achieve **constant space complexity ($O(1)$)**, ensuring the tool can scale regardless of ID length.

---

## Tech Stack
* **Language:** Python 3.11+
* **Framework:** FastMCP (Model Context Protocol)
* **Testing:** Verified via Node.js v22 (LTS) & MCP Inspector
* **Version Control:** Git/GitHub

---

## Verification & Debugging
I use the **MCP Inspector** to verify that the Python backend correctly handles JSON-RPC requests from AI agents.

### Test Case: Data Sanitization
* **Input ID:** `"RADAR"` (Symmetric/Valid)
* **Input Data:** `[10, 11, 10, 100, 11]`
* **Expected Result:** The `100` is identified as a spike and removed.
* **Status:** Verified 

![Data Sanitization Success](./data_sanitization_success.png)

---

## Future Roadmap
- [ ] **Bulk Processing:** Support for cleaning entire `.csv` files.
- [ ] **Missing Data Handling:** Adding logic to interpolate or fill `null` values in sensor streams.
- [ ] **Feature Scaling:** Implementing Z-score normalization for ML-ready feature engineering.