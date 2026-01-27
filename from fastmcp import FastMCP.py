from fastmcp import FastMCP

# Initialize the MCP Server
# This allows an AI agent to 'see' and 'use' your custom Python functions.
mcp = FastMCP("DataIntegrityService")

@mcp.tool()
def check_for_duplicates(numbers: list[int]) -> str:
    """
    Analyzes a list for duplicate values using an optimized Hashing pattern.
    Complexity: O(n) Time | O(n) Space.
    """
    # Using a Hash Set for O(1) average-time lookups
    seen = set()
    
    for n in numbers:
        if n in seen:
            return f"Duplicate detected: {n}"
        seen.add(n)
        
    return "No duplicates found. Data integrity verified."

if __name__ == "__main__":
    mcp.run()