from typing import Generator

def get_critical_errors(file_path: str) -> Generator[str, None, None]:
    """
    A memory-efficient generator that streams lines from a file.
    Only yields lines containing 'CRITICAL'.
    """
    try:
        # Context Manager ensures the file handle is automatically closed, 
        # preventing memory leaks or file locks even if the generator is interrupted.
        with open(file_path, 'r') as file:
            for line in file:
                if "CRITICAL" in line:
                    yield line.strip()
    except FileNotFoundError:
        print("Log file not found.")

# Usage
# Even if the file is 100GB, this loop only holds 1 line in memory at a time.

if __name__ == "__main__":
    raw_errors = get_critical_errors("server.log")
    prefixed_errors = (f"SERVER_A: {line}" for line in raw_errors) # generator expression

    for error in prefixed_errors:
        print(error)