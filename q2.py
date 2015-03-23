#threes
#functions:
def find_threes(l):
    a=0 #acumulate
    for i in (l):
        if ((i%3)==0):
            a=a+i
    return(a)
#code:
x=[0,1,2,3,4,5,6,7,8,9,10,30]
res= find_threes(x)
print("the sum of all the multiples of 3 in:",x," is: ",res)
