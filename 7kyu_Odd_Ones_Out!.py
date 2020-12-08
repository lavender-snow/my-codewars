def odd_ones_out(numbers):
    return [num for num in numbers if numbers.count(num) % 2 == 0]