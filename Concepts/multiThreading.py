import time
import threading

square_result = []
def calSquare(arr):  
    global square_result
    for i in arr:
        time.sleep(0.2)
        print ("Square - %d " %(i*i))
        square_result.append(i*i)

def calCube(arr):   
    for i in arr:
        time.sleep(0.2)
        print ("Cube - %d " %(i*i*i))

arr = [x for x in range(0,6)]
#create threads out of the methods

threadOne = threading.Thread(target=calSquare, args = (arr,))   #make sure to pass it like this and not calSquare(arr)
threadTwo = threading.Thread(target=calCube, args = (arr,))     #if you do, multi-threading will not happen.

t1 = time.time()
threadOne.start()
threadTwo.start()

threadOne.join()
threadTwo.join()

#before threading - 0.6s, after threading - 0.001s

print ("Time taken-", time.time()-t1)
print ("Result: ",square_result)    #the result gets printed. This whole program is a single process. Memory is shared.    
                                    #So even though the threading has terminated, the memory space alloted the process where the 
                                    #The result is stored is not destroyed.