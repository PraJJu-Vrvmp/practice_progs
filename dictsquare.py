inp = eval(input("Enter the limit"))
lst1 = []
lst2 = []
for i in range(1,inp):
	lst1.append(i)
	lst2.append(i**2)
d = dict(zip(lst1,lst2))
print(d)