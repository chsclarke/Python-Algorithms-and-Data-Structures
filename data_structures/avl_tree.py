# -*- coding: utf-8 -*-
"""
This is an example of AVL tree insert and print functinos implimented in python 3.
Copyright 2018 Chase Clarke cfclarke@bu.edu
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.leftChild = None
        self.rightChild = None
        self.height = 1
        self.balance = 0

class AVLTree:
    def __init__(self, rootNode):
        self.root = rootNode
        

    def insert(self, key, currentNode):
        insertNode = Node(key)
        insertNode.parent = currentNode

        #recursivly checking nodes until correct insert location found
        if insertNode.data < currentNode.data:
            if(currentNode.leftChild is None):
                currentNode.leftChild = insertNode

            else:
                self.insert(key, currentNode.leftChild)

        elif insertNode.data > currentNode.data:
            if(currentNode.rightChild is None):
                currentNode.rightChild = insertNode

            else:
                self.insert(key, currentNode.rightChild)

        #calculating height and balance of each node
        currentNode.height = 1 + self.getMax(currentNode.leftChild, currentNode.rightChild)
        currentNode.balance  = self.getBalance(currentNode.leftChild, currentNode.rightChild)


        #performing tree rotations to correct balance if needed
        #Case 1: Left - Left
        if currentNode.balance > 1 and key < currentNode.leftChild.data:
            return self.rightRotation(currentNode)
            
        #Case 2: Right - Right
        if currentNode.balance < -1 and key > currentNode.rightChild.data:
            return self.leftRotation(currentNode)

        #Case 3: Left - Right
        if currentNode.balance > 1 and key > currentNode.leftChild.data:
            currentNode.leftChild = self.leftRotation(currentNode.leftChild)
            return self.rightRotation(currentNode)

        #Case 4: Right - Left
        if currentNode.balance < -1 and key < currentNode.rightChild.data:
            currentNode.rightChild = self.rightRotation(currentNode.rightChild)
            return self.leftRotation(currentNode)
            
        return currentNode

    def leftRotation(self, root):
        print("left rotation on", root.data)
        temp = root.rightChild
        temp2 = temp.leftChild
        temp.leftChild = root
        root.rightChild = temp2
       
        #reassigning parents
        if root is not self.root:
            temp.parent = root.parent
            temp.parent.rightChild = temp

        root.parent = temp

        #re-calculating the height and balance for nodes
        root.height = 1 + self.getMax(root.leftChild, root.rightChild)
        temp.height = 1 + self.getMax(temp.leftChild, temp.rightChild)  
        root.balance  = self.getBalance(root.leftChild, root.rightChild)
        temp.balance  = self.getBalance(temp.leftChild, temp.rightChild)   

        #reassigning root
        if(root is self.root):
            self.root = temp

        return temp

    def rightRotation(self, root):
        print("right rotation on", root.data)
        temp = root.leftChild
        temp2 = temp.rightChild
        temp.rightChild = root
        root.leftChild = temp2
        
        #reassigning parents
        if root is not self.root:
            temp.parent = root.parent
            temp.parent.leftChild = temp

        root.parent = temp

        #re-calculating the height and balance for nodes
        root.height = 1 + self.getMax(root.leftChild, root.rightChild)
        temp.height = 1 + self.getMax(temp.leftChild, temp.rightChild)
        root.balance  = self.getBalance(root.leftChild, root.rightChild)
        temp.balance  = self.getBalance(temp.leftChild, temp.rightChild) 
        
        #reassigning root
        if(root is self.root):
            self.root = temp

        return temp


    def getMax(self, leftChild, rightChild):
        #checking for nonetype so max() isnt broken when child doesnt exist
        if (leftChild is None):
            if (rightChild is not None):
                return rightChild.height
            else:
                return 0
        elif (rightChild is None):
            if (leftChild is not None):
                return leftChild.height
            else:
                return 0
        else:
            return max(leftChild.height, rightChild.height)

    def getBalance(self, leftChild, rightChild):
        #checking for nonetype so max() isnt broken when child doesnt exist
        if (leftChild is None):
            if (rightChild is not None):
                return 0-rightChild.height
            else:
                return 0
        elif (rightChild is None):
            if (leftChild is not None):
                return leftChild.height
            else:
                return 0
        else:
            return (leftChild.height - rightChild.height)

    
    def printTree(self, root):
        #inorder traversal of tree
        if(root.leftChild is not None):
            self.printTree(root.leftChild)
        print(root.data)
        if (root.rightChild is not None):
            self.printTree(root.rightChild)


    def height(self, root): 
        # helper function for checking if tree is balanced
        # added after data structure coded
        if root is None: 
            return 0
        return max(self.height(root.leftChild), self.height(root.rightChild)) + 1
    
    def isBalanced(self, root):
        # checking if tree is balanced
        if root is None:
            return True
        
        balance = self.height(root.leftChild) - self.height(root.rightChild)
        
        if (balance > -2 and balance < 2 and self.isBalanced(root.leftChild) is True and self.isBalanced(root.rightChild) is True):
            return True
        else:
            return False

root = Node(1)

MyAVL = AVLTree(root)

lst = [3,5,4,2,16,15,20,25]

for i in lst:
    root = MyAVL.insert(i, root)

print("\ntree inorder:")
MyAVL.printTree(root)
print("\n", MyAVL.isBalanced(root))