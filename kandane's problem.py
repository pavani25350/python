
a=[]
size=int(input())
print("ENTER THE ARRAY ELEMENTS")
for i in range(size):
    b=int(input())
    a.append(b)
print("The array is",a)
def maxSum(a,size):
    max_so_far =a[0]
    curr_max =a[0]
    for i in range(1,size):
        curr_max=max(a[i],curr_max+a[i])
        max_so_far=max(max_so_far,curr_max)
    return max_so_far
print("maximum sum of subarray is ",maxSum(a,len(a)))
	 











































#taking inpit using fast I/O
