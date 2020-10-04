#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 01:44:21 2020

@author: Cheerag
"""


def isPrime(num):
    if num == 0:
        return 0
    i =2
    while i<num:
        if num%i ==0:
            break
        i+=1
    else:
        return num #"Prime"
    
    #return "Not Prime"

def printPrimeWithInRange(n):
    for i in range(2,n+1):
        result = isPrime(i)
        if result is not None:
            print(result)
    
    
printPrimeWithInRange(4)