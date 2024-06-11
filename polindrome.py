#!/usr/bin/env python

'''
Polindrome Number: It is a number with symmetric digit format. Which means if you reverse the digits the number remains the same. 
e.g.:  Number 17571 is a Polindrome. 

Faciniating Polindromes produced when an N-digit number consisting only 'digit-1'(1,11,111,1111) is powered by 2 (^2). The length of produced Plondrome is (2*N-1)

1^2    = 1
11^2   = 121
111^2  = 12321
1111^2 = 1234321
.
.
In order to produce sequence of 1, 11, 111 look for integral devision of powers of 10 by 9. e.g: 10//9=1 , 100//9=11, 1000//9=111, etc.   

In this script, a python function asks the user to input the N, and returns the sequence of N Polindrome numbers.

'''
import time
def polin1sN():

    N = int(input('Enter number N: '))
    
    # ------ Method I -------
    print('\n# ------ Method I -------')
    start = time.time()
    for i in range(1, N+1):
        print((10**i//9)**2)
    print(f'ET: {time.time() - start} secs.')


    # ------ Method II -------
    print('\n# ------ Method II -------')
    start = time.time()
    list(map(lambda i:print((10**i//9)**2),range(1,N+1))) 
    print(f'ET: {time.time() - start} secs.')


if __name__ == '__main__':
    polin1sN()




    