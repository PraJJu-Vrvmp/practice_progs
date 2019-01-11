lst = []
lst.extend(eval(input("enter numbers")))
"""Extends the empty list with elements entered to extend the list(Enter the elements separated by comma)"""
print(lst)
sum=0
for i in lst:
	sum = sum + i
print(sum)