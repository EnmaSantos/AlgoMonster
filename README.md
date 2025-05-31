# Python Sorting Algorithms and Applications

This repository contains a collection of Python scripts designed todemonstrate various sorting algorithms, their performance characteristics, and their applications in common coding problems. It serves as a resource for understanding how different sorting methods work, how they compare against each other, and how they can be leveraged to solve complex tasks.

The scripts cover:
*   Implementations of common sorting algorithms.
*   Performance benchmarking of these algorithms.
*   Comparisons of algorithms under specific data conditions.
*   Examples of sorting applied to interview-style problems.

## `sorting-algorithms.py`

This script provides implementations for a comprehensive set of sorting algorithms:

*   Bubble Sort
*   Selection Sort
*   Insertion Sort
*   Merge Sort
*   Quick Sort
*   Heap Sort
*   Counting Sort
*   Shell Sort
*   Tim Sort (Python's built-in `sorted()`)
*   Radix Sort
*   Bogo Sort (a highly inefficient, educational algorithm)

When executed, `sorting-algorithms.py` benchmarks these algorithms by running them on randomly generated datasets of various sizes. It then prints the execution time for each algorithm, allowing for a comparison of their performance.

**To run this script:**
```bash
python sorting-algorithms.py
```
The script will output the time taken by each algorithm to sort the test arrays and indicate if the sort was successful. Note that O(n²) algorithms are tested on smaller datasets, and Bogo Sort is tested on a very small dataset with a timeout due to its inefficiency.

## `algorithm-comparison.py`

This script focuses on a comparative analysis of Counting Sort, Tim Sort (Python's built-in `sorted()`), and Insertion Sort under specific data scenarios. The goal is to illustrate when one algorithm might be preferred over others based on the characteristics of the input data.

The script tests the following scenarios:
*   **Small integer range:** (e.g., 100,000 integers in the range 0-100) - Counting Sort typically excels here.
*   **Large integer range:** (e.g., 10,000 integers in the range 0-1,000,000) - Tim Sort often performs better as Counting Sort's space complexity becomes an issue.
*   **Floating-point numbers:** Counting Sort is not applicable; Tim Sort is used.
*   **Strings:** Counting Sort is not applicable; Tim Sort is used.
*   **Nearly sorted data:** Insertion Sort can be very efficient for nearly sorted arrays, often outperforming more complex algorithms in such cases. Tim Sort also handles this well due to its adaptive nature.

**To run this script:**
```bash
python algorithm-comparison.py
```
The output will show the execution times for the algorithms in each scenario and declare a "winner" based on speed.
```

## `interview-sorting-examples.py`

This script showcases how sorting is a fundamental technique for solving various common coding interview problems, often those found on platforms like LeetCode. Instead of implementing sorting algorithms from scratch, these examples use Python's built-in `sort()` method or `sorted()` function, emphasizing the application of sorting as a preparatory step.

Examples include:
*   **Merge Intervals (LeetCode #56):** Merging overlapping intervals after sorting them by their start times.
*   **3Sum (LeetCode #15):** Finding unique triplets that sum to zero, often solved efficiently using a two-pointer approach after sorting the array.
*   **Group Anagrams (LeetCode #49):** Grouping words that are anagrams of each other by sorting the characters within each word to create a common key.
*   **Top K Frequent Elements (LeetCode #347):** Finding the k most frequent elements, where sorting by frequency is one approach.
*   **Meeting Rooms II (LeetCode #253):** Determining the minimum number of meeting rooms required by sorting start and end times.
*   **Custom Sort Example:** Demonstrating how to sort objects based on multiple criteria (e.g., sorting people by age, then by name).

**To run this script:**
```bash
python interview-sorting-examples.py
```
Executing the script will run the example functions and print their outputs, illustrating the solutions to these problems.
```

## `bogo-sort.py`

This script contains a standalone implementation of Bogo Sort. Bogo Sort, also known as permutation sort or stupid sort, is a highly inefficient sorting algorithm based on generating permutations of the input array until a sorted one is found.

It is primarily included for educational and illustrative purposes to demonstrate an example of a "worst-case" algorithm. Due to its extremely poor performance (average-case complexity is O((n+1)!)), it is not practical for any real-world application.

**To run this script:**
```bash
python bogo-sort.py
```
The script will attempt to sort a small sample array and print the number of attempts required. Be aware that for arrays with more than a few elements, this script can take a very long time to complete (or effectively, never complete). The version in `sorting-algorithms.py` includes a timeout for this reason.
```

## `two-pointers.py`

This file contains a Python dictionary with sample user data and a print statement. It does not appear to be directly related to the sorting algorithms or algorithm comparison scripts but is included in the repository. The "3Sum" problem in `interview-sorting-examples.py` utilizes a two-pointer technique after an initial sort.

**To run this script:**
```bash
python two-pointers.py
```
This will print a value from the sample user data.
```

## How to Run Scripts

Each Python script in this repository can be run from the command line using the Python interpreter.

**General command:**
```bash
python <script_name>.py
```
For example, to run the main sorting algorithm benchmark:
```bash
python sorting-algorithms.py
```
Make sure you have Python 3 installed on your system. No external libraries are required for most scripts, beyond standard Python modules.
```

## Contributing

Contributions to this repository are welcome! If you have suggestions for improvements, new algorithms to add, or more examples of sorting applications, please feel free to:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes.
4.  Submit a pull request.

Please ensure that any new code is clear, well-commented, and tested where applicable.
```
