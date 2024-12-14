def fun(n):
    if n==0:
        return 0
    print(n)
    fun(n-1)
    print(n)
x=int(input())
fun(x)



#another fun
def fun(n,m):
    if n==0:
        return 0
    print(m)
    fun(n-1,m+1)
    print(m)
x,y=5,1
fun(x,y)

#another one
def fun(n,m):
    if n==0:
        return 0
    print(m)
    fun(n-1,m+1)
    if (m-1)!=0:
        print(m-1)
x,y=5,1
fun(x,y)



