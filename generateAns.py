def parseInput(inputStr):
    # get rid of leading '[' and trailing ']'
    inputStr = inputStr[1:-1]
    
    elements = []    
    curElement = []

    for c in inputStr:
        # '-' for negative number
        # '.' for floating point number
        if c.isdigit() or c == '-' or c == '.': 
            curElement.append(c)
        # entries in the same row are separated by one space
        elif c == ' ':
            elements.append("".join(curElement))
            curElement = []
        # entries in the different rows are separated by ';'
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
def generateCombinations(curIndex, elements, curCombination, possibleAns):
    '''
    curIndex - the current index of the element that is being processed
    elements - a list of elements got from parseInput()
    curCombination - a list of elements as the current combination
    possibleAns - a list storing all possible combinations
    '''
    # base case 
    if curIndex >= len(elements):
        possibleAns.append("[" + "".join(curCombination) + "]")
        possibleAns.append("[" + "".join(curCombination) + " ]")
        return
    
    # case 1: can add a space  
    if len(curCombination) == 0 or curCombination[-1] != ' ':
        curCombination.append(' ')
        generateCombinations(curIndex, elements, curCombination, possibleAns)
        curCombination.pop()
    
    # case 1: cannot add a space. Add the next element
    if len(curCombination) == 0 or elements[curIndex] == ';' or not curCombination[-1].replace('.','',1).isdigit():
        curCombination.append(elements[curIndex])
        generateCombinations(curIndex + 1, elements, curCombination, possibleAns)
        curCombination.pop()

if __name__ == '__main__':
    ans = input("Please enter the matrix as MATLAB notation without any unnecessary space or commas. E.g. [3;5;6]\n") 

    elements = parseInput(ans)
    possibleAns = []
    generateCombinations(0, elements, [], possibleAns)

    with open('allPossibleAns.txt', 'w') as writer:
        for ans in possibleAns:
            writer.write(ans + "\n")


