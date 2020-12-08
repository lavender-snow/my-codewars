def reverse(a):
    res = []
    rev = "".join(a)[::-1]
    idx = 0
    for word in a:
        l = len(word)
        res.append(rev[idx:idx+l])
        idx += l
    return res