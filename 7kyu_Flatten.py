def flatten(lst):
    res = []
    for l in lst:
        if type(l) == list:
            for x in l:
                res.append(x)
        else:
            res.append(l)
    return res
