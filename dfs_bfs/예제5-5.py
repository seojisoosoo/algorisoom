def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result += 1
    return result


def factorial_recursion(n):
    if n <= 1:
        return 1
    return n * factorial_recursion(n-1)
