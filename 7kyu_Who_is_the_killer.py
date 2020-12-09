def killer(suspect_info, dead):
    for suspect in suspect_info:
        if len(set(suspect_info[suspect]) & set(dead)) == len(dead):
            return suspect
    return None