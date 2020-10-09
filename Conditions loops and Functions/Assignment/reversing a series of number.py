#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 19:03:28 2020

@author: Cheerag



Print the following pattern for the given number of rows.
Pattern for N = 5
1 
3 2 
4 5 6 
10 9 8 7 
11 12 13 14 15
Input format : N (Total no. of rows)

Output format : Pattern in N lines

"""

def printPattern(n):
    count = 0
    for i in range(1,n+1):             #to iterate over rows
        #for even rows
        if i % 2 == 0:
            for evenrows in range(i):
                print(count,end=" ")
                count -=1
            count=count+i

            
        else:                           #for odd rows
            for oddrows in range(i):
                count+=1
                print(count,end=" ")
            count = count +i+1
        
        print()
            
printPattern(5)
        
        