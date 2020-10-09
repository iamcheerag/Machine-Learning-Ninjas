#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 19:45:13 2020

@author: Cheerag
"""

def indexOfCommonElement(commonElement,arr1,arr2):
    commonElementIndexInArr1 =[]
    commonElementIndexInArr2 =[]
    
    for data in commonElement:
        commonElementIndexInArr1.append(arr1.index(data))
        commonElementIndexInArr2.append(arr2.index(data))
        
    return commonElementIndexInArr1,commonElementIndexInArr2
    
    
    
def commonElementInBothArray(arr1,arr2):
    commonElement = []
    for ele1 in range(len(arr1)):
        if arr1[ele1] in arr2:
            commonElement.append(arr1[ele1])  

    return commonElement


def maximizeSum(commonElementIndexInArr1,commonElementIndexInArr2,arr1,arr2,commonElement):
    while arr1 and arr2:   
        sum1 = arr1[:commonElementIndexInArr1[0]]
        sum2 = arr2[:commonElementIndexInArr1[0]]
        ans = max(sum1,sum2)
        
        while arr1 and arr2:
            for i in range(1,len(commonElement)):
                sum1 = arr1[i:i+1]
                sum2 = arr2[i:i+1]
                
            if sum1<sum2:
                ans+=sum1
            else:
                ans+=sum2
        return ans
            
        
    
    
arr1 = [1,2,3,4]
arr2 = [2,3,9,11]
commonElement = commonElementInBothArray(arr1,arr2)
commonElementIndexInArr1,commonElementIndexInArr2 = indexOfCommonElement(commonElement,arr1,arr2)
maximizeSum(commonElementIndexInArr1,commonElementIndexInArr2,arr1,arr2,commonElement)