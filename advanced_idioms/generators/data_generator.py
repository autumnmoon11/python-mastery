import random
from datetime import datetime

def generate_mock_log(filename="server.log", lines=1000):
    levels = ["INFO", "DEBUG", "WARNING", "ERROR", "CRITICAL"]
    messages = [
        "User logged in", 
        "Database connection timeout", 
        "Disk space low", 
        "CPU usage exceeded 90%", 
        "Unauthorized access attempt",
        "Kernel panic: out of memory"
    ]
    
    with open(filename, "w") as f:
        for _ in range(lines):
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            level = random.choice(levels)
            msg = random.choice(messages)
            f.write(f"[{timestamp}] {level}: {msg}\n")
    print(f"Created {filename} with {lines} lines.")

if __name__ == "__main__":
    generate_mock_log()