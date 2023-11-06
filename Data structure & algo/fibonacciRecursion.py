
def fibRecursion(n):
    if n <= 1:
        return 1
    return (fibRecursion(n-1) + fibRecursion(n-2))


for i in range(10):
    print(fibRecursion(i))