listOne = ['a','b','c']
listTwo = [1,2,3]

obj = {}

for i in range(len(listOne)):
    obj[listOne[i]] = listTwo[i]

print (obj)

