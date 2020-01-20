import string

def findGreatest(n) :
    for i in range(n+1) :
        sample = [x for x in input()]
        newDict = {}
        highest = []
        for cha in set(sample):
            newDict[cha] = 0
        for cha in sample:
            newDict[cha] += 1
        val = max(list(newDict.values()))

        for k,v in newDict.items() :
            if v == val:
                highest.append(k)

        if len(highest) > 1:
            highest = map(lambda x: ord(x), highest)
            print (chr(min(highest)))
        else:
            print (highest[0])


findGreatest(2)