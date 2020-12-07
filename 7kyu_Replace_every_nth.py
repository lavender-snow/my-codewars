def replace_nth(text, n, old, new):
    count = 0
    l = list(text)
    for i,c in enumerate(l):
        if c == old:
            count+=1
            if count == n:
                l[i] = new
                count = 0
    return "".join(l)