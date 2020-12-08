def is_nice(arr):
    if len(arr) == 0: return False
    for n in arr:
        if not(n+1 in arr or n-1 in arr):
            return False
    return True