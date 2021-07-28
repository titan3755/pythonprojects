def majority_vote(lst):
    for x in lst:
        main_count = int(lst.count(x))
        if main_count > float(len(lst) / 2):
            return x
        elif main_count < float(len(lst) / 2):
            pass


print(majority_vote(["A", "B", "B"]))
