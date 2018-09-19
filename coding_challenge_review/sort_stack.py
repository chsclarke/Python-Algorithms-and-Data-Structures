
import collections

def sortStack(stack):
    tmpstack = collections.deque([])

    while (len(stack)):

        #pop is stack, popleft is queue
        tmp = stack.pop()        

        #for stack, top is end of list. for queue, top is beginging of list
        while(len(tmpstack) and tmpstack[len(tmpstack) - 1] > tmp):
            stack.append(tmpstack.pop())

        tmpstack.append(tmp)

    return tmpstack


if __name__ == '__main__':
    unsortedStack = collections.deque([1,5,3,6,4,2])
    sortedStack = sortStack(unsortedStack)

    print(sortedStack)


