def printAllSubbaryOfK(arr, k):
    count = 0
    buff = [None]*k
    startIndex = 0
    buffIndex = 0
    return recursion(arr, buff, startIndex, buffIndex)

def recursion(arr, buff, startIndex, buffIndex):
    if startIndex > len(arr):
        return
    if buffIndex == len(buff):
        print(buff)
        return
    i = startIndex
    while i < len(arr):
        buff[buffIndex] = arr[i]
        recursion(arr, buff, i+1, buffIndex+1)
        i += 1


print(printAllSubbaryOfK([1,2,3,4,5,6,7],3))