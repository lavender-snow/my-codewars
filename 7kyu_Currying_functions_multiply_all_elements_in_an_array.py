def multiply_all(l):
    def f(m):
        return list(map(lambda x:x*m,l))
    return f