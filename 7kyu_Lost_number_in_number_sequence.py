def find_deleted_number(arr, mixed_arr):
    l = list(set(arr)-set(mixed_arr))
    return l[0] if len(l) > 0 else 0