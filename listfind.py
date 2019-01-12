lst = []
str = input("Enter the elements:")
lst = str.split()
print(lst)
srch = input("Enter search element:")
for i in range(len(lst)):
	if srch == lst[i]:
		print(True)
		break
else:
	print(False)
