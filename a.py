'''x=int(input())

def fun(a):
    for i in range(1,x+1):
        print(i)
        i+=1
fun(x)'''

'''now doing it without loop'''

a=int(input("enter:"))
def fun(c):
    print(*range(1,c+1))
fun(a)

'''another method'''
def fun(n):
    if n==0:
        return 0
    fun(n-1)
    print(n)
x=int(input())
fun(x)


'''another method'''
def fun(n):
    if n==0:
        return 200
    print(n)
    t=fun(n-1)
    return t
x=int(input())
print(fun(x))