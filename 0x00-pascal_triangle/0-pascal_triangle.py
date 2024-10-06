#!/usr/bin/python3
def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    """
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    for i in range(1, n):
        # Start each row with a '1'
        row = [1]

        # Add the values from the previous row to form the new row
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])

        # End each row with a '1'
        row.append(1)
        triangle.append(row)

    return triangle
