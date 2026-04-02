#Accept names of your six friends as input. Append their surname with it 
#afterwards, reverse their names and display all.
list1 = []
for i in range(6):
    name = input("Enter names: ")
    list1.append(name)

list2 = []
for i in list1:
    surname = input("Enter surname: ")
    full_name = i + " " + surname
    list2.append(full_name)

list3 = []
for i in list2:
    rev_name = i[::-1]
    list3.append(rev_name)

print("Reversed names:", list3)


	
