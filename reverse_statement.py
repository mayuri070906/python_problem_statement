# input
# "Sky is blue"
# output
# "blue is Sky"

str1="Sky is blue"
mylist=str1.split()
mylist=mylist[::-1]
str2=" ".join(mylist)
print(str2)


# str1="Sky is blue"
# print(" ".join(str1.split()[::-1]))