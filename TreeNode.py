# -*- coding: utf-8 -*-

class TreeNode ():
    
    # constructor - takes data and creates a tree node
    def __init__ (self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None
        
    def insert (self, value):
        
        if self.value == value:
            print ("Cannot insert! Value exists!")
            return
            
        if self.value > value:
            if self.leftChild is None:
                self.leftChild = TreeNode (value)
            else:
                self.leftChild.insert (value)
            
        if self.value < value:
            if self.rightChild is None:
                self.rightChild = TreeNode (value)
            else:
                self.rightChild.insert (value)
                
    def getMax (self):
        
        if self.rightChild is not None:
            self.rightChild.getMax ()
            
        else:
            return self.value
            
    def getMin (self):
        
        if self.leftChild is not None:
            self.leftChild.getMin ()
            
        else:
            return self.value
            
    def inOrder (self):
        
        if self.leftChild is not None:
            self.leftChild.inOrder ()
            
        print (self.value)
        
        if self.rightChild is not None:
            self.rightChild.inOrder ()