#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 01:59:31 2020

@author: Cheerag
"""


def trailingZero(n):
    i=1
    flag = True
    result = 0
    while flag == True:
        ans = n//(5**i)
        if ans == 0:
            flag = False            
        result +=ans
        #print(result)
        i+=1
    
    return result

#n = int(input())
print(trailingZero(50))
