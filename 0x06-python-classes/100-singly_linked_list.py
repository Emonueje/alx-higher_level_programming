#!/usr/bin/python3

class Node:
    """ A class that defines the node of a singly linked list """
    def __init__(self, data, next_node=None):
        """ construct that shows the data and next_node """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ getter property of the data"""
        return (self.__data)

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
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    """ A class that describes a singly linked list """
    def __init__(self):
        """ a function that initializes """
        self.__head = None

    def sorted_insert(self, value):
        """ adds a new value to the node """
        new_node = Node(value)
        if not self.__head or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp_node = self.__head
            tmp_node = temp_node.next_node
            while (temp_node and tmp_node and (tmp_node.data < value)):
                temp_node = temp_node.next_node
                tmp_node = temp_node.next_node

            new_node.next_node = tmp_node
            temp_node.next_node = new_node

    def __str__(self):
        """prints singly linked list"""
        temp = self.__head
        all_str = ""
        while (temp):
            all_str += str(temp.data)
            temp = temp.next_node
            if (temp):
                all_str += "\n"
        return (all_str)
