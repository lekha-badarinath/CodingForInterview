'''
Created on Feb 15, 2019

@author: LB064195
'''
#https://www.hackerrank.com/challenges/collections-counter/problem

n = input()
shoeSize = [int(x) for x in raw_input().split()]
customers = int(raw_input())
profit = 0
for customer in range(customers):
    size,amount =[int(x) for x in raw_input().split()]
    if size in shoeSize:
        profit += amount
        shoeSize.remove(size)
    else:
        continue
print (profit)