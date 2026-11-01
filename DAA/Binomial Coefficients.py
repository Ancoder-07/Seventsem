
# Binomial Coefficients using Dynamic Programming

# Input number of rows
n = int(input("Enter number of rows: "))

# Create DP table
dp = [[0 for j in range(i + 1)] for i in range(n)]

# Generate binomial coefficients
for i in range(n):

    dp[i][0] = 1
    dp[i][i] = 1

    for j in range(1, i):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

# Display Pascal's Triangle
print("\nBinomial Coefficients:")

for i in range(n):
    print(dp[i])

"""
// Binomial Coefficients using Dynamic Programming

#include <iostream>
#include <vector>
using namespace std;

int main() {
    // Input number of rows
    int n;
    cout << "Enter number of rows: ";
    cin >> n;

    // Create DP table (row i has i+1 elements)
    vector<vector<unsigned long long>> dp;
    for (int i = 0; i < n; i++)
        dp.push_back(vector<unsigned long long>(i + 1, 0));

    // Generate binomial coefficients
    for (int i = 0; i < n; i++) {
        dp[i][0] = 1;
        dp[i][i] = 1;

        for (int j = 1; j < i; j++)
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
    }

    // Display Pascal's Triangle
    cout << "\nBinomial Coefficients:" << endl;

    for (int i = 0; i < n; i++) {
        cout << "[";
        for (int j = 0; j <= i; j++) {
            cout << dp[i][j];
            if (j < i) cout << ", ";
        }
        cout << "]" << endl;
    }

    return 0;
}
"""
