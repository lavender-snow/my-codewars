def least_larger(a, i): 
    if max(a) == a[i]:
        return -1
    return a.index(min([n for n in a if n > a[i]]))