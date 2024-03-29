#!/usr/bin/python3
"""A module that defines a Square Class"""


class Square:
    """ A class that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        Returns the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the value of the square size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """
        Returns the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square
        """
        if (type(value) is not tuple or len(value) != 2 or
            not all(isinstance(x, int) for x in value) or
            not all(x >= 0 for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        """ Prints the square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print("" * self.__position[0], end="")
                print("#" * self.__size)
