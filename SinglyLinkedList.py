# -*- coding: utf-8 -*-

# node class
class Node (object):
    
    # value and next node pointer
    def __init__ (self, value):
        self.value = value
        self.next = None
        
class LinkedList (object):
    
    # head
    def __init__ (self):
        self.head = None
        
    def insertFirst (self, value):
        newNode = Node (value)
        
        # empty list
        if self.head == None:
            self.head = newNode
            return
            
        # not an empty list
        newNode.next = self.head
        self.head = newNode
        return
        
    def insertLast (self, value):
        newNode = Node (value)
        
        # empty list
        if self.head == None:
            self.head = newNode
            return
            
        # not an empty list - find the last node
        current = self.head 
        while (current.next != None):
            current = current.next
            
        current.next = newNode
        return
        
    def getSize (self):
        
        # empty list
        if self.head == None:
            return 0
            
        size = 1
        current = self.head 
        while (current.next != None):
            current = current.next
            size += 1
            
        return size
    
    def removeFirst (self):
        
        # empty list
        if self.head == None:
            print ("Empty List")
            return
            
        # only one element 
        if self.head.next == None:
            self.head = None
            return
            
        # more than one
        self.head = self.head.next
        return 
        
    def removeLast (self):
        
        # empty list
        if self.head == None:
            print ("Empty List")
            return
            
        # only one element 
        if self.head.next == None:
            self.head = None
            return
            
        # more than one
        current = self.head
        advance = self.head.next
        while (advance.next != None):
            current = current.next
            advance = advance.next
            
        current.next = None
        return
        
    def insertBefore (self, value, existingValue):
        
        # empty list
        if self.head == None:
            print ("Empty List")
            return
        
        # only one element
        if self.head.next == None:
            if self.head.value == existingValue:
                self.insertFirst (value)
                return
        
        # more than one
        if self.head.value == existingValue:
            self.insertFirst (value)
            return
            
        current = self.head.next
        previous = self.head
        while (current.next != None):
            if current.value == existingValue:
                newNode = Node (value)
                previous.next = newNode
                newNode.next = current
                return
            current = current.next
            previous = previous.next
            
        print ("Could not find the element! No insertion made.")
        return
        
    def insertAfter (self, value, existingValue):
        
        # empty list
        if self.head == None:
            print ("Empty List")
            return
        
        # only one element
        if self.head.next == None:
            if self.head.value == existingValue:
                self.insertLast (value)
                return
            
        current = self.head.next
        while (current != None):
            if current.value == existingValue:
                newNode = Node (value)
                newNode.next = current.next
                current.next = newNode
            current = current.next
            
        print ("Could not find element! No insertion made.")
        return
        
        
    def printList (self):
        # empty list
        if self.head == None:
            print ("Empty List")
            return
            
        # not an empty list
        current = self.head
        
        while (current != None):
            print (current.value)
            current = current.next
        return
        
myList = LinkedList ()
myList.printList ()
myList.insertFirst (45)
myList.insertFirst (56)
myList.insertFirst (67)
myList.insertFirst (5)
myList.printList ()
myList.insertLast (99)
myList.insertLast (88)
myList.printList ()
print (myList.getSize ())
myList.insertLast (99)
myList.insertLast (88)
print (myList.getSize ())
myList.removeFirst ()
myList.printList ()
myList.removeLast ()
myList.removeLast ()
myList.printList ()
myList.insertBefore (77, 99)
myList.printList ()
myList.insertBefore (66, 67)
myList.printList ()
myList.insertAfter (111, 45)