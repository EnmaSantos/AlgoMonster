"""
Common Interview Problems That Use Sorting
These are the types of problems you'll actually see!
"""

def merge_intervals(intervals):
    """
    Leetcode #56 - Merge Intervals
    Given intervals [[1,3],[2,6],[8,10],[15,18]], return [[1,6],[8,10],[15,18]]
    """
    if not intervals:
        return []
    
    # Step 1: Sort by start time (this is the key insight!)
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:  # Overlapping
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    
    return merged


def three_sum(nums):
    """
    Leetcode #15 - 3Sum
    Find all unique triplets that sum to 0
    """
    nums.sort()  # Sorting enables the two-pointer technique!
    result = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:  # Skip duplicates
            continue
            
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return result


def group_anagrams(strs):
    """
    Leetcode #49 - Group Anagrams
    Group strings that are anagrams of each other
    """
    from collections import defaultdict
    groups = defaultdict(list)
    
    for s in strs:
        # Sort the characters to create a key
        key = ''.join(sorted(s))
        groups[key].append(s)
    
    return list(groups.values())


def top_k_frequent(nums, k):
    """
    Leetcode #347 - Top K Frequent Elements
    Find the k most frequent elements
    """
    from collections import Counter
    count = Counter(nums)
    
    # Sort by frequency (descending) and take top k
    # In interview, you might discuss using a heap instead for O(n log k)
    return [num for num, _ in count.most_common(k)]


def meeting_rooms_ii(intervals):
    """
    Leetcode #253 - Meeting Rooms II
    Find minimum number of meeting rooms required
    """
    if not intervals:
        return 0
    
    # Sort start and end times separately
    starts = sorted(interval[0] for interval in intervals)
    ends = sorted(interval[1] for interval in intervals)
    
    rooms = 0
    end_ptr = 0
    
    for start in starts:
        if start < ends[end_ptr]:
            rooms += 1
        else:
            end_ptr += 1
    
    return rooms


# Example custom sorting problem
def custom_sort_problem():
    """
    Sort people by: age (ascending), then name (alphabetical)
    This tests understanding of custom comparators
    """
    people = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 30},
        {"name": "David", "age": 25}
    ]
    
    # Method 1: Using key with tuple
    people.sort(key=lambda p: (p["age"], p["name"]))
    
    # Method 2: Using multiple sorts (stable sort)
    people.sort(key=lambda p: p["name"])  # Secondary sort first
    people.sort(key=lambda p: p["age"])   # Primary sort last
    
    return people


# Testing the functions
if __name__ == "__main__":
    print("1. Merge Intervals:")
    print(f"   Input: [[1,3],[2,6],[8,10],[15,18]]")
    print(f"   Output: {merge_intervals([[1,3],[2,6],[8,10],[15,18]])}")
    
    print("\n2. Three Sum:")
    print(f"   Input: [-1,0,1,2,-1,-4]")
    print(f"   Output: {three_sum([-1,0,1,2,-1,-4])}")
    
    print("\n3. Group Anagrams:")
    print(f"   Input: ['eat','tea','tan','ate','nat','bat']")
    print(f"   Output: {group_anagrams(['eat','tea','tan','ate','nat','bat'])}")
    
    print("\n4. Top K Frequent:")
    print(f"   Input: nums=[1,1,1,2,2,3], k=2")
    print(f"   Output: {top_k_frequent([1,1,1,2,2,3], 2)}")
    
    print("\n5. Custom Sort:")
    print(f"   Output: {custom_sort_problem()}")
    
    print("\n" + "="*60)
    print("Key Takeaways:")
    print("- You use sort() or sorted(), not implement sorting")
    print("- Sorting often enables other techniques (two pointers, binary search)")
    print("- Custom comparators are important to know")
    print("- Understanding O(n log n) complexity is crucial") 