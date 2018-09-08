# -*- coding: utf-8 -*-
"""
This is an example of a doubly linked list in python 3. 
Copyright 2018 Chase Clarke cfclarke@bu.edu
"""

class Node:
    
    def __init__(self,val):
        self.val = val
        self.next = None 
        self.prev = None

class LList:
    
    def __init__(self, node):
        self.head = node
        self.tail = None
        self.iterator = None
        
    def find(self, val):
        
        self.iterator = self.head
        
        #iterate through list until element is found or list ends
        while(self.iterator.next is not None):
            
                if (self.iterator.val is val):
                    return ("found")
                    
                self.iterator = self.iterator.next
                
        if(self.iterator.val is val):
            return("Found")
            
        if (self.iterator.next is None):
            return str(val) + " not found."
            

    def insert(self, val):
        
        insertNode = Node(val)
        self.iterator = self.head
        
        #if only one element
        if(self.head.next is None):
            self.head.next = insertNode
            insertNode.prev = self.head
            self.tail = insertNode
            return
        
        #> 1 element
        else:
            while(self.iterator.next is not None):
                self.iterator = self.iterator.next
                
            self.iterator.next = insertNode
            insertNode.prev = self.iterator
            self.tail = insertNode
            self.tail = insertNode

    def remove(self, val):
        
        self.iterator = self.head
        iterator = self.iterator
        
        #head of list
        if(self.head.val is val):
            self.head = self.head.next
            self.head.prev = None
            return
        
        #tail of list
        elif(self.tail.val is val):
            self.tail = self.tail.prev
            self.tail.next = None
            return
        
        #middle of list
        else:
            while(iterator.next is not None):
                iterator = iterator.next
                
                if(iterator.val is val):
                    iterator.prev.next = iterator.next
                    iterator.next.prev = iterator.prev
                    return
                
                else:
                    return str(val) + "not found."
    
    def printList(self):
        
        if(self.head is not None):
            self.iterator = self.head
            print(self.iterator.val, end=", ")
            
            while(self.iterator.next is not None):
                self.iterator = self.iterator.next
                print(self.iterator.val, end=", ")
    
        else:
            print("List is empty.")
        print("")
            

class OpenChain:

    def __init__(self, hashValue):
        self.hashValue = hashValue
        self.hashTable = []

        #builds empty hash table with header nodes in each index
        for i in range(0,hashValue-1):
            self.hashTable.append(LList(Node(None)))

    
    def insert(self, data):
        location = data%self.hashValue
        LinkList = self.hashTable[location]
        LinkList.iterator = LinkList.head

        #if index empty add data there
        if (LinkList.head.val is None):
            LinkList.head.val = data
            return

        #else iterate to end of LList and add there
        else:
            LinkList.insert(data)
            return


    def find(self, data):
        location = data%self.hashValue
        LinkList = self.hashTable[location]
        LinkList.iterator = LinkList.head

        if (LinkList.head.val is data):
            print(data, "found at", id(data))
            return
        else:
            while(LinkList.iterator.next is not None):
                LinkList.iterator = LinkList.iterator.next 
                if (LinkList.iterator.val is data):
                    print(data, "found at", id(data))
                    return

            print(data, "not found.")
            return
    
    def printTable(self):
        for i in self.hashTable:
            i.printList()
        print()


"""Open Chaining Example"""

HashTable = OpenChain(10)

HashTable.insert(2)
HashTable.insert(3)
HashTable.insert(4)
HashTable.insert(14)
HashTable.insert(24)

HashTable.printTable()

HashTable.find(2)
HashTable.find(4)
HashTable.find(14)
HashTable.find(24)
HashTable.find(7)



"""Doubly Linked List Example"""

# node1 = Node(12) #initialize new node
# lst1 = LList(node1) #initialize new llist with node

# #add values to list
# lst1.insert(13)
# lst1.insert(14)
# lst1.insert(15)

# #print full list from head to tail
# lst1.printList()

# #print tail->prev->prev
# print(lst1.tail.prev.prev.val)

# #find element in list
# print(lst1.find(16))

# #remove element
# lst1.remove(14)

# #print updated list
# lst1.printList()
