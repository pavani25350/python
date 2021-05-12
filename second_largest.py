a=int(input())
l=[]
for i in range(a):
  l.append(int(input()))
b=l.index(max(l))
l.pop(b)
print(max(l))


"""
Problem Description:

The program takes a list and prints the second largest number in the list.

Input Format:

Input consists of n + 1 integers. First integer corresponds to the size ,
The next n inputs corresponds to the elements in the list."""
