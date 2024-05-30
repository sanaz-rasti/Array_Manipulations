#!/usr/bin/env python

def RightReverse(arr, LenArr, NumRot): 
    tempArr = [0] * LenArr
    tempArr[:NumRot] = arr[-NumRot:]
    tempArr[NumRot:] = arr[:LenArr-NumRot]    
    return tempArr


if __name__ == '__main__':
    testcases = int(input('Enter number of test cases:'))
    for i in range(testcases):
        print('-----------------------------------')
        print(f'Test case {i}')
        N = int(input('Size of array:'))
        K = int(input('Number of rotations:'))
        arr = []
        for l in range(N):
            arr.append(int(input('Array Element: ')))

        print('-----------------')
        print(f'Array:{arr}')
        print(f'Reverse of Array: {RightReverse(arr,N,K)}')

