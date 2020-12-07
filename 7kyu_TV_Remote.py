def search(c):
    keyboard = [["a","b","c","d","e","1","2","3"],
                ["f","g","h","i","j","4","5","6"],
                ["k","l","m","n","o","7","8","9"],
                ["p","q","r","s","t",".","@","0"],
                ["u","v","w","x","y","z","_","/"]]
    for i,row in enumerate(keyboard):
        for j,key in enumerate(row):
            if c == key:
                 return [i,j]
    return [-1,-1]

def tv_remote(word):
    now = [0,0]
    count = 0
    for c in word:
        next = search(c)
        count += abs(now[0] - next[0]) + abs(now[1] - next[1]) + 1
        now = next

    return count
