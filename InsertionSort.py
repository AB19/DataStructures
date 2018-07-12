# -*- coding: utf-8 -*-

def main ():
    
    unsortedArr = [10, -1, 34, 89, 50, -7, -189]
    sortedArr = insertionSort (unsortedArr)
    print (sortedArr)
    
    assert (sortedArr == sorted (unsortedArr))
    return
    
def insertionSort (unsortedArr):
    
    for sortedIndex in range (1, len (unsortedArr)):
        for i in range (sortedIndex, 0, -1):
            if unsortedArr [i] < unsortedArr [i - 1]:
                temp = unsortedArr [i]
                unsortedArr [i] = unsortedArr [i - 1]
                unsortedArr [i - 1] = temp
            else:
                break
    return unsortedArr
    
main ()