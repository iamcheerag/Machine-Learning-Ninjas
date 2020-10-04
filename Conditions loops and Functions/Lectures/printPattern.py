#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 21:22:13 2020

@author: Cheerag
"""


def printPattern(n):
    row = 0
    while row<n:
        col = 0
        count = 1
        '''
        This for printing numbers in increasing order
        '''
        while col<=row:
            print(count,end="")
            count+=1
            col+=1
        
        
        for spaces in range(2*(n-row-1)):  #for spaces
            print(" ",end="")
            
        
        count = row+1
        while count>=1:
            print(count,end="")
            count-=1
            
        print()
        row+=1  
 
        
        
n = 4
printPattern(n)