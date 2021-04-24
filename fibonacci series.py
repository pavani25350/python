a=0
b=1
print("Fibnacci Series")
N=int(input("Enter a number"))
print(a)
print(b)
if N<=0:
    print("Enter a positive Number & try again")
elif N>0:
    for i in range(2,N):
        c=a+b
        print(c)
        a=b
        b=c
        
        
    
