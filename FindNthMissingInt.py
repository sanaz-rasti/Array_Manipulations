#!/usr/bin/env python

# ---------------------------
'''
Given an array of arr and requested N for the N-th missing integer value to be found, 
the function returns a list of missing integer elements. 
e.g:
    Input:
        N = 5
        len_arr = 3
        Array = [1,7,8]
    
    Output:
        [2, 3, 4, 5, 6]
'''
# ---------------------------
def FindNthMissingInt(arr, N):
    arn = list(set(arr))
    lst  = []
    for i in range(1,len(arn)+N+1):
        if not i in arn and len(lst)<N:
            lst.append(i)
    return lst 


if __name__ == '__main__':
    N = int(input('Nth missing integer?'))
    len_arr = int(input('Length of array?').strip())
    arr = []
    
    print('Enter array elemnts:')
    for _ in range(len_arr):
        arr_item = int(input().strip())
        arr.append(arr_item)
    
    print(FindNthMissingInt(arr, N))
