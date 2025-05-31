import random
import time
import string

def counting_sort_integers(arr):
    """Counting sort for integers"""
    if not arr:
        return arr
    min_val, max_val = min(arr), max(arr)
    count = [0] * (max_val - min_val + 1)
    for num in arr:
        count[num - min_val] += 1
    result = []
    for i, c in enumerate(count):
        result.extend([i + min_val] * c)
    return result

def tim_sort(arr):
    """Python's built-in sort"""
    return sorted(arr)

def quick_sort(arr):
    """Simple quick sort implementation"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    return quick_sort([x for x in arr if x < pivot]) + \
           [x for x in arr if x == pivot] + \
           quick_sort([x for x in arr if x > pivot])

print("Sorting Algorithm Comparison: When to Use What")
print("=" * 60)

# Test 1: Small range integers (Counting Sort excels)
print("\nTest 1: 100,000 integers, range 0-100")
arr1 = [random.randint(0, 100) for _ in range(100000)]

start = time.time()
counting_sort_integers(arr1.copy())
counting_time = time.time() - start

start = time.time()
tim_sort(arr1.copy())
tim_time = time.time() - start

print(f"Counting Sort: {counting_time:.4f}s")
print(f"Tim Sort:      {tim_time:.4f}s")
print(f"Winner: Counting Sort ({tim_time/counting_time:.1f}x faster)")

# Test 2: Large range integers (Counting Sort struggles)
print("\nTest 2: 10,000 integers, range 0-1,000,000")
arr2 = [random.randint(0, 1000000) for _ in range(10000)]

start = time.time()
counting_sort_integers(arr2.copy())
counting_time = time.time() - start

start = time.time()
tim_sort(arr2.copy())
tim_time = time.time() - start

print(f"Counting Sort: {counting_time:.4f}s")
print(f"Tim Sort:      {tim_time:.4f}s")
print(f"Winner: Tim Sort ({counting_time/tim_time:.1f}x faster)")

# Test 3: Floating point numbers (Counting Sort can't handle)
print("\nTest 3: 10,000 floating point numbers")
arr3 = [random.uniform(0, 1000) for _ in range(10000)]

print("Counting Sort: Cannot sort floats!")
start = time.time()
tim_sort(arr3.copy())
tim_time = time.time() - start
print(f"Tim Sort:      {tim_time:.4f}s")

# Test 4: Strings (Counting Sort can't handle)
print("\nTest 4: 10,000 random strings")
arr4 = [''.join(random.choices(string.ascii_letters, k=10)) for _ in range(10000)]

print("Counting Sort: Cannot sort strings!")
start = time.time()
tim_sort(arr4.copy())
tim_time = time.time() - start
print(f"Tim Sort:      {tim_time:.4f}s")

# Test 5: Nearly sorted data (Insertion sort excels)
print("\nTest 5: 10,000 nearly sorted integers")
arr5 = list(range(10000))
# Swap only 100 random pairs
for _ in range(100):
    i, j = random.randint(0, 9999), random.randint(0, 9999)
    arr5[i], arr5[j] = arr5[j], arr5[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

start = time.time()
insertion_sort(arr5.copy())
insertion_time = time.time() - start

start = time.time()
tim_sort(arr5.copy())
tim_time = time.time() - start

print(f"Insertion Sort: {insertion_time:.4f}s")
print(f"Tim Sort:       {tim_time:.4f}s")

print("\n" + "=" * 60)
print("\nBest Algorithm for Different Scenarios:")
print("- Small integer range: Counting Sort or Radix Sort")
print("- General purpose: Tim Sort (Python's sorted()) or Quick Sort")
print("- Nearly sorted data: Insertion Sort or Tim Sort")
print("- Stable sort needed: Merge Sort or Tim Sort")
print("- Limited memory: Heap Sort")
print("- Linked lists: Merge Sort")
print("- Strings/Objects: Quick Sort, Merge Sort, or Tim Sort")
print("- Guaranteed O(n log n): Merge Sort or Heap Sort") 