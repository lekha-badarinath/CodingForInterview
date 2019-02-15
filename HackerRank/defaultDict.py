'''
Created on Feb 15, 2019

@author: LB064195
'''
from __future__ import print_function
from collections import defaultdict


n,m = [int(x) for x in raw_input().split()]
nList = list()
mList = list()
dic = defaultdict(list)

for x in range(n):
    nList.append(raw_input())
for x in range(m):
    mList.append(raw_input())

z = 0
for i in mList:
    for j in range(len(nList)):
        if i == nList[j]:
            dic[i].append(j+1)
    if i not in nList:
        dic[i].append(-1)

 
for i in dic.keys():
    for j in dic[i]:
        print (j, end =" ")
    print ("")
