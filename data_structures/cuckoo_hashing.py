# -*- coding: utf-8 -*-
"""
This is an example of insertion sort in python 3.
wost case runtime O(n^2)
Copyright 2018 Chase Clarke cfclarke@bu.edu
"""

class CuckooHashTable:
    
    def __init__(self,hashValue1, hashValue2):
        self.hashValue1 = hashValue1
        self.hashValue2 = hashValue2
        self.hashTable1 = [None] * hashValue1
        self.hashTable2 = [None] * hashValue2

    """The insert function will give the program 100 tries to find an empty index.
       It checks correct index in the first list and if not empty will assign the 
       first lists value to a temp variable, insert 'data' into that list and index then
       repeats the cycle on the other list."""
    def insert(self, data):
        currData = data    

        for i in range(0,100):
            currTable = i % 2
            
            #hashTable1
            if (currTable is 0):
                if (self.hashTable1[currData % self.hashValue1] is None):
                    self.hashTable1[currData % self.hashValue1] = currData
                    return
                else:
                    self.hashTable1[currData % self.hashValue1], currData = currData,  self.hashTable1[currData % self.hashValue1]
                    
            #hashTable2
            elif (currTable is 1):
                if (self.hashTable2[currData % self.hashValue2] is None):
                    self.hashTable2[currData % self.hashValue2] = currData
                    return
                else:
                    self.hashTable2[currData % self.hashValue2], currData = currData,  self.hashTable2[currData % self.hashValue2]

        return "Infinte loop detected, item not inserted. REHASH."

    def find(self, data):

        if (self.hashTable1[data % self.hashValue1] is data):
            print (data, "found at", id(self.hashTable1[data % self.hashValue1]))
            return

        elif (self.hashTable2[data % self.hashValue2] is data):
            print (data, "found at", id(self.hashTable2[data % self.hashValue2]))
            return

        else:
            print (data, "not found.")
            return
        
    def printTable(self):

        print(self.hashTable1)
        print(self.hashTable2)
        return


HashTable = CuckooHashTable(10, 9)

HashTable.insert(3)
HashTable.insert(4)
HashTable.insert(5)
HashTable.insert(15)
HashTable.insert(25)

HashTable.printTable()

HashTable.find(25)
HashTable.find(32)