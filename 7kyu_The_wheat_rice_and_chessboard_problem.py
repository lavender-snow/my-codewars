def squares_needed(grains):
    n = 0
    while grains >= 2**n:
        n+=1
    return n