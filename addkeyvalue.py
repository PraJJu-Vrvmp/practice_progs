d = {'a':"Hello",'b':"Hey", 3:"Hi"}
lst1 = []
lst2 = []
n = eval(input("Enter the no. of additional entries:"))
for i in range(n):
	k = input("Enter %d key:"%(i+1))
	lst2.append(input("Enter the %d value:"%(i+1)))
for key in d:
	if k!=key:
		lst1.append(k)
d1 = dict(zip(lst1,lst2))
d.update(d1)
print(d)