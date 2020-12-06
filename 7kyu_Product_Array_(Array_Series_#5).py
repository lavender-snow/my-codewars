def product_array(numbers):
    p = 1
    for n in numbers:
        p *= n
        
    return [p/n for n in numbers]