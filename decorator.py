def outer(func):
    d = {}
    def inner(x):
        if x in d:
            return d[x]
        result = func(x)
        d[x] = result
        return result

    return inner


@outer
def rechnen(x):
    return x * x


print(rechnen(5))
print(rechnen(5))
print(rechnen(7))
