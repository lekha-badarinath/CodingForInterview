#Print a given matrix in spiral form
#****One small glitch - 4 is getting types twice
#https://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/
from __future__ import print_function

def spiral(m,n,arr):
    '''
    m - No. of rows
    n - No. of columns 
    k - counter for rows 
    l - counter for columns 
    '''
    k = 0;l = 0
    while (k < m and l < n):
        for i in range(l,n):              #m=3,n=4,k=0,l=0
            print (arr[k][i], end=" ")
        k += 1
        for i in range(k,m):            #m=3,n=4,k=1,l=0
            print (arr[i][n-1], end=" ")
        n -= 1    
        if k<m:    
            for i in range(n-1,l-1,-1):         #m=3,n=3,k=1,l=0 #l = 0, since upper range is not printed, giving l-1 = -1, 
                                                #will print the element at 0 also.
                print (arr[m-1][i], end=" ")
            m -= 1
        if l<n:
            for i in range(m-1,k-1,-1):         #m=3, n=3,k=1,l=0
                print (arr[i][l], end=" ")
            l += 1

arr = [ [1,2,3,10],
        [4,5,6,11],
        [7,8,9,12] ]
spiral(3,4,arr)
