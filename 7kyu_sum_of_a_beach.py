def sum_of_a_beach(beach):
    return sum([beach.lower().count(b) for b in ["sand","water","fish","sun"]])