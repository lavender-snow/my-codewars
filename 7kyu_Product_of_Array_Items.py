def product(numbers):
    if numbers is None:
        return None
    
    if len(numbers) == 0:
        return None
    
    res = 1
    for num in numbers:
        res *= num
    
    return res