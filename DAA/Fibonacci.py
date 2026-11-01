
# Fibonacci using Recursive and Non-Recursive Methods

# Recursive Fibonacci
def fibonacci_recursive(n):
    global recursive_steps
    recursive_steps += 1

    if n <= 1:
        return n

    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


# Non-Recursive Fibonacci
def fibonacci_nonrecursive(n):
    global iterative_steps

    a, b = 0, 1
    result = []

    for i in range(n):
        iterative_steps += 1
        result.append(a)
        a, b = b, a + b

    return result


# Input
n = int(input("Enter number of terms: "))

if n < 0:
    print("Please enter a non-negative number.")

else:
    recursive_steps = 0
    iterative_steps = 0

    # Non-Recursive
    result1 = fibonacci_nonrecursive(n)

    # Recursive
    result2 = [fibonacci_recursive(i) for i in range(n)]

    # Display results
    print("\nNon-Recursive Fibonacci:")
    print(result1)
    print("Step Count:", iterative_steps)

    print("\nRecursive Fibonacci:")
    print(result2)
    print("Step Count:", recursive_steps)

    """
    // Fibonacci using Recursive and Non-Recursive Methods

#include <iostream>
using namespace std;

const int MAX = 100;

int recursiveSteps = 0;
int iterativeSteps = 0;

long long result1[MAX];   // stores non-recursive result
long long result2[MAX];   // stores recursive result

// Recursive Fibonacci
long long fibonacciRecursive(int n) {
    recursiveSteps++;

    if (n <= 1)
        return n;

    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}

// Non-Recursive Fibonacci
void fibonacciNonRecursive(int n) {
    long long a = 0, b = 1;

    for (int i = 0; i < n; i++) {
        iterativeSteps++;
        result1[i] = a;

        long long next = a + b;
        a = b;
        b = next;
    }
}

// Print an array in Python list style: [0, 1, 1, 2]
void printArray(long long arr[], int n) {
    cout << "[";
    for (int i = 0; i < n; i++) {
        cout << arr[i];
        if (i < n - 1)
            cout << ", ";
    }
    cout << "]" << endl;
}

int main() {

    int n;
    cout << "Enter number of terms: ";
    cin >> n;

    if (n < 0) {
        cout << "Please enter a non-negative number." << endl;
    }
    else {
        // Non-Recursive
        fibonacciNonRecursive(n);

        // Recursive
        for (int i = 0; i < n; i++) {
            result2[i] = fibonacciRecursive(i);
        }

        // Display results
        cout << "\nNon-Recursive Fibonacci:" << endl;
        printArray(result1, n);
        cout << "Step Count: " << iterativeSteps << endl;

        cout << "\nRecursive Fibonacci:" << endl;
        printArray(result2, n);
        cout << "Step Count: " << recursiveSteps << endl;
    }

    return 0;
}
"""