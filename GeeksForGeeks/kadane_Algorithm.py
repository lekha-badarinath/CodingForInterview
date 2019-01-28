#Question Link - https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0
#Concept Link - https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
#Largest Sum
#Contiguous array
def kadaneAlgorithm():
    testcase = int(input())
    for test in range(testcase):       
        size = int(input())
        arr = [int(x) for x in raw_input().split()] #python 2.7 --> raw_input()
        max_ending_here = 0
        max_so_far = min(arr)
        for i in range(0,size):
            max_ending_here = max(arr[i],max_ending_here + arr[i])
            max_so_far = max(max_so_far,max_ending_here)
        print (max_so_far)
kadaneAlgorithm()

#===============================================================================
# Test inputs:
# 3             --> No. of test cases
# 2             -->array length for first test case
# 1,2           -->array inputs,separated by a space 
# 3             -->array length for second test case
# 4,12,15       -->array inputs,separated by a space 
# 4             -->array length for third test case
# -1,12,-4,1    -->array inputs,separated by a space 
#===============================================================================