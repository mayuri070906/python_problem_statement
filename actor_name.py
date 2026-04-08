#Sort the names of 5 actors in descending order. Identify average length of 
#all names, append a “*” at the end of all names
list1=[]
for name in range(5):
	name=input("Enter name of actor:")
	list1.append(name)
list1.sort(reverse=True)
print("Actors name in descending order:"list1)

total_length=0
for name in list1:
	total_length+=len(name)
avg_len=total_length/5
print("average length of all names:",avg_len)

for i in range(len(list1)):
    list1[i] = list1[i] + "*"

print("Updated names:",list1)
