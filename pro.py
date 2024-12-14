'''question is the same as codeforces 617 a problem...
the difference is that here we can only take one step or the m no.of steps and not inbetween'''


x,m=map(int,input().split())
if x<m:
    print(1)
elif (x%m==0):
    print(x//m)
else:
    print((x//m)+x%m)