def last(*args):    
    if len(args) == 1:
        if type(args[0]) == int:
            return args[0]
        else:
            return args[0][-1]  
    return args[-1]