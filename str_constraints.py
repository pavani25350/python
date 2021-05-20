#print("Hello world")
def fun():
    def check_len(inp):
        if len(inp)<=30:
            return inp
        else :
            return input("Enter a string with length less than 30")
    def con1(inp):
        count=0
        a=len(inp)
        s=['a','e','i','o','u','A','E','I','O','U']
        if inp[0] not in s and inp[a-1] not in s:
            print("con1 statisifies")
            for i in range(1,a-1):
                if inp[i] in s:
                    count+=1
            if count==1:
                print("Yes")
            else :
                print("No")
    a=check_len(input())
    con1(a)
fun()
            
    
