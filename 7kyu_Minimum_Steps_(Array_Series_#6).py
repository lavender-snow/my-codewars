def minimum_steps(numbers, value):
    sum = 0
    for i,n in enumerate(sorted(numbers)):
        sum += n
        if value <= sum:
            return i
    return -1