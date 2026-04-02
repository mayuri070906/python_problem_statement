#Input an array of names of ten cities. Convert them in lower case, check 
#any two of them are equal or not and display first character of all names.

list1=['Sangli','Pandharpur','Goa','Kolhapur','Satara','Solapur','Jath','Kerla','Vijapur','Benglore']
list1=[city.lower() for city in list1]	
found=False
for i in range(len(list1)):
	for j in range(i+1,len(list1)):
		if list1[i]==list1[j]:
			print("Equal cities found",list1[i])
			found=True
if not found:
	print("No equal cities")
list2=[city[0] for city in list1]
print("First characters:",list2)
			