#https://www.hackerrank.com/challenges/py-collections-namedtuple/problem

from collections import namedtuple

n, col = (int(raw_input()), raw_input().split())
data = namedtuple('data',col)

total = 0
for i in range(n):
    data1 = data(*raw_input().split())
    total += int(data1.MARKS)

print (round(float(total/n),2))