#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_cp=matrix[:]
    for i in range(len(matrix)):
        matrix_cp[i]=list(map(lambda x : x*x,matrix[i]))
    return matrix_cp
