def filter(lst,n):
	lst1 = []
	for i in range(n):
		if i%2 == 0:
			lst1.append(lst[i])
	print(lst1)



lst2 = []
n = eval(input("Enter the no. of elements:"))
for i in range(0,n):
	el = eval(input("Enter the %d element:"%(i+1)))
	lst2.append(el)
filter(lst2,n)