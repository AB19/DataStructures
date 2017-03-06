# Find minimum in a list
# first one compares each element with one another
import time
MyList = [22, 256, 8, -99, -3, 56, 98, 8, 7, 3330, 22, 311, -33232, 556, 78]

def BadOne (TempList):
    start = time.time()

    for i in range (len (TempList)):
        for j in range (len (TempList)):
            if (TempList [i] < TempList [j]):
                TempVal = TempList [i]
                TempList [i] = TempList [j]
                TempList [j] = TempVal

    MinVal = TempList [0]
    end = time.time ()

    Seconds = end - start
    print ("Seconds passed: %10.7f" %(Seconds))

    return MinVal

RetVal = BadOne (MyList)
print ("Min Val: " + str (RetVal))

# Second one compares a variable with all the variables in the list
def GoodOne (TempList):
    start = time.time ()

    MinVal = 0
    for i in range (len (TempList)):
        if (TempList [i] < MinVal):
            MinVal = TempList [i]

    end = time.time ()

    Seconds = end - start
    print ("Seconds passed: %10.7f" %(Seconds))

    return MinVal

RetVal = GoodOne (MyList)
print ("Min Val: " + str (RetVal))
