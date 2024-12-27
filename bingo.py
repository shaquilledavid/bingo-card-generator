import numpy as np


def generateBingoCard():
    """
    Create a 5x5 grid meant for 75-ball Bingo
    
    b i n g o
    i       |
    n   x   |
    g       |
    o -------
    """

    matrix = np.zeros((5,5), dtype='U100')

    #format the matrix
    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix):
            matrix[i][j] = '    '
            j += 1
        i += 1

    matrix[2][2] = 'FREE'
    return matrix

matrix = generateBingoCard()


