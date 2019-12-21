"""
2D countably infinite search.

0,0 | 0,1 | 0,2 | 0,3 | 0,4 | 0,5 |
1,0 | 1,1 | 1,2 | 1,3 | 1,4 | 1,5 |
2,0 | 2,1 | 2,2 | 2,3 | 2,4 | 2,5 |
3,0 | 3,1 | 3,2 | 3,3 | 3,4 | 3,5 |
4,0 | 4,1 | 4,2 | 4,3 | 4,4 | 4,5 |
5,0 | 5,1 | 5,2 | 5,3 | 5,4 | 5,5 |

Order of search:
0,0 ->
0,1 -> 1,0 ->
0,2 -> 1,1 -> 2,0 ->
0,3 -> 1,2 -> 2,1 -> 3,0
0,4 -> 1,3 -> 2,2 -> 3,1 -> 4,0
0,5 -> 1,4 -> 2,3 -> 3,2 -> 4,1 -> 5,0

Diagonal number sequence:
Tn = n * (n + 1) / 2
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, ...
"""
import math


def _get_diagonal_index(n):
    """
    Get the diagonal series index of the closest lower diagonal number.

    Using the equation for triangular numbers:
    https://en.wikipedia.org/wiki/Triangular_number

    Tn = n * (n + 1) / 2
    ax^2 + bx + c = 0
    1/2n^2 + 1/2n - Tn = 0
    x = (-b +- sqrt(b^2 - 4ac)) / 2a
    n = sqrt(1/4 + 2Tn) +- 1/2
    """
    return int(math.sqrt(.25 + 2 * n) + .5) - 1


def _get_diagonal_number(index):
    """
    Get the diagonal number for a given index into the sequence.

    Using the equation for triangular numbers:
    https://en.wikipedia.org/wiki/Triangular_number

    Tn = n * (n + 1) / 2
    """
    return index * (index + 1) // 2


def get_countable_indexes(iteration):
    """Search through two countably infinite sequences diagonally."""
    diagonal_index = _get_diagonal_index(iteration)
    diagonal_number = _get_diagonal_number(diagonal_index)

    v_1 = iteration - diagonal_number
    v_2 = diagonal_index - v_1

    return v_1, v_2
