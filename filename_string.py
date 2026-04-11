#Accept the names of 5 films from keyboard. Display the names starting 
#with “k” ending with “a” display substring of all from 1st to 3rd position 
#and find last occurrence of “e” for all the names.
file_names=[]
for i in range(5):
	filename=input("Enter file names:")
	file_names.append(filename)
new_filename_list=[]
for filename in file_names:
	if filename[0].lower()=='k' and filename[-1].lower()=='a':
		new_filename_list.append(filename)
print(new_filename_list)
print(file_names[0:3])
new_filename_list1=[]
for filename in file_names:
	pos = filename.lower().rfind('e')
print(filename, "->", pos)
		


