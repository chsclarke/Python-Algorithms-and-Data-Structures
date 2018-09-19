import collections


class Node:
    #node class for building tree
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.height = 1
        self.balance = 0

  
def getHeight(root):
    #returns the height of the tree using a DFS traversal
    currentDepth = 1
    queue = collections.deque([(root, 1)])

    while queue:
        vertex, depth = queue.pop()

        #checking if at deepest depth
        if currentDepth < depth:
            currentDepth = depth

        #checking if leaf node to avoid errors in for loop
        if not vertex:
            break

        if vertex.left:
            queue.append((vertex.left, depth + 1))
        if vertex.right:
            queue.append((vertex.right, depth + 1))

    return currentDepth




def getNodesAtDepth(root, k):
    #returns nodes a kth depth using BFS traversal
    queue = collections.deque([(root, 1)])
    nodeList = []

    while queue:
        vertex, depth = queue.popleft()

        #checking if at deepest depth
        if depth == k:
            nodeList.append(vertex.data)

        #checking if leaf node to avoid errors in for loop
        if not vertex:
            break

        if vertex.left:
            queue.append((vertex.left, depth + 1))
        if vertex.right:
            queue.append((vertex.right, depth + 1))

    return nodeList


def printAncestors(root, target): 
    # recurisve inorder call of BT that finds target
    # then moves up the recursion stack printing ancestors

    # Base case
    if root == None: 
        return False 
      
    if root.data == target: 
        return True 

    # If target is present in either left or right subtree  
    # of this node, then print this node 
    if (printAncestors(root.left, target) or 
        printAncestors(root.right, target)): 
        print (root.data,) 
        return True
  
    # Else return False  
    return False

if __name__ == '__main__':
    root = Node(5)
    left = Node(4)
    right = Node(6)
    root.left = left
    root.right = right
    left.left = Node(3)

    print("depth:", getHeight(root))

    print("nodes at kth depth: ", getNodesAtDepth(root, 2))

    print("ancestors of 3:", printAncestors(root, 3))