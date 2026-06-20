def f(n):
    if n == 0:
        return
    f(n - 1)
    print(n)

f(5)