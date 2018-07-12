# -*- coding: utf-8 -*-

def main ():
    
    unsortedArr = [10, -1, 34, 89, 50, -7, -189]
    sortedArr = selectionSort (unsortedArr)
    print (sortedArr)
    
    assert (sortedArr == sorted (unsortedArr))
    return
    
def selectionSort (unsortedArr):
    unsortedIndex = len (unsortedArr) - 1
    while (unsortedIndex != 0):
        maxVal, index = unsortedArr [0], 0
        for i in range (unsortedIndex + 1):
            if maxVal < unsortedArr [i]:
                maxVal = unsortedArr [i]
                index = i
        temp = unsortedArr [unsortedIndex]
        unsortedArr [unsortedIndex] = maxVal
        unsortedArr [index] = temp
        unsortedIndex -= 1
    return unsortedArr
    
main ()