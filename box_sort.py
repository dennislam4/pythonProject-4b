# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 10-13-2022
# Description: Program that contains a box class where init method takes a private length, wideth and height as
# parameters. Inside has volume method that returns volume of box. Has get methods for length, width and height.
# Contains seperate function named box_sort that users inserertion sort to sort a list of boxes from greatest to least
# in volume.

class Box:
    """Class that represents a box"""

    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    def get_length(self):
        """Get method for length of box"""
        return self._length

    def get_width(self):
        """Get method for width of box"""
        return self._width

    def get_height(self):
        """Get method for height of box"""
        return self._height

    def volume(self):
        """Returns the volume of the box"""
        return self._length * self._width * self._height


def box_sort(box_list):
    """Uses insertion algotrithm to sort list of boxes from greatest to lowest volume"""
    for box_index in range(1, len(box_list)):
        box_value = box_list[box_index]
        while box_volume >= 0 and box_list[box_index].volume() < box_value.volume():
            if box_value < box_list[box_volume]:
                box_list[box_volume + 1] = box_list[box_volume]
                box_list[box_volume] = box_value
                box_volume = box_volume - 1

