def fun():
    def no_cust(inp):
        if inp>=1 and inp<=3*10**3 :
            return inp
        else :
            return int(input("Enter number in given range"))
    def Happy_quotient(inp):
        if inp>=1 and inp<=3*10**3:
            return inp
        else :
            return int(input("Enter Happiness Quotient in given range"))

    def restuarant(Nval,H_quo):    
        j=1
        i=0
        sum_val=0
        p=0
        while p<len(H_quo):
            sum_val=sum_val+abs(H_quo[i]-j)        
            i=i+1                                  
            j=j+1
            p+=1
        print("The unhappiness sum is",sum_val)


    N=int(input("Enter integer value"))
    no_cust(N)
    cust=[]
    arr1=[]
    for i in range(N):
        cust.append(int(input()))
    print("Happiness quotient of customers",cust)
    for j in cust:
        Happy_quotient(j)
    restuarant(N,cust)
    
fun()        
