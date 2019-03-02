class Element():                    #Creating a container for linked list
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList():                 
    def __init__(self,head = None): #Creating head of the linked list
        self.head = head
    
    def atBeginning(self,beginning):
        beginningNode = Element(beginning)
        
        beginningNode.next = self.head
        self.head = beginningNode
    
    def atEnd(self,end):
        endNode = Element(end)
        if self.head is None:
            self.head = endNode
        last = self.head
        while last.next:
            last = last.next
        last.next = endNode

    def printVal(self):
        printVal = self.head
        while printVal is not None:
            if printVal.next is not None:
                print (printVal.value)
                printVal = printVal.next
    



node0 = LinkedList()                
node0.head = Element(11)            #Inserting the first element to the head of the LL
node1 = Element(12)
node2 = Element(15)
node3 = Element(14)

print (node1.next)

node0.head.next = node1             #Connecting the head to the next value
node1.next = node2
node2.next = node3
node0.atBeginning(10)
node0.atBeginning(9)
node0.atEnd(20)
print (node0.head.value,node0.head.next)
print (node0.printVal())
