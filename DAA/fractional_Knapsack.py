# Fractional Knapsack using Greedy Method

# Input number of items
n = int(input("Enter number of items: "))

items = []

for i in range(n):
    weight = int(input("Enter weight of item: "))

    if weight <= 0:
        print("Weight must be greater than zero.")
        exit()

    value = int(input("Enter value of item: "))

    ratio = value / weight
    items.append((weight, value, ratio))

# Input knapsack capacity
capacity = int(input("Enter knapsack capacity: "))

# Sort items by value/weight ratio
items.sort(key=lambda x: x[2], reverse=True)

total_value = 0

# Greedy selection
for weight, value, ratio in items:

    if capacity >= weight:
        total_value += value
        capacity -= weight

    else:
        total_value += ratio * capacity
        break

# Display result
print("\nMaximum value in Knapsack:", total_value)

"""
// Fractional Knapsack using Greedy Method

#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

struct Item {
    long long weight;
    long long value;
    double ratio;   // value / weight
};

int main() {
    // Input number of items
    int n;
    cout << "Enter number of items: ";
    cin >> n;

    vector<Item> items;

    for (int i = 0; i < n; i++) {
        long long weight, value;

        cout << "Enter weight of item: ";
        cin >> weight;

        if (weight <= 0) {
            cout << "Weight must be greater than zero." << endl;
            return 0;
        }

        cout << "Enter value of item: ";
        cin >> value;

        double ratio = (double)value / weight;
        items.push_back({weight, value, ratio});
    }

    // Input knapsack capacity
    long long capacity;
    cout << "Enter knapsack capacity: ";
    cin >> capacity;

    // Sort items by value/weight ratio (highest first)
    // stable_sort keeps the original order for equal ratios, like Python's sort
    stable_sort(items.begin(), items.end(),
                [](const Item &a, const Item &b) { return a.ratio > b.ratio; });

    double total_value = 0;

    // Greedy selection
    for (const Item &it : items) {
        if (capacity >= it.weight) {
            // take the whole item
            total_value += it.value;
            capacity -= it.weight;
        } else {
            // take a fraction of the item and stop
            total_value += it.ratio * capacity;
            break;
        }
    }

    // Display result
    cout << fixed << setprecision(2);
    cout << "\nMaximum value in Knapsack: " << total_value << endl;

    return 0;
}
"""