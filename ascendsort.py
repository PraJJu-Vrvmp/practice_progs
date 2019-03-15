lst = []
lst.extend(eval(input("Enter elements:")))
for j in range(len(lst)-1):
	for i in range(len(lst)-1):
		if lst[i]>lst[i+1]:
			temp = lst[i]
			lst[i]=lst[i+1]
			lst[i+1]=temp
print(lst)
