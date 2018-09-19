import collections

def getCloser(inpChar):
    if inpChar == '(':
        return ')'

    if inpChar == ')':
        return '('

    if inpChar == '[':
        return ']'

    if inpChar == ']':
        return '['

    if inpChar == '{':
        return '}'

    if inpChar == '}':
        return '{'


def isBalanced(stack):

    openChars = ['(','{','[']

    closeChars = [')','}',']']

    tmpstack = collections.deque([])
    for i in stack:

        if i in openChars:
            print("adding", i, "to tmpstack")
            tmpstack.append(i)

        elif i in closeChars and len(tmpstack):
            print(tmpstack)
            tmp = tmpstack.pop()
            if getCloser(i) != tmp:
                print(i,"not equal to", tmp)
                return False

        elif not len(tmpstack) and i in closeChars:
            return False
    

    if(len(tmpstack)):
        return False
    
    return True
                


if __name__ == '__main__':
    inputChars = collections.deque(['{','d','(','a','b',')','}'])

    print(isBalanced(inputChars))