def find_smallest(numbers,to_return):
    min_num = min(numbers)
    return min_num if to_return == "value" else numbers.index(min_num)