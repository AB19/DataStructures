class DeQueue():

    def __init__ (self):
        self.MyDeQ = []

    def AddFront (self, item):
        self.MyDeQ.insert (0, item)

    def AddBack (self, item):
        self.MyDeQ.append (item)

    def RemoveFront (self):
        return self.MyDeQ.pop (0)

    def RemoveBack (self):
        return self.MyDeQ.pop ()

    def isEmpty (self):
        if (len (self.MyDeQ) > 0):
            return False
        else:
            return True

    def Size (self):
        return len (self.MyDeQ)
