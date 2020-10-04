#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 22:08:04 2020

@author: Cheerag
"""

def reverseString(s):
    splitString = s.split()
    for s in splitString:
        print(s[::-1],end=" ")
    


inputString = 'cheerag verma'
reverseString(inputString)