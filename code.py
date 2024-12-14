n=int(input())
x=0
for i in range(n+1):
    x=x^i
print(x)

'''this is bruteforce code it can have a better solution'''

n=int(input())
if n%4==1:
    print(1)
if n%4==2:
    print(n+1)
if n%4==3:
    print(0)
if n%4==0:
    print(n)

'''more optimal sol and its timecomplexity is o(1)'''


'''another method'''
def XoR(n):
    if n%4==1:
        return 1
    if n%4==2:
        return n+1
    if n%4==3:
        return 0
    if n%4==0:
        return n
l=int(input("enter lower limit:"))
r=int(input('enter upper limit:'))
a=XoR(l-1)
b=XoR(r)
c=a^b
print(c)
    