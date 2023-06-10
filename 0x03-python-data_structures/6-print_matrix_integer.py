#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for j in row:
            print("{}".format(j), end=" ")
        print()
