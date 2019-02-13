def factorial(n):
    """calculating factorial of n recursively"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


def fibonacci(n):
    """Calculating fibonaccii  """
    if n <= 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#print(factorial(5))


for i in range(2, 36):
    print(i, fibonacci(i))
