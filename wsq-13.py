#Babylonian Metoth sqrt.
#functions:
def Baby(x):
    ans=x
    y=0
    while (ans!=y):
        y=ans
        ans=(x/ans+ans)/2
    return ans

#code:
print("this program calculates the sqrt of a number using Babylonian Metoth")
n=int(input("give me the number: "))
ans=Baby(n)
print("the sqrt of: ",n," is: ",ans)
