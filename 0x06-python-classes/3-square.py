#!/usr/bin/python3
""" A Module containing a class that defines a square"""


class Square:
    """ A class that defines a square."""

    def __init__(self, size=0):
        """ Initializes a new square
        Args:
        size(int) size of the new square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
            """
            Calculates and returns the area of the square.
            Args:
            size(int) size of the square
            """
            return (self.__size * self.__size)
