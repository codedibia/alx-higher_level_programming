#!/usr/bin/python3
""" A Module containing a class that defines a square"""


class Square:
    """
    A class that defines a square.
    """

    def __init__(self, size=0):
        """ Initializes a new square
        Args:
        size(int) sizr of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("Size must be >= 0")
        else:
            self.__size = size
