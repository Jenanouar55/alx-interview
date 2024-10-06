#!/usr/bin/python3
"""
0. Pascal's Triangle
This module defines the function pascal_triangle generates Pascal triangle.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to n rows.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list of lists: A list of lists where each inner list represents a row
        of Pascal's triangle.
    """
    res = []  # Initialize the result list to store levels of Pascal Triangle

    if n > 0:
        # Loop through the number of rows
        for i in range(1, n + 1):
            level = []  # Initialize a new row (level)
            C = 1  # The first value of every row is always 1

            # Populate each row with the correct values
            for j in range(1, i + 1):
                level.append(C)  # Append the current value of C
                C = C * (i - j) // j

            res.append(level)  # Add the completed row to the result list

    return res  # Return the full Pascal's Triangle as a list of lists
