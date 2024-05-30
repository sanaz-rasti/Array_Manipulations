#!/usr/bin/env python
import numpy as np
import time

def hcf2numbers():
    m,n = map(int,input('Enter two positive numbers(integers): ').split(" "))
    # ------ Method I ------
    print('\n# ------ Method I -------')
    start = time.time()
    while m!=n:
        if m>n:
            m = m-n
        else:
            n = n-m
    print(f'HCF: {m}')
    print(f'ET: {time.time() - start} secs.')

    # ------ Method II -------
    print('\n# ------ Method II -------')
    start = time.time()
    while m!=n:
        n,m,_ = np.sort([m,n,abs(m-n)])
    print(f'HCF: {m}')
    print(f'ET: {time.time() - start} secs.')


if __name__ == '__main__':
    hcf2numbers()
    