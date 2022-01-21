def printAllSubbaryOfK(number):
    buff = [None]*len(number)
    return recursion(number, buff, 0, 0)

def recursion(arr, buff, startIndex, buffIndex):
    if startIndex >= len(arr) or buffIndex == len(buff):
        print(buff)
        return
    letters = getLetters(arr[startIndex])
    if len(letters) == 0:
        return recursion(arr, buff, startIndex+1, buffIndex)
    for eachLetter in letters:
        buff[buffIndex] = eachLetter
        recursion(arr, buff, startIndex+1, buffIndex+1)

def getLetters(digit):
    if digit == 0 or digit == 1:
        return []
    elif digit == 2:
        return ['A','B','C']
    elif digit == 3:
        return ['D','E','F']
    elif digit == 4:
        return ['G','H','I']
    elif digit == 5:
        return ['J','K','L']
    elif digit == 6:
        return ['M','N','O']
    elif digit == 7:
        return ['P','Q','R','S']
    elif digit == 8:
        return ['T','U','V']
    elif digit == 9:
        return ['W','X','Y','Z']

    


print(printAllSubbaryOfK([4,5,6]))
