import random
import time
import sys

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Heap Sort
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr

# Counting Sort
def counting_sort(arr):
    if not arr:
        return arr
    
    # Find range of values
    max_val = max(arr)
    min_val = min(arr)
    range_size = max_val - min_val + 1
    
    # Create counting array
    count = [0] * range_size
    
    # Count occurrences
    for num in arr:
        count[num - min_val] += 1
    
    # Reconstruct sorted array
    output = []
    for i in range(range_size):
        output.extend([i + min_val] * count[i])
    
    return output

# Shell Sort
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    
    return arr

# Tim Sort (Python's built-in sort)
def tim_sort(arr):
    # Python's built-in sort uses Timsort algorithm
    return sorted(arr)

# Radix Sort
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    if not arr:
        return arr
    
    # Handle negative numbers by adding offset
    min_val = min(arr)
    if min_val < 0:
        offset = -min_val
        arr = [x + offset for x in arr]
    else:
        offset = 0
    
    max_num = max(arr)
    exp = 1
    
    while max_num // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    
    # Remove offset if applied
    if offset > 0:
        arr = [x - offset for x in arr]
    
    return arr

# Bogo Sort (Warning: This is extremely inefficient!)
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def bogo_sort(arr):
    # For arrays of 100 elements, this could take forever!
    # Let's add a timeout mechanism
    start_time = time.time()
    timeout = 5  # 5 seconds timeout
    attempts = 0
    
    while not is_sorted(arr):
        random.shuffle(arr)
        attempts += 1
        
        # Check timeout
        if time.time() - start_time > timeout:
            print(f"    Bogo Sort timed out after {attempts:,} attempts!")
            return arr
    
    print(f"    Bogo Sort succeeded after {attempts:,} attempts!")
    return arr

# Main function to test all algorithms
def main():
    # Set random seed for reproducibility
    random.seed(42)
    
    # Increase recursion limit for Quick Sort with large arrays
    sys.setrecursionlimit(10000)
    
    # Generate random arrays
    def generate_array(size):
        return [random.randint(1, 10000) for _ in range(size)]
    
    # Function to run algorithm with timeout
    def run_with_timeout(algorithm, arr, timeout=30):
        import signal
        
        def timeout_handler(signum, frame):
            raise TimeoutError("Algorithm timed out")
        
        # Note: signal-based timeout only works on Unix-like systems
        # For cross-platform, we'll just warn about slow algorithms
        try:
            sorted_arr = None
            if algorithm.__name__ in ["merge_sort", "quick_sort", "counting_sort", "tim_sort", "radix_sort"]:
                sorted_arr = algorithm(arr.copy())
            else:
                sorted_arr = arr.copy()
                algorithm(sorted_arr)
            return sorted_arr, False
        except Exception as e:
            return arr, True
    
    # Dictionary of algorithms with their array sizes
    # For O(n²) algorithms, we'll use smaller sizes
    algorithms = [
        ("Bubble Sort", bubble_sort, 10000),  # Reduced to 10K for O(n²)
        ("Selection Sort", selection_sort, 10000),  # Reduced to 10K for O(n²)
        ("Insertion Sort", insertion_sort, 10000),  # Reduced to 10K for O(n²)
        ("Merge Sort", merge_sort, 1000000),
        ("Quick Sort", quick_sort, 1000000),
        ("Heap Sort", heap_sort, 1000000),
        ("Counting Sort", counting_sort, 1000000),
        ("Shell Sort", shell_sort, 1000000),
        ("Tim Sort", tim_sort, 1000000),
        ("Radix Sort", radix_sort, 1000000),
        ("Bogo Sort", bogo_sort, 20)  # Only 20 numbers for Bogo Sort!
    ]
    
    print("Sorting Algorithm Performance Test")
    print("=" * 70)
    print(f"Array sizes:")
    print(f"  - O(n log n) and better algorithms: 1,000,000 numbers")
    print(f"  - O(n²) algorithms (Bubble, Selection, Insertion): 10,000 numbers")
    print(f"  - Bogo Sort: 20 numbers")
    print("=" * 70)
    print()
    
    for name, algorithm, array_size in algorithms:
        # Generate array of appropriate size
        arr = generate_array(array_size)
        
        # Show array size for clarity
        size_str = f"({array_size:,} numbers)"
        
        print(f"{name:20} {size_str:20} ", end="", flush=True)
        
        # Measure sorting time
        start_time = time.time()
        
        try:
            # Make a copy for algorithms that modify in-place
            if name in ["Merge Sort", "Quick Sort", "Counting Sort", "Tim Sort", "Radix Sort"]:
                sorted_arr = algorithm(arr.copy())
            else:
                sorted_arr = arr.copy()
                algorithm(sorted_arr)
            
            end_time = time.time()
            elapsed_time = end_time - start_time
            
            # Verify the array is sorted
            is_correct = all(sorted_arr[i] <= sorted_arr[i+1] for i in range(len(sorted_arr)-1))
            
            print(f"Time: {elapsed_time:10.6f} seconds | Sorted: {'✓' if is_correct else '✗'}")
            
        except RecursionError:
            print(f"Time: {'FAILED':>10} | Recursion limit exceeded")
        except Exception as e:
            print(f"Time: {'ERROR':>10} | {str(e)}")
    
    print("\n" + "=" * 70)
    print("Notes:")
    print("  - O(n²) algorithms use smaller datasets (10,000) for practical timing")
    print("  - Bogo Sort has a 5-second timeout and uses only 20 numbers")
    print("  - Quick Sort may hit recursion limits with certain data patterns")

if __name__ == "__main__":
    main()
