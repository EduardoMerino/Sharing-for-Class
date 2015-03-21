#functions:
def gcd(x,y):
    if (x==y):
        ans=x
    else:
        if(x>y):
            ans=gcd((x-y),y)
        else:
            ans=gcd(x,(y-x))
    return ans
#code:
print("I will give you the Greatest Common Divisor of two int. numbers")
a=int(input("give me the first number: "))
b=int(input("give me the second number: "))
rgcd= gcd(a,b)
print("the Greatest Common Divisor of ",a," and ",b," is: ",rgcd)
