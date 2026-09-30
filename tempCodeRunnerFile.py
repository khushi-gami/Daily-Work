def test(n):
    if n == 1:
        return 1
    return n + test(n - 1)
print(test(4))