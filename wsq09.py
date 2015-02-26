#funciones#
def factry(n):
    x=1
    r=1
    while(x<n):
        x=x+1 #contador
        r=r*x #acumulador
    return r

#codigo#
res=1
while (res==1):
    num=int(input("Dame un numero: "))
    if(num<0):
        print(num," no es un numero factorial")
    else:
        ans = factry(num)
        print("el factorial de !",num," es: ",ans)
    res=int(input("quieres hacer otro numero? 1=si, 0=no: "))
    if(res!=1 and res!=0):
        print("opcion no valida")
        res=(int(input("intenta de nuevo, 1=si, 0=no: ")))
print("Adios!")
