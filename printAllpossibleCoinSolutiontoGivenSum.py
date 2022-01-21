def printAllSubbaryOfK(arr, k):
    buff = []
    return recursion(arr,buff,0,k,0)
    

def recursion(arr, buff, startIndex, target, sum):
    if sum > target:
        return
    if sum == target:
        print(buff)
        return
    i = startIndex
    while i < len(arr):
        buff.append(arr[i])
        recursion(arr, buff, i, target, sum+arr[i])
        buff.pop()
        i += 1
    


print(printAllSubbaryOfK([1,2,5],5))
