def addlist(lst,n):
	sum = 0
	for i in range(0,n):
		sum = sum + lst[i]
	print(sum)
lst1 = []
n = eval(input("Enter the no. of elements:"))
for i in range(0,n):
	el = eval(input("Enter the %d element:"%(i+1)))
	lst1.append(el)
print(lst1)
addlist(lst1,n)