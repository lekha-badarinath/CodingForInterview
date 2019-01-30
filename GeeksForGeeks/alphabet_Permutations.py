#Question - https://practice.geeksforgeeks.org/problems/permutations-of-a-given-string/0/?ref=self
#arrays #list #strings #permutationsOfStrings #usingItertools

from itertools import permutations

def per():
    for test in range(int(input())):
        input_str = input()
        st = str("".join(sorted(input_str)))
        permList = permutations(st)
        for i in list(permList):
            new_st = str("".join(i))
            print (new_st,end = ' ')
        print ("")
    
per()