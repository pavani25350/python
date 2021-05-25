s=[]
def fun():
    def primenum(x,y):
        if x==1:
            x=2
        for i in range(x,y+1):
            for j in range(2,i):
                if i%j==0:
                    break
            else :
                s.append(i)
        return s
    def cond1(pr):
        if len(pr)>=2:
            value=max(pr)-min(pr)
        elif len(pr)==1:
            value=0
        elif len(pr)==0:
            value=-1
        print("diff is",value)
    a,b=map(int,input().split())
    pr=[]
    pr=primenum(a,b)
    print(pr)
    cond1(pr)

fun()
            
