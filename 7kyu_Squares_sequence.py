def squares(x, n):
    if n <= 0: return []
    res = [x]
    for i in range(n-1):
        res.append(res[i]**2)
    return res