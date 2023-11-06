
def factRecursion(n):
    if n == 1:
        return 1
    return  n * factRecursion(n - 1)


print(factRecursion(5))