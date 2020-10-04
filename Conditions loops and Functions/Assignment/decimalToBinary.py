#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 01:35:09 2020

@author: Cheerag
"""


def decimalToBinary(num):
    result = ""
    while num>0:
        reminder = str(num%2)
        result = result+reminder
        num = num//2
        
    return result[::-1]


print(decimalToBinary(8))
