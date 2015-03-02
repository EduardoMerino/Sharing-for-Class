print("this program will do the sum of al the numbers within an interval set by you")
x=int(input("I will sum all the numbers from: "))
y=int(input("to: "))
xl=x #for the print#
r=0 #r=answer the final number#
while (x<=y):
    r=r+x
    x=x+1
print("the sum of all the numbers from ",xl," to ",y," is: ",r)
