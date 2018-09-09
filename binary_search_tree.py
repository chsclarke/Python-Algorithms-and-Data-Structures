# -*- coding: utf-8 -*-
"""
This is an example of a BST implimented in python 3.
Copyright 2018 Chase Clarke cfclarke@bu.edu
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.parent = None

class BST:
    def __init__(self, rootNode):
        self.root = rootNode

    def insert(self, key, currentNode):
        insertNode = Node(key)
        insertNode.parent = currentNode

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

    """inorder traversal of tree"""
    def printTree(self, root):

        if(root.leftChild is not None):
            self.printTree(root.leftChild)

        print(root.data)
        
        if (root.rightChild is not None):
            self.printTree(root.rightChild)


root = Node(8)

MyBST = BST(root)

lst = [6, 1, 13, 14, 4, 7, 3, 14, 10]

for i in lst:
    MyBST.insert(i, root)

MyBST.printTree(root)