def digits(num):
    s = str(num)
    l = []
    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            l.append(int(s[i])+int(s[j]))
    return l