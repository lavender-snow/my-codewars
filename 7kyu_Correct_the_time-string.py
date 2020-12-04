import re

def time_correct(t):
    if t is None:
        return None
    
    if t == '':
        return ''
    
    m = re.fullmatch('^([0-9]{2}):([0-9]{2}):([0-9]{2})$',t)
    if m is not None:
        second = (int(m[1])*60*60 + int(m[2])*60 + int(m[3])) % 86400
        
        hour,second = divmod(second,3600)
        minute,second = divmod(second,60)
        return f"{str(hour).zfill(2)}:{str(minute).zfill(2)}:{str(second).zfill(2)}"
    
    return None