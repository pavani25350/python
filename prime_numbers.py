def prime_numbers(max_val):
    count=0
    for num in range(1,max_val+1):
        if num>1:
            for i in range(2,num):
                if num%i==0:
                    break
            else :
                print(num)
max1=int(input("enter the limit to list prime numbers in that range"))
print("Prime numbers in given range are")
prime_numbers(max1)
                
            
    
