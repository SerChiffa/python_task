def factorial(x):
    pr = 1
    for i in range(2, x + 1):
        pr = pr * i
    return pr


def sochet(n, k):
    return factorial(n)/(factorial(k) * factorial(n-k))


print(sochet(8, 4))
