def fact(n):
    if n == 0:
        f = 1
    else:
        f = 1
        for i in range(1, n + 1):
            f *= i
            yield f


for el in fact(5):
    print(el)
