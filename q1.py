#triangles
#functions:
def triangles(x):
    for i in range(1,x):
        print("T"*i) #first half
    for i in range(x,0,-1):
        print("T"*i) #2nd half
#code:
z=int(input("give me the size of the triangle: "))
triangles(z)
