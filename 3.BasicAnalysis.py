import time

def SumVal (TempVal):
    start = time.time ()

    SumVal = 0
    for i in range (1, TempVal + 1):
        SumVal = SumVal + i

    end = time.time ()
    Seconds = end - start
    print ("Seconds passed: %10.7f" %(Seconds))
    return SumVal

Val = int (input ())
print (SumVal (Val))
