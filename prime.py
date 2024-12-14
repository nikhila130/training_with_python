n=int(input("enter number:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
        if(count>2):
            print("not prime")
        else:
            print("prime")


""" this is another method to find a prime number:
n=int(input())
flag=0
for i in range(2,n):
if(n%i==0):
flag=1
break
if flag==1:
print("not prime")
else:
print("prime")
"""

''' another method:
n=int(input())
flag=0
for i in range(2,(n//2)+1):
if n%i==0:
flag=1
break
if flag==1:
print("npt prime")
else:
print("prime")
'''

'''amother method:
 n=int(input())
flag=0
for i in range(2,int(n**0.5)+1):
if n%i==0:
flag=1
break
if flag==1:
print("npt prime")
else:
print("prime")

'''