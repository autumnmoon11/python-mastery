import time
import sys
import os

# Adding the root path so we can import our decorator from a different folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from advanced_idioms.decorators.time_execution import time_execution_decorator

@time_execution_decorator
def check_list(data_list, target):
    """Linear search (O(n))"""
    return target in data_list

@time_execution_decorator
def check_set(data_set, target):
    """Hash table lookup (O(1))"""
    return target in data_set

def run_benchmark():
    size = 1_000_000
    large_list = list(range(size))
    large_set = set(range(size))
    target = -1

    print(f"--- Benchmarking Membership Check (Size: {size:,}) ---")
    
    # The decorator handles the start/end time and the print statement
    check_list(large_list, target)
    check_set(large_set, target)


if __name__ == "__main__":
    run_benchmark()