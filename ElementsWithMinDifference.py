#!/usr/bin/env python
import numpy as np
# ---------------------------
'''
Given an array of arr, the function herein finds the differnce between each element. 
Looking for the minumum difference, the function will return pairs of elements with minimum difference.
e.g:
    Input:
        Array = [1,2,3,4,5]
    
    Output:
        1, 2
        2, 3
        3, 4
        4, 5
'''
# ---------------------------
def PairsWithMinimumDiff(arr):
    pairs = [(x,y) for xi, x in enumerate(arr) for y in arr[xi+1:]]
    lst = [abs(elem[1]-elem[0]) for elem in pairs]
    mlst = min(lst)
    
    for elem in pairs:
        if abs(elem[1]-elem[0])==mlst:
            print(f'{elem[0]}, {elem[1]}')


if __name__ == '__main__':

    len_arr = int(input('Length of array?').strip())

    arr = []
    print('Enter array elemnts:')
    for _ in range(len_arr):
        arr_item = int(input().strip())
        arr.append(arr_item)
    
    PairsWithMinimumDiff(arr)
