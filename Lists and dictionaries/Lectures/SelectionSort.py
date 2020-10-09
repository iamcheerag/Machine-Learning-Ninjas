# -*- coding: utf-8 -*-

def selectionSort(arr):
    minIndex = 0
    for i in range(len(arr)):
        minIndex = i
        for j in range(i+1,len(arr)):
            if arr[minIndex]>arr[j] and j<len(arr):
                minIndex = j

        arr[i],arr[minIndex] = arr[minIndex],arr[i]
    
    return arr

inputArr = [10,7,5,2,9]
print(selectionSort(inputArr))
list(map(int,input().split()))