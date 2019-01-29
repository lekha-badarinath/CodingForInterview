def simple():
    num = int(input())
    arr = [int(x) for x in raw_input().split()]
    if len(arr) != 1:
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] != 1:
                arr.insert(arr[i],arr[i]+1)
                print (arr[i]+1)
    if len(arr) != num:
        print (arr[-1]+1)
#simple()    

#---------------------------------------------------------------------------------------------------------------------------
def missingSum():
    for test in range(int(input())):        
        num_of_elements = int(input())
        arr = [int(x) for x in raw_input().split()]
        sets = set()
        for i in range(len(arr)-1):
            difference = arr[i+1]-arr[i]
            if difference not in sets:
                sets.add(difference)
            else:
                diff_of_sequence = difference
        
        for j in range(len(arr)-1):
            diff = arr[j+1]-arr[j]
            if diff != diff_of_sequence:
                missing_num = arr[j]+diff_of_sequence
        print (missing_num)
        
        #=======================================================================
        # if len(arr) != num_of_elements:
        #     arr.append(arr[-1]+diff)
        #     print (arr)
        #=======================================================================

missingSum()