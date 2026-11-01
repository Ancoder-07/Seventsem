
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