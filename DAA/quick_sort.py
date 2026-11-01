
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

"""
// Deterministic vs Randomized Quick Sort

#include <iostream>
#include <vector>
#include <random>
#include <chrono>
#include <utility>
using namespace std;

long long count1 = 0;   // comparisons in deterministic quick sort
long long count2 = 0;   // comparisons in randomized quick sort

mt19937 rng(random_device{}());

// Deterministic Quick Sort (pivot = last element)
vector<int> deterministic_quick_sort(const vector<int> &arr) {
    if (arr.size() <= 1)
        return arr;

    int pivot = arr.back();
    vector<int> left, right;

    for (size_t i = 0; i + 1 < arr.size(); i++) {
        count1++;

        if (arr[i] <= pivot)
            left.push_back(arr[i]);
        else
            right.push_back(arr[i]);
    }

    vector<int> result = deterministic_quick_sort(left);
    result.push_back(pivot);
    vector<int> r = deterministic_quick_sort(right);
    result.insert(result.end(), r.begin(), r.end());
    return result;
}

// Randomized Quick Sort (pivot = random element)
vector<int> randomized_quick_sort(const vector<int> &arr) {
    if (arr.size() <= 1)
        return arr;

    uniform_int_distribution<int> dist(0, (int)arr.size() - 1);
    int pivot_index = dist(rng);
    int pivot = arr[pivot_index];

    vector<int> arr_copy = arr;
    swap(arr_copy[pivot_index], arr_copy.back());

    vector<int> left, right;

    for (size_t i = 0; i + 1 < arr_copy.size(); i++) {
        count2++;

        if (arr_copy[i] <= pivot)
            left.push_back(arr_copy[i]);
        else
            right.push_back(arr_copy[i]);
    }

    vector<int> result = randomized_quick_sort(left);
    result.push_back(pivot);
    vector<int> r = randomized_quick_sort(right);
    result.insert(result.end(), r.begin(), r.end());
    return result;
}

void print_array(const vector<int> &a) {
    cout << "[";
    for (size_t i = 0; i < a.size(); i++) {
        cout << a[i];
        if (i + 1 < a.size()) cout << ", ";
    }
    cout << "]" << endl;
}

int main() {
    // Input
    int n;
    cout << "Enter number of elements: ";
    cin >> n;

    vector<int> arr;
    for (int i = 0; i < n; i++) {
        int num;
        cout << "Enter element: ";
        cin >> num;
        arr.push_back(num);
    }

    // Deterministic Quick Sort
    count1 = 0;
    auto start = chrono::high_resolution_clock::now();

    vector<int> result1 = deterministic_quick_sort(arr);

    double time1 = chrono::duration<double>(
        chrono::high_resolution_clock::now() - start).count();

    // Randomized Quick Sort
    count2 = 0;
    start = chrono::high_resolution_clock::now();

    vector<int> result2 = randomized_quick_sort(arr);

    double time2 = chrono::duration<double>(
        chrono::high_resolution_clock::now() - start).count();

    // Display results
    cout << "\nDeterministic Quick Sort:" << endl;
    cout << "Sorted Array: ";
    print_array(result1);
    cout << "Comparisons: " << count1 << endl;
    cout << "Execution Time: " << time1 << " seconds" << endl;

    cout << "\nRandomized Quick Sort:" << endl;
    cout << "Sorted Array: ";
    print_array(result2);
    cout << "Comparisons: " << count2 << endl;
    cout << "Execution Time: " << time2 << " seconds" << endl;

    return 0;
}
"""