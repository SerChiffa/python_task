def factorial(n):
    if n == 1:
        return 1
    prevfac = factorial(n - 1)
    return n * prevfac


n = int(input())
print(factorial(n))
