#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 23:14:12 2020

@author: Cheerag
"""

def leaderInArray(arr):
    stack=[-9999]
    result = []
    for i in range(len(arr)-1,-1,-1):
        if arr[i]>=stack[-1]:
            result.append(arr[i])
            stack.append(arr[i])
    return result[::-1]

arr= list(map(int,input().split()))         
ans = (leaderInArray(arr))
print(*ans)