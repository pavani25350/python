a=int(input())
l=[]
for i in range(a):
  l.append(int(input()))
len1=len(l)-1
l[0],l[len1]=l[len1],l[0]
print(l)




"""
Sample Input:

4

23

45

67

89

Sample Output:

[89, 45, 67, 23]"""
