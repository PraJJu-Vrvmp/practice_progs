lst1 = []
lst2 = []
lst1.extend(eval(input("Enter the elements of list1:")))
lst2.extend(eval(input("Enter the elements of list2:")))
print(lst1)
print(lst2)
for i in range(len(lst1)):
	for j in range(len(lst2)):
		if (lst2[j] == lst1[i]):
			print(True)
