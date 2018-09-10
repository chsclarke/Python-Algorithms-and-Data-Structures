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

class BST:
    def __init__(self, rootNode):
        self.root = rootNode

    def insert(self, key, currentNode):
        insertNode = Node(key)

        currentNode.height = 1 + max(self.getHeight(currentNode.leftChild), self.getHeight(currentNode.rightChild))

        if insertNode.data < currentNode.data:
            if(currentNode.leftChild is None):
                currentNode.leftChild = insertNode
                return

            else:
                self.insert(key, currentNode.leftChild)

        elif insertNode.data > currentNode.data:
            if(currentNode.rightChild is None):
                currentNode.rightChild = insertNode
                return

            else:
                self.insert(key, currentNode.rightChild)


    def leftRotation(self, root):
        temp = root.rightChild
        temp2 = temp.leftChild

        temp.leftChild = root
        root.rightChild = temp2

        return


    def rightRotation(self, root):
        temp = root.leftChild
        temp2 = temp.rightChild

        temp.rightChild = root
        root.leftChild = temp2

        return

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

MyBST = BST(root)

lst = [2, 3, 4, 5]

for i in lst:
    MyBST.insert(i, root)

MyBST.printTree(root)

print("")

print(root.height)