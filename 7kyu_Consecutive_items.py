def consecutive(arr, a, b):
    return True if abs(arr.index(a) - arr.index(b)) == 1 else False