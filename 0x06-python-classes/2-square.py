#!/usr/bin/python3
"""A module that contains classes and functions for the classes and objects\
        at alx"""


class Square:
    """A class that defines a square"""
    def __init__(self, size=0):
        """initialization of the object"""
        self.__size = size
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        if (self.__size) < 0:
            raise ValueError("size must be >= 0")
