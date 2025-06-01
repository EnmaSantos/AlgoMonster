import random

def is_sorted(arr):
    """Check if the array is sorted in ascending order"""
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def bogo_sort(arr):
    """Bogo sort algorithm - randomly shuffle until sorted"""
    attempts = 0
    while not is_sorted(arr):
        random.shuffle(arr)
        attempts += 1
        # Print progress every 1000 attempts to avoid overwhelming output
        if attempts % 1000 == 0:
            print(f"Attempt {attempts}: {arr}")
    
    print(f"Sorted in {attempts} attempts!")
    return arr

# Example usage
if __name__ == "__main__":
    # Test with a small array (bogo sort is very inefficient!)
    test_array = [3, 1, 4, 7, 2, 5, 6, 7, 6, 67, 654]
    print(f"Original array: {test_array}")
    
    # Make a copy to sort (bogo_sort modifies the original)
    array_to_sort = test_array.copy()
    sorted_array = bogo_sort(array_to_sort)
    
    print(f"Sorted array: {sorted_array}")
    
    # Test with an even smaller array for demonstration
    small_array = [2, 1, 3]
    print(f"\nSmall array: {small_array}")
    small_copy = small_array.copy()
    bogo_sort(small_copy)
    print(f"Sorted: {small_copy}")