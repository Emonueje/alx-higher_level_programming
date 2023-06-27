#!/usr/bin/python3
"""A module that contains classes and functions for the classes and objects\
        at alx"""


class Square:
    """A class that defines a square"""
    def __init__(self, size=0):
        """initialization of the object"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size) < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ returns the area of the square """
        return self.__size ** 2
