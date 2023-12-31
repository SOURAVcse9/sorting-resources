import time
import memory_profiler
import sys
# Set a higher recursion limit
sys.setrecursionlimit(10**6)

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    iterations = 0
 # Outer loop for each element
    for i in range(n):
  # Inner loop for comparisons and swaps
        for j in range(0, n-i-1):
            iterations += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return iterations

# Insertion Sort
def insertion_sort(arr):
    iterations = 0
# Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        iterations += 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            iterations += 1
        arr[j + 1] = key

    return iterations

# Heap Sort
def heapify(arr, n, i, iterations):
 # Heapify a subtree rooted at index i
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left
    iterations += 1

    if right < n and arr[largest] < arr[right]:
        largest = right
    iterations += 1

    if largest != i:
     # Swap and heapify the affected sub-tree
        arr[i], arr[largest] = arr[largest], arr[i]
        iterations += 1
        heapify(arr, n, largest, iterations)

def heap_sort(arr):
    n = len(arr)
    iterations = 0

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, iterations)
 
 # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        iterations += 1
        heapify(arr, i, 0, iterations)

    return iterations

# Counting Sort
def counting_sort(arr):
    iterations = 0
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    output = [0] * len(arr)

  # Count occurrences of each element
    for i in range(len(arr)):
        count[arr[i] - min_val] += 1
        iterations += 1

# Modify count array to store the position of elements
    for i in range(1, len(count)):
        count[i] += count[i - 1]
        iterations += 1

# Build the output array
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
        iterations += 1

 # Copy the output array back to the original array
    for i in range(len(arr)):
        arr[i] = output[i]
        iterations += 1

    return iterations
# Quick Sort
def quick_sort_helper(arr, low, high, iterations):
    # Recursive helper function for Quick Sort
    if low < high:
        pi, iterations = partition(arr, low, high, iterations)

        # Update iterations for left and right partitions
        iterations = quick_sort_helper(arr, low, pi - 1, iterations)
        iterations = quick_sort_helper(arr, pi + 1, high, iterations)

    return iterations

def partition(arr, low, high, iterations):
    # Choose the rightmost element as pivot
    pivot = arr[high]
    i = low - 1

    # Iterate through the array to rearrange elements around the pivot
    for j in range(low, high):
        iterations += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    iterations += 1

    return i + 1, iterations

def quick_sort(arr):
    n = len(arr)
    iterations = 0
    iterations = quick_sort_helper(arr, 0, n - 1, iterations)
    return iterations



# Merge Sort
def merge(arr, left, mid, right, iterations):
     # Merge two sub-arrays of arr[]
    n1 = mid - left + 1
    n2 = right - mid

    left_arr = arr[left:left + n1]
    right_arr = arr[mid + 1:mid + 1 + n2]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        iterations += 1
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right_arr[j]
        j += 1
        k += 1

    return iterations  # Fix: Return the total number of iterations

def merge_sort_helper(arr, left, right, iterations):
     # Recursive helper function for Merge Sort
    if left < right:
        mid = (left + right) // 2

        # Fix: Return the total number of iterations
        iterations = merge_sort_helper(arr, left, mid, iterations)
        iterations = merge_sort_helper(arr, mid + 1, right, iterations)

        # Fix: Return the total number of iterations
        iterations = merge(arr, left, mid, right, iterations)

    return iterations  # Fix: Return the total number of iterations

def merge_sort(arr):
    n = len(arr)
    iterations = 0
    iterations = merge_sort_helper(arr, 0, n - 1, iterations)
    return iterations




# Read data from file
def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = [int(line.strip()) for line in file]
    return data

# Write data to file
def write_data_to_file(file_path, data):
    with open(file_path, 'w') as file:
        file.writelines("{}\n".format(item) for item in data)

if __name__ == "__main__":
    # Replace 'random_data.txt' with the actual file path
    input_file_path = 'sorted_data.txt'
    while True:
        print("Choose a sorting algorithm:")
        print("1. Bubble Sort")
        print("2. Insertion Sort")
        print("3. Heap Sort")
        print("4. Counting Sort")
        print("5. Quick Sort")
        print("6. Merge Sort")
        print("0. Exit")

        choice = int(input("Enter the number of your choice: "))
        if choice == 0:
            break
        elif choice == 1:
            # Bubble Sort
            data_bubble = read_data_from_file(input_file_path)
            start_time = time.time()
            iterations_bubble = bubble_sort(data_bubble.copy())
            end_time = time.time()
            execution_time_bubble = end_time - start_time
            output_file_path_bubble = 'sorted_data_bubble.txt'
            write_data_to_file(output_file_path_bubble, data_bubble)
            mem_usage_bubble = memory_profiler.memory_usage()[0]
            # Print bubblesort results
            print("Bubble Sort - Execution Time: {:.6f} seconds".format(execution_time_bubble))
            print("Bubble Sort - Number of Iterations: {}".format(iterations_bubble))
            print("Bubble Sort - Memory Usage: {:.2f} MB".format(mem_usage_bubble))
        elif choice == 2:
            # Insertion Sort
            data_insertion = read_data_from_file(input_file_path)
            start_time = time.time()
            iterations_insertion = insertion_sort(data_insertion.copy())
            end_time = time.time()
            execution_time_insertion = end_time - start_time
            output_file_path_insertion = 'sorted_data_insertion.txt'
            write_data_to_file(output_file_path_insertion, data_insertion)
            mem_usage_insertion = memory_profiler.memory_usage()[0]
            # Print insertionsort results
            print("\nInsertion Sort - Execution Time: {:.6f} seconds".format(execution_time_insertion))
            print("Insertion Sort - Number of Iterations: {}".format(iterations_insertion))
            print("Insertion Sort - Memory Usage: {:.2f} MB".format(mem_usage_insertion))
        elif choice == 3:
            # Heap Sort
            data_heap = read_data_from_file(input_file_path)
            start_time = time.time()
            iterations_heap = heap_sort(data_heap.copy())
            end_time = time.time()
            execution_time_heap = end_time - start_time
            output_file_path_heap = 'sorted_data_heap.txt'
            write_data_to_file(output_file_path_heap, data_heap)
            mem_usage_heap = memory_profiler.memory_usage()[0]
            # Print heapsort results 
            print("\nHeap Sort - Execution Time: {:.6f} seconds".format(execution_time_heap))
            print("Heap Sort - Number of Iterations: {}".format(iterations_heap))
            print("Heap Sort - Memory Usage: {:.2f} MB".format(mem_usage_heap))
        elif choice == 4:
            # Counting Sort
            data_counting = read_data_from_file(input_file_path)
            start_time = time.time()
            iterations_counting = counting_sort(data_counting.copy())
            end_time = time.time()
            execution_time_counting = end_time - start_time
            output_file_path_counting = 'sorted_data_counting.txt'
            write_data_to_file(output_file_path_counting, data_counting)
            mem_usage_counting = memory_profiler.memory_usage()[0]
            # Print countingsort results
            print("\nCounting Sort - Execution Time: {:.6f} seconds".format(execution_time_counting))
            print("Counting Sort - Number of Iterations: {}".format(iterations_counting))
            print("Counting Sort - Memory Usage: {:.2f} MB".format(mem_usage_counting))
        elif choice == 5:
            # Quick Sort
            data_quick = read_data_from_file(input_file_path)
            start_time = time.time()
            iterations_quick = quick_sort(data_quick.copy())
            end_time = time.time()
            execution_time_quick = end_time - start_time
            output_file_path_quick = 'sorted_data_quick.txt'
            write_data_to_file(output_file_path_quick, data_quick)
            mem_usage_quick = memory_profiler.memory_usage()[0]
            # Print Quick Sort results
            print("\nQuick Sort - Execution Time: {:.6f} seconds".format(execution_time_quick))
            print("Quick Sort - Number of Iterations: {}".format(iterations_quick))
            print("Quick Sort - Memory Usage: {:.2f} MB".format(mem_usage_quick))
        elif choice == 6:
            # Merge Sort
            data_merge = read_data_from_file(input_file_path)
            start_time = time.time()
            iterations_merge = merge_sort(data_merge.copy())
            end_time = time.time()
            execution_time_merge = end_time - start_time
            output_file_path_merge = 'sorted_data_merge.txt'
            write_data_to_file(output_file_path_merge, data_merge)
            mem_usage_merge = memory_profiler.memory_usage()[0]
            # Print Merge Sort results
            print("\nMerge Sort - Execution Time: {:.6f} seconds".format(execution_time_merge))
            print("Merge Sort - Number of Iterations: {}".format(iterations_merge))
            print("Merge Sort - Memory Usage: {:.2f} MB".format(mem_usage_merge))

        
       
    
