#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    return sum(ae * bc for ae, bc in my_list) / sum(bc for ae, bc in my_list)
