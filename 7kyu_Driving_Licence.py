def driver(data):
    months = {"Jan":1,
              "Feb":2,
              "Mar":3,
              "Apr":4,
              "May":5,
              "Jun":6,
              "Jul":7,
              "Aug":8,
              "Sep":9,
              "Oct":10,
              "Nov":11,
              "Dec":12}
    res = data[2][0:min(5,len(data[2]))].upper() + "9"*max(0,5-len(data[2]))
    res += data[3][-2]
    
    if data[4] == "F":
        res += str(50+months[data[3][3:6]])
    else:
        res += str(months[data[3][3:6]]).zfill(2)
    res += data[3][0:2]
    
    res += data[3][-1]
    
    res += data[0][0]
    
    if data[1] == "":
        res += "9"
    else:
        res += data[1][0]
    
    res += "9"
    
    res += "AA"
    
    return res