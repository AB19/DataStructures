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


class DecimalToBinary ():

    def __init__ (self):
        pass

    def ConvertToDec (self, DecimalVal):
        self.Dec = DecimalVal
        StackObj = Stack ()
        while self.Dec > 0:
            StackObj.AddItem (self.Dec % 2)
            self.Dec = self.Dec // 2
        self.Binary = ""
        while (StackObj.isEmpty() == False):
            Val = StackObj.RemoveItem ()
            self.Binary = self.Binary + str (Val)
        return self.Binary

InVal = int (input ())
DecObj = DecimalToBinary ()
TestVal = DecObj.ConvertToDec (InVal)
print ("Binary Value of " + str (InVal) + " is: " + str (TestVal))
