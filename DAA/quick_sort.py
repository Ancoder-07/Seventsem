
import random
import time

# Deterministic Quick Sort
def deterministic_quick_sort(arr):
    global count1

    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    left = []
    right = []

    for i in range(len(arr) - 1):
        count1 += 1

        if arr[i] <= pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return deterministic_quick_sort(left) + [pivot] + deterministic_quick_sort(right)


# Randomized Quick Sort
def randomized_quick_sort(arr):
    global count2

    if len(arr) <= 1:
        return arr

    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    arr_copy = arr.copy()
    arr_copy[pivot_index], arr_copy[-1] = arr_copy[-1], arr_copy[pivot_index]

    left = []
    right = []

    for i in range(len(arr_copy) - 1):
        count2 += 1

        if arr_copy[i] <= pivot:
            left.append(arr_copy[i])
        else:
            right.append(arr_copy[i])

    return randomized_quick_sort(left) + [pivot] + randomized_quick_sort(right)


# Input
n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

# Deterministic Quick Sort
count1 = 0
start = time.perf_counter()

result1 = deterministic_quick_sort(arr.copy())

time1 = time.perf_counter() - start

# Randomized Quick Sort
count2 = 0
start = time.perf_counter()

result2 = randomized_quick_sort(arr.copy())

time2 = time.perf_counter() - start

# Display results
print("\nDeterministic Quick Sort:")
print("Sorted Array:", result1)
print("Comparisons:", count1)
print("Execution Time:", time1, "seconds")

print("\nRandomized Quick Sort:")
print("Sorted Array:", result2)
print("Comparisons:", count2)
print("Execution Time:", time2, "seconds")
