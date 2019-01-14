m = input("Enter 1st value:")
n = input("Enter 2nd value:")
try:
	a = float(m)
	b = float(n)
	y = a+b
	print(y)
except:
	y=m+n
	if (y.isalpha()==True):
		print(y)
	else:
		print("error")