
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
