#!/usr/bin/python3
"""A module that contains classes and functions for the classes and objects\
        at alx"""


class Square:
    """A class that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """ initializes the object square """
        self.__size = size
        self.__position = position

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
    @property
    def position(self):
        """ Private attribute position getter """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ Private position setter """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("Position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """ prints to stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for k in range(self.__size):
                print("{}{}".format(" " * self.__position[0], '#'*self.__size))
