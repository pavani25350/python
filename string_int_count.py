str1=input()
a=list(str1)
s=[]
p=[]
print(a)
for i in range(len(a)):
    if a[i].isalpha():
        continue
    else:
        s.append(a[i])
print(s)
for i in range(len(s)):
    p.append(s.count(s[i]))
if s.count(s[i])== max(p):
    print(s[i])




"""Given a string , return the most occurring integer value present in the string
Example , string="pav1wdb2xbba2"   output:2"""
