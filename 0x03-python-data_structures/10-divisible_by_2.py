#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    decision = []
    for i in my_list:
        if i % 2 == 0:
            decision.append(True)
        else:
            decision.append(False)
    return decision
