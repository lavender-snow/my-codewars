def duplicate_sandwich(arr):
    idx = [i for i,x in enumerate(arr) if arr.count(x) == 2]
    return arr[idx[0]+1:idx[1]]