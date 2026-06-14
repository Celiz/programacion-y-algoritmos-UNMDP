def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_iterativo(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


n = 10

print("Recursivo:")
for i in range(n + 1):
    print(fibonacci(i), end=" ")

print("\nIterativo:")
for i in range(n + 1):
    print(fibonacci_iterativo(i), end=" ")
