#Input names of seven sports from keyboard. Display those names starts 
#with “t”, display names ending with “t”, insert character “m” at position 3 
#for all and delete character at position 4 and display all the strings
list1=[]
for i in range(7):
	str=input("enter sports:")
	list1.append(str)

print(list1)
#Display those names starts with “t”,
list2=[]
for sport in list1:
	if sport[0].lower()=='t':
		list2.append(sport)
print(list2)
#display names ending with “t”
list3=[]
for sport in list1:
	if sport[-1].lower()=='t':
		list3.append(sport)
print(list3)
# Insert 'm' at position 3
list4 = []
for sport in list1:
    new_s = sport[:3] + 'm' + sport[3:]
    list4.append(new_s)
print("After inserting m:", list4)

# Delete character at position 4
list5 = []
for sport in list4:
    new_s = sport[:4] + sport[5:]
    list5.append(new_s)
print("After deleting position 4:", list5)
