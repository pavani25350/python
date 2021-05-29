def func(s):
    for i in s:
        if i>=1 and i<=10**9:
            b.append(i)
    return b
def fun2(a):

    for i in range(0,len(a),2):  #4 3 2 1   N=4 N-1=3
        sum2=a[i]+a[i+1]
        sum1.append(sum2)  
    value=max(sum1)-min(sum1)
    print("Minimum difference of strengths is",value)
N=int(input("Enter number of elements"))
s=[]
b=[]
a,sum1=[],[]
sum2=0
print("List elements are")
for i in range(N):
    s.append(int(input()))
print("List is",s)
if N%2==0 and N>=1 and N<=200000:
    b=func(s)
if b:
    fun2(b)


"""Pree says he stole Daenerys' dragons, and would return them to Daenerys only if she can pair the dragons in a peculiar way.
There are N (N is even) dragons, the strength of ith dragon is Ai. She needs to create N/2 pairs of the dragons. The strength of the dragon pair is the sum of the strengths of dragons in the pair. She needs to pair them in such a way that the difference between the strength of dragon pair with maximum strength and the strength of the dragon pair with minimum strength is minimised.

Now, you need to find the minimum difference in strengths if she has paired them correctly.
Input
The first line of the input contains an integer N, the number of dragons.
The second line of the input contains N integers, the strengths of the dragons.


Constraints
1 <= N <= 200000 (so many dragons, huh)
1 <= Ai <= 109 for all values of i
N is divisible by 2 """
