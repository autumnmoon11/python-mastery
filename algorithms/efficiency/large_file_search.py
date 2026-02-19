import csv
from pathlib import Path

def generate_sorted_data(filename: str, num_rows: int):
    """Generates a sorted CSV file for binary search testing."""
    file_path = Path(filename)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    print(f"Generating {num_rows} rows in {filename}...")
    
    with open(file_path, "w", newline='') as f:
        writer = csv.writer(f)
        for i in range(1, num_rows + 1):
            # We pad the ID with zeros to ensure lexicographical 
            # sorting matches numerical sorting (0001, 0002, etc.)
            writer.writerow([f"{i:08}", f"Data_Point_{i}"])
            
    print(f"File created: {file_path.stat().st_size / (1024*1024):.2f} MB")


def find_in_large_file(file_path: str, target_id: str) -> str:
    """
    Binary search on a sorted file's byte offsets.
    Complexity: O(log(bytes) * line_length)
    Memory: O(1) - Constant regardless of file size.
    """
    if not file_path.exists():
        return "Error: File not found."
    
    file_size = file_path.stat().st_size
    
    with open(file_path, "rb") as f:
        low = 0
        high = file_size
        
        while low <= high:
            mid = low + (high - low) // 2
            f.seek(mid)
            
            # Skip the current potentially partial line,
            # UNLESS we are at the very beginning of the file.
            if mid != 0:
                f.readline()
            
            # Record our position after seeking the start of a line
            current_pos = f.tell()
            line_bytes = f.readline()

            if not line_bytes: # End of file
                high = mid - 1
                continue

            line = line_bytes.decode('utf-8').strip()
            if not line:
                continue
                
            # Compare
            current_id = line.split(',')[0]
            
            if current_id == target_id:
                return f"FOUND at byte {current_pos}: {line}"
            elif current_id < target_id:
                low = mid + 1
            else:
                high = mid - 1
                
    return "ID not found in file"

if __name__ == "__main__":
    DATA_FILE = Path("data/massive_sorted.csv")
    NUM_ROWS = 1_000_000

    # Generate data if it doesn't exist
    if not DATA_FILE.exists():
        generate_sorted_data(str(DATA_FILE), NUM_ROWS)
    else:
        print(f"Using existing data file: {DATA_FILE}")

    print("\n--- Starting Binary Search on Disk ---")

    # Test Cases
    test_ids = [
        "00000001",  # Boundary: First ID
        "00524001",  # Mid-file ID
        "01000000",  # Boundary: Last ID
        "99999999"   # Not found
    ]

    for target in test_ids:
        print(f"Searching for {target}...")
        result = find_in_large_file(DATA_FILE, target)
        print(f"Result: {result}")