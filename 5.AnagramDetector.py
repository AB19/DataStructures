# find anagrams
# Eg: earth and heart

Str1 = "earth"
Str2 = "heart"

# Does with a complexity of n^2
def CheckAll (Str1, Str2):
    List1 = list (Str1)
    List2 = list (Str2)
    for i in range (len (List1)):
        for j in range (len (List2)):
            if (List1 [i] == List2 [j]):
                List2 [j] = "Jaffa"
    for i in range (len (List2)):
        if (List2 [i] != "Jaffa"):
            return False
    return True

RetVal = CheckAll (Str1, Str2)
print (RetVal)

def SortAndCompare (Str1, Str2):
    List1 = list (Str1)
    List2 = list (Str2)

    List1.sort()
    List2.sort()

    if (List1 == List2):
        return True
    else:
        return False

RetVal = SortAndCompare (Str1, Str2)
print (RetVal)
