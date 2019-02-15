'''
Created on Feb 15, 2019

@author: LB064195
'''
from __future__ import print_function
from collections import defaultdict

dic = defaultdict(list)
mList = []
n,m = [int(x) for x in raw_input().split()]
for i in range(1,n+1):
    dic[raw_input()].append(i)

for i in range(m):
    mList.append(raw_input())

for i in mList:
    if i in dic:
        for j in dic[i]:
            print(j, end=" ")
        print("")
    else:
        print(-1)
        
