dict = {1:"Speckbit", 2:"World", 3:"Quiet"}
srch = input("Enter the word to be searched:")
for key in dict:
	if dict[key] == srch:
		print ("Key is %d"%key)