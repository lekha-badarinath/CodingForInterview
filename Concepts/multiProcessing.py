#multiprocessing creates two different processes/programs

import time
import multiprocessing

square_result = []
def calSquare(arr):  
    global square_result
    for i in arr:
        time.sleep(0.2) #add sleep time so you can go to the task scheduler and see different Python processes running.
        print ("Square - %d " %(i*i))
        square_result.append(i*i)
    print ("Inside the process:",square_result)  
def calCube(arr):   
    for i in arr:
        time.sleep(0.2)
        print ("Cube - %d " %(i*i*i))

if __name__ == '__main__':

    arr = [x for x in range(1,6)]

    mp1 = multiprocessing.Process(target = calSquare, args = (arr,))
    mp2 = multiprocessing.Process(target = calCube, args = (arr,))
    
    mp1.start()
    mp2.start()
    
    mp1.join()
    mp2.join()
    print ("Done")
    print ("Outside the process:",square_result) #this time the square_result will not be populated.
                                    #Since calSquare is a separate process, the memory space allocated will be destroyed 
                                    #once the program finishes running
                                    #Hence, the result will not be available outside the method.
                                