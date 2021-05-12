
def fun():
    def Nvalue(inp):
        if inp>=4 and inp<=10**5:
            return inp
        else :
            pass
    def element(inp):
        if inp>=1 and inp<=10**4:
            return inp
        else:
            pass
    def abs_min_max(size,values ):
        from itertools import islice
        list_len=len(values)
        length_to_split=[1,1,1,list_len-3]
        Input=iter(values)
        output= [list(islice(Input,elem))
                 for elem in length_to_split]
        print("split length list:",length_to_split)
        print("List after splitting:",output)
        s=sum(output[-1])
        for i in range(1,len(output[-1])+1):
            values[-i]=s
        print(values)
        print("difference is ",max(values)-min(values))
    a=Nvalue(int(input("enter the size of array")))
    arr_val=[]
    arr_val2=[]
    for i in range(a):
             arr_val.append(int(input()))
    print(arr_val)
    for i in arr_val :
             arr_val2.append(element(i))
    print(arr_val2)
    abs_min_max(a,arr_val2)
fun()




"""you are given an array A of N elements.You divide this array into 4-nonempty sublists B,C,D,E by making 3 cuts to it. 
Let P,Q,R,S be the sum of elements in the new array B,C,D,E.your task is to find out minimum possible absolute
difference of the (maximum and the minimum among P,Q,R,S)."""
