#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 22:15:53 2020

@author: Cheerag

Even Fibonacci Numbers

    Given a number N find the sum of all the even valued terms in the fibonacci sequence less than or equal to N. Try generating only even fibonacci numbers instead of iterating over all Fibonacci numbers.
    Input Format
    Line 1 : An integer N
    Output Format
    Total Sum
    Input Constraints
    1 <= N <= 10^6
    Sample Input 1:
    8
    Sample Output 1 :
    10
    Sample Input 2:
    400
    Sample Output 2:
    188
"""

def evenFib(n):
    a = 1
    b = 1
    i = 2
    ans = 0
    while i <n-1:
        sum = a+b
        if sum%2==0:    
            ans = ans + sum
            print(sum)
        a,b = b,sum
        i+=1     
    return ans
        
        
evenFib(10)