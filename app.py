"""
Data Integrity Service - MCP Server
Author: V Sai Mahesh
Purpose: High-performance data validation tools for Agentic AI workflows.
"""

from fastmcp import FastMCP


mcp = FastMCP("DataIntegrityService") #initializing the framework

def check_duplicates_optimized(numbers: list[int]) -> str:
    """
    Core algorithm to detect duplicates.
    Time Complexity: O(n) - Single pass through the data.
    Space Complexity: O(n) - Stores unique elements in a hash set.
    """
    # Using a set for O(1) average time complexity lookups
    seen = set()
    for n in numbers:
        if n in seen:
            return f"Duplicate detected: {n}"
        seen.add(n)
    return "Data integrity verified. No duplicates found."

# 3. AI Tool Interface (The Agentic Layer)
@mcp.tool()
def identify_duplicates(numbers: list[int]) -> str:
    """
    Analyzes a list for duplicate values using an optimized hashing pattern.
    Useful for pre-processing datasets before analytical tasks.
    """
    # Simply call the tested logic function
    return check_duplicates_optimized(numbers)

# 4. Entry Point & Testing
if __name__ == "__main__":
    # Test cases to verify logic before server deployment
    test_cases = [
        ([1, 2, 3, 4, 5], "Expected: No duplicates"),
        ([1, 2, 3, 2, 1], "Expected: Duplicate detected: 2")
    ]

    print("=== [PHASE 1] LOGIC VERIFICATION ===")
    for data, expected in test_cases:
        result = check_duplicates_optimized(data)
        print(f"Input: {data} | Result: {result} ({expected})")

    print("\n=== [PHASE 2] STARTING MCP SERVER ===")
    # Starts the server to allow AI Agents to call the tool
    mcp.run()