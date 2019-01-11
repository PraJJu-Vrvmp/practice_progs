lst = []
lst.extend(eval(input("Enter elements")))

for i in range(len(lst)-1):
	if lst[i]>lst[i+1]:
		lst[i],lst[i+1]=lst[i+1],lst[i]
print(lst)
