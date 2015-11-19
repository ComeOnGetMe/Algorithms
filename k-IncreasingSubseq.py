# Problem: Given a list of numbers, output an increasing subsequence of length 3
# Alan Yan
# Nov, 19

import sys
def subseq(num):
    x=num[0]
    xIndex=0
    y=sys.maxint
    yIndex=[0,0]
    for i in xrange(1,len(num)):
        if num[i] > y:
            return yIndex + [i]
        elif num[i] > x:
            y = min(y, num[i])
            yIndex = [xIndex,i]
        else:
            x = num[i]
            xIndex = i 
    return [-1]

for i in xrange(input()):
    num=map(int,raw_input().split(' '))
    print subseq(num)
