import time
import concurrent.futures
from pathlib import Path
from algorithms.efficiency.large_file_search import find_in_large_file

def concurrent_search_robust(file_path: Path, target_ids: list, executor_class):
    """
    Executes searches with granular error handling and 'as_completed' logic.
    This pattern is preferred for production-grade telemetry and resilience.
    """
    results = {}
    with executor_class() as executor:
        # Submit all tasks and map the Future object to the ID for tracking
        future_to_id = {
            executor.submit(find_in_large_file, file_path, tid): tid 
            for tid in target_ids
        }
        
        # Process results as they finish (non-blocking order)
        for future in concurrent.futures.as_completed(future_to_id):
            target_id = future_to_id[future]
            try:
                # Exception is raised if the task failed
                data = future.result()
                results[target_id] = data
            except Exception as exc:
                # In a real system, we'd log this to a file
                results[target_id] = f"Error: {exc}"
                
    return results

def run_benchmarks(file_path: Path, ids: list):
    """Compares execution strategies using the robust pattern."""
    print(f"--- Benchmarking {len(ids)} searches ---")

    # 1. ThreadPool (I/O Bound - Great for files)
    start = time.perf_counter()
    t_results = concurrent_search_robust(file_path, ids, concurrent.futures.ThreadPoolExecutor)
    t_duration = time.perf_counter() - start
    print(f"Threaded:      {t_duration:.4f}s (Found {len(t_results)} items)")

    # 2. ProcessPool (CPU Bound - High overhead)
    start = time.perf_counter()
    p_results = concurrent_search_robust(file_path, ids, concurrent.futures.ProcessPoolExecutor)
    p_duration = time.perf_counter() - start
    print(f"Multiprocess:  {p_duration:.4f}s (Found {len(p_results)} items)")

if __name__ == "__main__":
    DATA_FILE = Path("data/massive_sorted.csv")
    SEARCH_LIST = [f"{i:08}" for i in range(100, 200)] 
    
    if not DATA_FILE.exists():
        print("Please run the generator first.")
    else:
        # Run the robust search and print the first few results as a sample
        final_results = concurrent_search_robust(DATA_FILE, SEARCH_LIST[:5], concurrent.futures.ThreadPoolExecutor)
        for tid, res in final_results.items():
            print(f"Sample Result: ID {tid} -> {res}")
            
        # Then run the benchmark to see the timing
        run_benchmarks(DATA_FILE, SEARCH_LIST)