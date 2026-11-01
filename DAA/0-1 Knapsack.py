
# 0-1 Knapsack using Dynamic Programming

# Input number of items
n = int(input("Enter number of items: "))

weights = []
values = []

for i in range(n):
    w = int(input("Enter weight of item: "))
    v = int(input("Enter value of item: "))

    weights.append(w)
    values.append(v)

# Input knapsack capacity
capacity = int(input("Enter knapsack capacity: "))

# Create DP table
dp = [[0 for j in range(capacity + 1)] for i in range(n + 1)]

# Dynamic Programming
for i in range(1, n + 1):
    for w in range(capacity + 1):

        if weights[i - 1] <= w:
            dp[i][w] = max(
                values[i - 1] + dp[i - 1][w - weights[i - 1]],
                dp[i - 1][w]
            )
        else:
            dp[i][w] = dp[i - 1][w]

# Display maximum value
print("\nMaximum value in Knapsack:", dp[n][capacity])

# Display selected items
print("Selected Items:")

w = capacity
for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        print("Item", i)
        w -= weights[i - 1]

"""
// 0-1 Knapsack using Dynamic Programming

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    // Input number of items
    int n;
    cout << "Enter number of items: ";
    cin >> n;

    vector<int> weights(n), values(n);

    for (int i = 0; i < n; i++) {
        cout << "Enter weight of item: ";
        cin >> weights[i];
        cout << "Enter value of item: ";
        cin >> values[i];
    }

    // Input knapsack capacity
    int capacity;
    cout << "Enter knapsack capacity: ";
    cin >> capacity;

    // Create DP table (n+1 rows, capacity+1 columns), filled with 0
    vector<vector<int>> dp(n + 1, vector<int>(capacity + 1, 0));

    // Dynamic Programming
    for (int i = 1; i <= n; i++) {
        for (int w = 0; w <= capacity; w++) {
            if (weights[i - 1] <= w) {
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                );
            } else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    // Display maximum value
    cout << "\nMaximum value in Knapsack: " << dp[n][capacity] << endl;

    // Display selected items
    cout << "Selected Items:" << endl;

    int w = capacity;
    for (int i = n; i > 0; i--) {
        if (dp[i][w] != dp[i - 1][w]) {
            cout << "Item " << i << endl;
            w -= weights[i - 1];
        }
    }

    return 0;
}
"""