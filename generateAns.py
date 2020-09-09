def parseInput(inputStr):
    # get rid of '[' ']'
    inputStr = inputStr[1:-1]

    elements = []    
    curElement = []

    for c in inputStr:
        if c.isdigit() or c == '-' or c == '.':
            curElement.append(c)
        elif c == ' ':
            elements.append("".join(curElement))
            curElement = []
        elif c == ';':
            elements.append("".join(curElement))
            elements.append(';')
            curElement = []
        else:
            print("Invalid input!")
            exit(1)
    
    elements.append("".join(curElement))

    return elements

# back tracking algorithm
def generateCombinations(curIndex, elements, curAns, possibleAns):
    # base case 
    if curIndex >= len(elements):
        possibleAns.append("[" + "".join(curAns) + "]")
        possibleAns.append("[" + "".join(curAns) + " ]")
        return
    
    if len(curAns) == 0 or curAns[-1] != ' ':
        # add a space 
        curAns.append(' ')
        generateCombinations(curIndex, elements, curAns, possibleAns)
        curAns.pop()
    
    if len(curAns) == 0 or elements[curIndex] == ';' or not curAns[-1].replace('.','',1).isdigit():
        # do not add a space
        curAns.append(elements[curIndex])
        generateCombinations(curIndex + 1, elements, curAns, possibleAns)
        curAns.pop()

if __name__ == '__main__':
    ans = input("Please enter the matrix as MATLAB notation without any unnecessary space or commas. E.g. [3;5;6]\n") 

    elements = parseInput(ans)
    possibleAns = []
    generateCombinations(0, elements, [], possibleAns)

    with open('allPossibleAns.txt', 'w') as writer:
        for ans in possibleAns:
            writer.write(ans + "\n")


