#functions
def my_sum(l):
    n=0
    r=0
    while n<len(l):
        r=r+(l[n])
        n=n+1
    return r
def my_st(l):
    n=0
    r=0
    while n<len(l):
        r=((l[n])-(my_sum(l))/(len(l)))**2
        n=n+1
    return (r**0.5)


#list
print("this program is about lists, I'll read 10 numbers you give me")
n=1
x1=float(input("give me the first number: "))
nums = [x1]
while(n<10):
    n=n+1
    y=float(input("give me the next number: "))
    nums.append(y)
#answers
rs=my_sum(nums)
rp=(my_sum(nums))/(len(nums))
st=my_st(nums)
print("the sum of those numbers is: ",rs)
print("the avarage of those numbers is: ",rp)
print("the standard deviation of those numbers is: ",st)
