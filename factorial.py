def factorial(N):
    if N==1:
        return N
    else :
        return N*factorial(N-1)
val=int(input("Enter a integer value"))
if val==0:
    print("Factorial of 0 is 1")
elif val<0:
    print("sorry,Factorial doesn't exist for negetive integers")
else :
    result=factorial(val)
    print("Factorial of given integer is",result)

