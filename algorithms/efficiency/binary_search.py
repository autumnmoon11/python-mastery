from typing import Any, List, Optional

def binary_search(arr: List[Any], target: Any) -> Optional[int]:
    """
    Performs a type-agnostic binary search to find the index of a target element.

    This implementation demonstrates the 'Divide and Conquer' pattern with O(log n) 
    time complexity. While Python's 'bisect' module provides a C-optimized version 
    of this logic for production use, this manual implementation serves as a 
    reference for pointer-based search logic and memory-efficient indexing.

    Args:
        arr (List[Any]): A sorted list of comparable elements.
        target (Any): The element to locate.

    Returns:
        Optional[int]: The index of the target if found, otherwise None.
        
    Complexity:
        Time: O(log n) - The search space is halved each iteration.
        Space: O(1) - Search is performed in-place with three pointers.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1

    return None

if __name__ == "__main__":
    # Test Case 1: Integer in list
    ids = [10, 22, 35, 47, 50, 63, 75, 88, 91, 100]
    print(f"Test 1 (ID 75): Found at index {binary_search(ids, 75)}")

    # Test Case 2: Integer NOT in list
    print(f"Test 2 (ID 55): Found at index {binary_search(ids, 55)}")

    # Test Case 3: Word in a sorted dictionary (List of strings)
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    target_word = "elderberry"
    print(f"Test 3 (Word '{target_word}'): Found at index {binary_search(words, target_word)}")

    # Test Case 4: Word NOT in dictionary
    print(f"Test 4 (Word 'kiwi'): Found at index {binary_search(words, 'kiwi')}")