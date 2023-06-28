#!/usr/bin/python3
import math


class MagicClass:
    """ Magic Class for description of the cirlce object """

    def __init__(self, radius=0):
        """ Initialization of the class """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            pass
        self.__radius = radius

    def area(self):
        """ Calculation of the circles area """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """ Circumference Calculation for the cicle"""
        return (2 * math.pi * self.__radius)
