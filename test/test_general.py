# encoding: utf-8

# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.
from src.code import check_sudoku
correcto = [[1, 2, 3],
            [2, 3, 1],
            [3, 1, 2]]

incorrecto1 = [[1, 2, 3, 4],
               [2, 3, 1, 3],
               [3, 1, 2, 3],
               [4, 4, 4, 4]]

incorrecto2 = [[1, 2, 3, 4],
               [2, 3, 1, 4],
               [4, 1, 2, 3],
               [3, 4, 1, 2]]

incorrecto3 = [[1, 2, 3, 4, 5],
               [2, 3, 1, 5, 6],
               [4, 5, 2, 1, 3],
               [3, 4, 5, 2, 1],
               [5, 6, 4, 3, 2]]

incorrecto4 = [['a', 'b', 'c'],
               ['b', 'c', 'a'],
               ['c', 'a', 'b']]

incorrecto5 = [[1, 1.5],
               [1.5, 1]]

incorrecto6 = [[1, 0, 0, 0],
               [0, 1, 0],
               [0, 0, 0, 1]]


# Casos test
def test_repeats_much():
    assert(check_sudoku(incorrecto1)) == False
    # >>> False

def test_correct_simple():
    assert(check_sudoku(correcto)) == True
    # >>> True

def test_bad_position():
    assert(check_sudoku(incorrecto2)) == False
    # >>> False

def test_number_out_of_index():
    assert(check_sudoku(incorrecto3)) == False
    # >>> False

def test_not_integer_string():
    assert(check_sudoku(incorrecto4)) == False
    # >>> False

def test_not_integer_float():
    assert(check_sudoku(incorrecto5)) == False
    # >>> False

def test_no_n_x_n():
    assert(check_sudoku(incorrecto6)) == False
    # >>> False