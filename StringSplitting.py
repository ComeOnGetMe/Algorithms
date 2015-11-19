# Ex 6.9 in Book: Algorithm, S.Dasgupta, C.H.Papadimitriou, 2006
# Writer: Alan Yan
# Date: Nov 17th, 2015
# Test sample: ./stringsplitting.in

[m,n]=map(int,raw_input().split(' '))
cut = map(int,raw_input().split(' '))
cut.sort()
cut=[0]+cut+[n]
d=[[0]*(m+2) for i in xrange(m+2)]

for i in xrange(2,m+2):
    for j in xrange(m+2-i):
        d[i+j][j]=min([d[k][j]+d[i+j][k] for k in xrange(j+1,i+j)])+cut[i+j]-cut[j]
    print d
#print d[m+1][0]
