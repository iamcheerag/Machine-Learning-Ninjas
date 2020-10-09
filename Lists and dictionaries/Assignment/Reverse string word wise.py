#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 12:53:56 2020

@author: Cheerag

Reverse string Word Wise

Reverse the given string word wise. That is, the last word in given string should come at 1st place, last second word at 2nd place and so on. Individual words should remain as it is.
Input format :
String in a single line
Output format :
Word wise reversed string in a single line
Constraints :
0 <= |S| <= 10^7
where |S| represents the length of string, S.
Sample Input 1:
Welcome to Coding Ninjas
Sample Output 1:
Ninjas Coding to Welcome
Sample Input 2:
Always indent your code
Sample Output 2:
code your indent Always
"""

def reverseString(s):
    splitString = s[::-1]
    splitString = splitString.split()
    for s in splitString:
        #print(s)
        print(s[::-1],end=" ")
    


inputString =input()
reverseString(inputString)

