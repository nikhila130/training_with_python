'''
program to find the sum of digits in a num
n=int(input("enter value"))
def getSum(n): 
   
    sum = 0
    for digit in str(n):  
      sum += int(digit)       
    return sum
print(getSum(n))
'''
n=int(input())
sum=0
flag=0
while(n):
    r=n%10
    sum+=r
    n//=10
    for i in range(2,int(sum**0.5)+1):
        if sum%i==0:
            flag=1
            break
        if flag==1:
            print("not googly")
        else:
            print("googly")

'''
googly num is a num where the sum of digits of a num is equal to prime
'''

