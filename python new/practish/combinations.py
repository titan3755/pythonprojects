def combinations(*items):
    group = 1
    for thing in items:
        if thing == 0:
            pass
        else:
            group = group * thing
    possible_combinations = group
    return possible_combinations



