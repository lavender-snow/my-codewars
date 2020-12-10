def numbers_with_digit_inside(x, d):
    l = [0,0,1]
    for i in range(1,x+1):
        if str(d) in str(i):
            l[0] += 1
            l[1] += i
            l[2] *= i
    if l[0] == 0:
        return [0,0,0]
    else:
        return l