import time

def run_benchmark():
    # 1. Setup: Create 1 million items
    size = 1_000_000
    large_list = list(range(size))
    large_set = set(range(size))
    
    target = -1  # A value we know is NOT in either collection (Worst case scenario)

    print(f"--- Benchmarking Membership Check (Size: {size:,}) ---")

    # 2. Test the List (O(n) - Linear Time)
    start_list = time.perf_counter()
    is_in_list = target in large_list
    end_list = time.perf_counter()
    list_time = end_list - start_list
    print(f"List Lookup Time: {list_time:.6f} seconds")

    # 3. Test the Set (O(1) - Constant Time)
    start_set = time.perf_counter()
    is_in_set = target in large_set
    end_set = time.perf_counter()
    set_time = end_set - start_set
    print(f"Set Lookup Time:  {set_time:.6f} seconds")

    # 4. Senior Analysis
    if set_time > 0:
        multiplier = list_time / set_time
        print(f"\nResult: The Set was {multiplier:.1f}x faster than the List.")

if __name__ == "__main__":
    run_benchmark()