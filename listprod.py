lst = []
lst.extend(eval(input("enter numbers")))
"""Extends the empty list with elements entered to extend the list(Enter the elements separated by comma)"""
print(lst)
prod=1
for i in lst:
	prod = prod * i
print(prod)