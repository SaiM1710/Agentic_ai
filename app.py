import math
from fastmcp import FastMCP

mcp = FastMCP("DataSanitizer")

# 1. Logic for ID Validation
def pre_validate_logic(record_id: str) -> bool:
    """Pure logic function for ID symmetry."""
    left = 0
    right = len(record_id) - 1
    while left < right:
        if not record_id[left].isalnum():
            left += 1
            continue
        if not record_id[right].isalnum():
            right -= 1
            continue
        if record_id[left].lower() != record_id[right].lower():
            return False
        left += 1
        right -= 1
    return True

# 2. Logic for Scrubbing Spikes
def scrub_logic(data_list: list[float]) -> list[float]:
    """Pure logic function for removing outliers."""
    if len(data_list) < 3:
        return data_list
    sanitized = []
    window = 3
    for i in range(len(data_list)):
        if i < window:
            sanitized.append(data_list[i])
            continue
        avg = sum(data_list[i-window : i]) / window
        if data_list[i] > (avg * 3):
            continue
        sanitized.append(data_list[i])
    return sanitized

# --- MCP TOOL WRAPPERS ---

@mcp.tool()
def validate_id(record_id: str) -> bool:
    """Checks if a Record ID has been corrupted using symmetry logic."""
    return pre_validate_logic(record_id)

@mcp.tool()
def sanitize_data_record(record_id: str, sensor_values: list[float]) -> dict:
    """
    Main pipeline to sanitize raw records.
    Ensures the ID is valid and removes sensor malfunctions.
    """
    # Use our logic functions
    is_valid = pre_validate_logic(record_id)
    
    if not is_valid:
        return {"status": "REJECTED", "reason": "Invalid ID format"}
        
    cleaned_data = scrub_logic(sensor_values)
    
    return {
        "status": "SANITIZED",
        "record_id": record_id,
        "final_data": cleaned_data
    }

if __name__ == "__main__":
    mcp.run()