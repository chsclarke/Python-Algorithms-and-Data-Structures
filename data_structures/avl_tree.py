# -*- coding: utf-8 -*-
"""
This is an example of an AVL tree implimented in python 3.
Copyright 2018 Chase Clarke cfclarke@bu.edu
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

class AVLTree:
    def __init__(self, rootNode):
        self.root = rootNode


    def insert(self, key, currentNode):
        insertNode = Node(key)

        if insertNode.data < currentNode.data:
            if(currentNode.leftChild is None):
                currentNode.height += 1
                currentNode.leftChild = insertNode

            else:
                currentNode.height = 1 + self.insert(key, currentNode.leftChild)

        elif insertNode.data > currentNode.data:
            if(currentNode.rightChild is None):
                currentNode.height += 1
                currentNode.rightChild = insertNode

            else:
                currentNode.height = 1 + self.insert(key, currentNode.rightChild)
        
        balance = self.getBalance(currentNode)
 
        # Case 1 - Left Left
        if balance > 1 and key < currentNode.leftChild.data:
            return self.rightRotation(currentNode)
 
        # Case 2 - Right Right
        if balance < -1 and key > currentNode.rightChild.data:
            return self.leftRotation(currentNode)
 
        # Case 3 - Left Right
        if balance > 1 and key > currentNode.leftChild.data:
            currentNode.leftChild = self.leftRotation(currentNode.leftChild)
            return self.rightRotation(currentNode)
 
        # Case 4 - Right Left
        if balance < -1 and key < currentNode.rightChild.data:
            currentNode.rightChild = self.rightRotation(currentNode.rightChild)
            return self.leftRotation(currentNode)
        
        return currentNode.height

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

    def leftRotation(self, root):
        temp = root.rightChild
        temp2 = temp.leftChild
        temp.leftChild = root
        root.rightChild = temp2

        root.height = 1 + self.getMax(root.leftChild, root.rightChild)
        temp.height = 1 + self.getMax(temp.leftChild, temp.rightChild)

        self.root = temp
        

    def rightRotation(self, root):
        temp = root.leftChild
        temp2 = temp.rightChild
        temp.rightChild = root
        root.leftChild = temp2

        root.height = 1 + self.getMax(root.leftChild, root.rightChild)
        temp.height = 1 + self.getMax(temp.leftChild, temp.rightChild)

        self.root = temp


    def getHeight(self, root):
        if not root:
            return 0
 
        return root.height
 
    def getBalance(self, root):
        if not root:
            return 0
 
        return self.getHeight(root.leftChild) - self.getHeight(root.rightChild)

    """inorder traversal of tree"""
    def printTree(self, root):

        if(root.leftChild is not None):
            self.printTree(root.leftChild)

        print(root.data)
        
        if (root.rightChild is not None):
            self.printTree(root.rightChild)


root = Node(1)

MyAVL = AVLTree(root)

lst = [2, 3, 4, 5]

for i in lst:
    MyAVL.insert(i, root)

MyAVL.printTree(MyAVL.root)