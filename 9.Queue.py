class Queue ():

    def __init__ (self):
        self.MyQueue = []

    def AddItem (self, item):
        self.MyQueue.insert (0, item)

    def RemoveItem (self):
        return self.MyQueue.pop ()

    def isEmpty (self):
        if len (self.MyQueue) == 0:
            return True
        else:
            return False

    def CheckSize (self):
        return len (self.MyQueue)

    def PrintQue (self):
        print (self.MyQueue)

QueObj = Queue()
print (QueObj.isEmpty())
QueObj.AddItem (3)
QueObj.AddItem ("jaffa")
print (QueObj.CheckSize ())
print (QueObj.RemoveItem ())
QueObj.PrintQue ()
