a=int(input())
s=[]
s_dup=[]
for i in range(a):
  s_dup.append(int(input()))
for i in s_dup:
  if i not in s:
    s.append(i)    
print("Non-duplicate items:")
print(s)
  



   """   Remove the Duplicate
The program takes a lists and removes the duplicate items from the list.

Problem Solution:

Take the number of elements in the list and store it in a variable. Accept the values into the list using a for loop and insert them into the list. Use a for loop to traverse through the elements of the list. Use an if statement to check if the element is already there in the list and if it is not there, append it to another list.
Print the non-duplicate items of the list. Exit.   """
