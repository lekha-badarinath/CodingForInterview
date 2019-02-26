#rotating a 1D array so that the element at pos 0 is moved to pos N-1.
def rotateOne():
    arr = [10,11,12,13] #[11,12,13,10]   
    for i in range(len(arr)-1):
        arr.insert(0,arr[-1])
        del arr[-1]
    print (arr)

def rotateTwo(arr):
    #arr = [10,11,12,13] #[13,10,11,12]
    newArr=[]
    for i in range(len(arr)):
        newArr.insert(i+1,arr[i])
    newArr.insert(0,newArr[-1])
    del newArr[-1]
    print (newArr)
#rotateTwo([1,2,3,4,5,6,7,8])

def rotateThree(arr):
    #arr = [10,11,12,13] #[13,10,11,12]
    newArr = []
    for i in range(len(arr),0,-1):
        newArr.insert(i,arr[i-1])
    newArr[0] = arr[-1]
    print (newArr)
rotateThree([10,11,12,13])
class Classy(object):
    def __init__(self):
        self.items = []
    def addItem(self,item):
        self.items.append(item)
    def getClassiness(self):
        self.dc = {"tophat":2,"bowtie":4,"monocle":5}
        self.classiness = 0
        for i in self.items:
            if i in self.dc:
                self.classiness += self.dc[i]
        return self.classiness
#===============================================================================
# me = Classy()
# print (me.getClassiness())      
# me.addItem("tophat")  
# print (me.getClassiness())
# 
# me.addItem("tophat")
# me.addItem("bowtie")  
# print (me.getClassiness())
#===============================================================================
    