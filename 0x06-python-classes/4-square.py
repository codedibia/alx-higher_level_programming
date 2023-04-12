#!/usr/bin/python3
""" A module that uses getter and setter in a class"""


class Square:
    """A Class that defines a square"""

    def __init__(self, size=0):
        """
        Initializes a square
        """
        self.size = size

    @property
    def size(self):
        """
        Returns the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Inputs new value of size when needed
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    def area(self):
        """
        Returns the area of the square
        """
        return (self.__size * self.__size)
