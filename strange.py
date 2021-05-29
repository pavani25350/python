a=0
b=1
print("Fibnacci Series")
N=int(input("Enter a number"))
print(a)
print(b)
s=[0,1]
if N<=0:
    print("Enter a positive Number & try again")
elif N>0:
    for i in range(2,N):
        c=a+b
        s.append(c)
        a=b
        b=c
print(s)
if s[-1]%2==0:
    print("Dead")
else :
    print("Alive")
    
"""offrey has issued orders for Stark's execution. Now, you are trying to predict if Stark will survive or not. You are confident that Stark's survival depends on the Nth fibonacci number's parity. If it is odd you will predict that Stark lives but if it is even you will predict that Stark dies. Given N, print your prediction.
Fibonacci series is a series where,
Fibonacci(1) = 0
Fibonacci(2) = 1
Fibonacci(i) = Fibonacci(i-1) + Fibonacci(i-2); for i > 2
Input
Input Contains a single integer N.

Constraints:
1 <= N <= 1000000 """
