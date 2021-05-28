class usermaincode(object):
    def marathon(cls,N,top_sc,s):
        sum1=0
        s.sort()
        for i in range(1,top_sc+1):    
            sum1+=s[-i]    
        return sum1
N=int(input("Enter number of attendies"))
top_sc=int(input("Enter number of top scorers"))
s=[]
print("List elements are")
for i in range(N):
    s.append(int(input()))
print(s)
obj1=usermaincode()
print(obj1.marathon(N,top_sc,s))




""" N number of people participated in a coding marathon and are asked to solve some problems.Each carried 1 mark
Total marks each person achieved were calculated .You have to calculate the sum of the marks of top K scorers from the list"""
