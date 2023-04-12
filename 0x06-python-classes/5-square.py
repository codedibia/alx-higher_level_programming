#!/usr/bin/python3
"""A module that defines a square and prints it out with the "#" character"""


class Square:
    """
    A class that Initializes a square
    """
    def __init__(self, size=0):
        """
        Initializes the square
        """
        self.size = size

    @property
    def size(self):
        """
        Returns the value of size as a private property
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the acceptable value of the private property : size
        """
        if type(value) is not int:
            raise TypeError("size muat be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Returns the area of the square
        """

        return (self.__size * self.__size)

    def my_print(self):
        """
        Prints the square with the character "#"
        """
        if self.__size != 0:
            for i in range(self.__size):
                print("#" * self.__size)
        else:
            print()
