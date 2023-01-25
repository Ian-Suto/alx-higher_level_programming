#!/usr/bin/python3
"""Module generate's a Pascal triangle"""


def pascal_triangle(n):
    """Return's a list of lists of int rep the Pascal triangle of n."""
    if n <= 0:
        return []
    result = [[1]]

    for i in range(n - 1):
        tmp = [0] + result[-1] + [0]
        row = []
        for j in range(len(result[-1]) + 1):
            row.append(tmp[j] + tmp[j + 1])
        result.append(row)
    return result
