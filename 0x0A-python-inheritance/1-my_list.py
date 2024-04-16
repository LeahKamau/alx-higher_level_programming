#!/usr/bin/python3
"""
This module consists of class that inherits from another class
"""


class MyList(list):
    """class MyList inherits from list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)
        """

        sorted_list = sorted(self)
        print(sorted_list)
