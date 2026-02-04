import pandas as pd
from fastmcp import FastMCP

# Initialize our service
mcp = FastMCP("Data_Integrity_Service")

# The 'Vault' is our high-speed index (Hash Map)
# We use this to store cleaned data for instant retrieval
data_vault = {}

# --- BUSINESS LOGIC ---

def is_valid_identifier(record_id: str) -> bool:
    """
    Uses the Two-Pointer pattern to ensure ID integrity.
    Interview Note: O(n) Time | O(1) Space.
    """
    clean_id = "".join(char.lower() for char in record_id if char.isalnum())
    left, right = 0, len(clean_id) - 1
    
    while left < right:
        if clean_id[left] != clean_id[right]:
            return False
        left += 1
        right -= 1
    return True

def remove_sensor_spikes(vitals: list[float]) -> list[float]:
    """
    Filters out noise using a Sliding Window average.
    If a value is 3x the local average, we consider it a sensor glitch.
    """
    if len(vitals) < 3:
        return vitals
        
    sanitized_data = []
    window_size = 3
    
    for i in range(len(vitals)):
        if i < window_size:
            sanitized_data.append(vitals[i])
        else:
            # Calculate the average of the last 3 'clean' readings
            local_avg = sum(vitals[i-window_size:i]) / window_size
            
            # Skip values that are mathematically impossible/outliers
            if vitals[i] > (local_avg * 3):
                continue
            sanitized_data.append(vitals[i])
            
    return sanitized_data

# --- MCP TOOLS (THE ETL PIPELINE) ---

@mcp.tool()
def process_data_batch(csv_path: str) -> dict:
    """
    Extracts data from a CSV, transforms it, and loads it into the Vault.
    Uses Hashing to deduplicate records in one pass.
    """
    try:
        # 1. EXTRACT: Read the raw file
        df = pd.read_csv(csv_path)
        
        # Track our progress for the final report
        metrics = {"successful": 0, "duplicates": 0, "invalid_ids": 0}
        
        # 2. TRANSFORM & LOAD: Process row by row
        for _, row in df.iterrows():
            record_id = str(row['id']).strip()
            
            # DEDUPLICATION: O(1) Check using Hashing
            if record_id in data_vault:
                metrics["duplicates"] += 1
                continue
            
            # VALIDATION
            if not is_valid_identifier(record_id):
                metrics["invalid_ids"] += 1
                continue
            
            # CLEANING: Parse the vitals string into a list of numbers
            try:
                raw_readings = [float(x) for x in str(row['vitals']).split(',')]
                data_vault[record_id] = remove_sensor_spikes(raw_readings)
                metrics["successful"] += 1
            except ValueError:
                metrics["invalid_ids"] += 1 # Bad data format in vitals
                
        return {
            "status": "Pipeline Run Complete",
            "summary": metrics,
            "total_records_in_vault": len(data_vault)
        }
        
    except FileNotFoundError:
        return {"error": f"The file at {csv_path} was not found."}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}

@mcp.tool()
def get_clean_record(record_id: str) -> dict:
    """Retrieves a sanitized record instantly from memory."""
    record = data_vault.get(record_id)
    if record:
        return {"id": record_id, "vitals": record}
    return {"status": "error", "message": "Record ID not found in the sanitized vault."}

if __name__ == "__main__":
    mcp.run()