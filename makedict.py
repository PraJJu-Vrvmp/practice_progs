n = eval(input("Enter the no. of dictionary keys:"))
lst1 = []
lst2 = []
for i in range(n):
	k = input("Enter %d key:"%(i+1))
	v = input("Enter %d value:"%(i+1))
	lst1.append(k)
	lst2.append(v)
d = dict(zip(lst1,lst2))
print(d)
