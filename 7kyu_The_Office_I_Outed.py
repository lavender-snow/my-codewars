def outed(meet, boss):
    score = sum([v*2 if k == boss else v for k,v in meet.items()])/len(meet)
    return "Get Out Now!" if score <= 5 else "Nice Work Champ!"