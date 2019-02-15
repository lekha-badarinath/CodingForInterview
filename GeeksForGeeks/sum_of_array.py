arr = [1,2,3,4,7,5]#N-1 tests
num = 12
curr_sum = arr[0]
start = 0
n = 6
for i in range(0,len(arr)-1):
    for j in range(1,len(arr)-1):
        curr_sum = arr[i] + arr[j]
        if curr_sum == num:
            print (arr[i],arr[j])
    
        
        
    