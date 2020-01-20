def findDiagonalDifference(arr,n):
    sumLeft = 0
    sumRight = 0
    for i in range (0, len(arr)):
        sumLeft += arr[i][i]
        sumRight += arr[n-1-i][i]
    return abs(sumLeft - sumRight)

arr = [[1,2,3],[4,5,6],[9,8,9]]
print (findDiagonalDifference(arr,3))