# implementation of a stack data structure
# operations: add, remove, peek, check if empty, size
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

StackObj = Stack()
print (StackObj.isEmpty())
StackObj.AddItem (4)
StackObj.AddItem ("Jaffa")
StackObj.PrintStack()
print (StackObj.isEmpty())
print (StackObj.Peek ())
print ("Length of the Stack is: " + str (StackObj.CheckSize()))
StackObj.ClearStack ()
print ("Length of the Stack after clearing is: " + str (StackObj.CheckSize()))
