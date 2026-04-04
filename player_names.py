#Input names of five players from keyboard. Display their names from index 
#position 2 onwards; replace all the occurrences of “e” with “a” only if their 
#names starts with letter “s”.

list1 = []
for i in range(5):
    name = input("Enter names of players: ")
    list1.append(name)
print("Names from index 2 onwards:",list1[2:])
list2=[]
for player in list1[2:]:
	if player[0].lower()=='s':
		result=player.replace('e','a')
		list2.append(result)
print("Modified names:",list2)


