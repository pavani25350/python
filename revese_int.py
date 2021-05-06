def reverse_int(num):
    rev=0
    while num>0:
        digit=num%10
        rev=rev*10+digit
        num=num//10
    if num<0:
        print("enter a positive integer")
    print("Reverse of given integer is",rev)
    
val=int(input("Enter integer value"))
reverse_int(val)
