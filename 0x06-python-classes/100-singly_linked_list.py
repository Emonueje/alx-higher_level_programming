#!/usr/bin/python3

class Node:
    """ A class that defines the node of a singly linked list """
    def __init__(self, data, next_node=None):
        """ construct that shows the data and next_node """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ getter property of the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """ setter property for the data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """ getter property for the next node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ setter property for the next node """
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList:
    """ A class that describes a singly linked list """
    def __init__(self):
        """ a function that initializes """
        self.__head = None

    def sorted_insert(self, value):
        """ adds a new value to the node """
        head = self.__head
        new_node = Node(value, head)
        self.__head = new_node
