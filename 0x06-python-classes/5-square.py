#!/usr/bin/python3
"""A module that contains classes and functions for the classes and objects\
        at alx"""


class Square:
    """A class that defines a square"""
    def __init__(self, size=0):
        """ initializes the object square """
        self.__size = size

    def area(self):
        """ returns the area of the square """
        return self.__size ** 2

    @property
    def size(self):
        """ returns the size of the squre """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ sets the value of the size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ prints to stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for k in range(self.__size):
                    print("#", end="")
                print()
