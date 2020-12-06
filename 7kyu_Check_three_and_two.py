def check_three_and_two(array):
    return sorted([array.count(c) for c in set(array)]) == [2,3]