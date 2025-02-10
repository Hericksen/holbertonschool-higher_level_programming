#!/usr/bin/python3
'''Pascal's Triangle'''
def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle up to level n."""
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]  # First element is always 1

        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)  # Last element is always 1
        triangle.append(new_row)

    return triangle
