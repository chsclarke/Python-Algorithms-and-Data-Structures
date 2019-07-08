#Reverse an integer:
n = 12345
rev=0   
while(n>0):
    dig=n%10 #gets last digit
    rev=rev*10 + n%10 #adds a power of ten and sets equal to last digit
    n=n//10
print(n, " reversed ", rev)

#Reverse a string:
print("hello world reversed ", 'hello world'[::-1])

#queue
queue = []
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
queue.pop(0)
# >>> 1
queue
# >>> [2, 3, 4, 5]

#stack
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
stack.pop(0)
# >>> 5
stack
# >>> [1, 2, 3, 4]

# max depth bst. recursive DFS approach
def dfs(root, depth):
    if root is None: return depth
    return max (dfs(root.right, depth + 1), dfs(root.left, depth + 1))
return dfs(root, 0)
