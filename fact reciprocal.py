#to print reciprocal of the factorial of given num:
n=int(input())
fact=1
for i in range(1,n+1):
    fact=fact*i
    i-=1
print('1/',fact)
