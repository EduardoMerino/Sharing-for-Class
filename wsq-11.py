#functions
def inv (x): #invert number
    y = str(x)
    y = y[::-1]
    return int(y)
def bec_pali (x): #become palindrome
        ix=x+inv(x)
        if (ix==inv(ix)):
            ans=ix
        else:
            for i in range (31):
                bec_pali(ix)
            else:
                ans=(-1)
        return ans

#code
print("ill tell you the amount of palindroms in a sequence of numbers")
n0=int(input("give the initial number: ")) #initial number
nf=int(input("give the final number: ")) #final number
palindromes=0
non_palindromes=0
for i in range (n0,nf+1):
    y=inv(i)
    if(i==y):
        palindromes=palindromes+1
        print (i)
    else:
        y=bec_pali(i)
        if (y==-1):
            non_palindromes=non_palindromes+1
        else:
            palindromes=palindromes+1
            print(y)
print("in the list of numbers form ",n0," to ",nf," there are: ",palindromes," palindromes and ",non_palindromes," non palindromes numbers.")
