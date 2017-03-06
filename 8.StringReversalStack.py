# Reverse a string using stack
class Stack():

    def __init__(self):
        self.MyStack = []

    def AddItem (self, item):
        self.MyStack.append (item)

    def RemoveItem (self):
        return self.MyStack.pop ()

    def Peek (self):
        return self.MyStack [-1]

    def isEmpty (self):
        StackLen = len (self.MyStack)
        if StackLen == 0:
            return True
        else:
            return False

    def CheckSize (self):
        return len (self.MyStack)

    def PrintStack (self):
        print (self.MyStack)

    def ClearStack (self):
        del self.MyStack [:]

class StringReversal ():

    def __init__ (self):
        pass

    def Reverse (self, InVal):
        self.InStr = InVal
        self.InList = list (self.InStr)
        StackObj = Stack ()
        while len (self.InList) > 0:
            StackObj.AddItem (self.InList [0])
            del self.InList [0]
        self.OutStr = ""
        while StackObj.isEmpty() == False:
            Val = StackObj.RemoveItem ()
            self.OutStr = self.OutStr + Val
        return self.OutStr

StrRev = StringReversal ()
InStr = input ()
OutStr = StrRev.Reverse (InStr)
print ("Reversal of " + InStr + " is " + OutStr)
