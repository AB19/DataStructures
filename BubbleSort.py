# -*- coding: utf-8 -*-

def main ():
    
    unsortedArr = [10, -1, 34, 89, 50, -7, -189]
    sortedArr = bubbleSort (unsortedArr)
    print (sortedArr)
    
    assert (sortedArr == sorted (unsortedArr))
    return
    
def bubbleSort (unsortedArr):
    unsortedIndex = len (unsortedArr) - 1
    while (unsortedIndex > 0):
        for i in range (unsortedIndex):
            if unsortedArr [i] > unsortedArr [i + 1]:
                temp = unsortedArr [i]
                unsortedArr [i] = unsortedArr [i + 1]
                unsortedArr [i + 1] = temp
        unsortedIndex -= 1
        
    return unsortedArr
    
main ()