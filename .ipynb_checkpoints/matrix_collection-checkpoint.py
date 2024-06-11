#!/usr/bin/env python

'''
input:
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]
          

'''



def matrix_shape(matrix):
    a,b = np.array(matrix).shape
    print(f'shape of Matrix is {np.array(matrix).shape}')
    return a,b

def del_row_i(matrix,i):
    del matrix[i]
    return matrix

def create_matrix_from_dict():
    lst = input().split()
    dct = {lst[i]:lst[i+1] for i in range(0,len(lst),2)}
    matrix = [list(dct.keys()),list(dct.values())]
    return matrix