# concatinations in lists
# l1=[10,19,28,37,'Hello']
# l2=[45,35,37,'Bye']
# print(id(l1+l2))
# print(id(l1))
# print(id(l2))


# multiplication of lists.

# l1=[10,19,28,37,'Hello']

# print(l1*3)


# iteration through list

# l1=[10,19,28,37,'Hello']
# for item in l1:
#     print(item,end=" ")

# membership of list
# l1=[10,19,28,37,'Hello']
# print(11 in l1)

# deletion of list
# l1=[10,19,28,37,'Hello']
# print(l1)
# del l1
# print(l1)

# length of list

# l1=[12,12.3,35,56,'mayuri',[1,2,3,4]]
# # print(len(l1))
# count=0
# for i in l1:
#     count+=1
# print(count)

# get lergest item in a list
# l1=[15,36,78,65,39]
# print(max(l1))

# maximum=l1[0]
# for i in l1:
#     if i>maximum:
#         maximum=i
# print(maximum)

# Name=['mayuri','shravani','vaibhavi','shweta','radha']
# print(max(Name,key=len))
# print(max(Name))

# get minimum item in a list
# l1=[15,36,78,65,39]
# print(min(l1))

# minimum=l1[0]
# for i in l1:
#     if i<minimum:
#         minimum=i
# print(minimum)

# Name=['mayuri','shravani','vaibhavi','shweta','radha']
# print(min(Name,key=len))
# print(min(Name))

# append() function in list
# l1=[12,3,4,5,3,55,3,2,4,4234,13,13,131,2,4433,54]
# l1.append(34)
# print(l1)

# l2=[]
# for i in range(3):
#     name=input()
#     l2.append(name)
# print(l2)

# extend() function in list
# lang1=['marathi','hindi','english','gujarati']
# lang2=['urdu','franch','japani']
# for i in lang2:
#     lang1.append(i)
# print(lang1)

# lang1=['marathi','hindi','english','gujarati']
# lang1.extend(['urdu','franch','japani'])
# print(lang1)

# insert( function in list
# l1=[1,3,4,5]
# l1.insert(1,2)
# print(l1)

# remove function in list
# cart=['mobile','earphone','laptop','microphone']
# cart.remove('mobile')
# print(cart)

# pop() function in list
# cart=['mobile','earphone','laptop','microphone']
# print(cart.pop(1))
# print(cart)

# clear() function in list
# cart=['mobile','earphone','laptop','microphone']
# cart.clear()
# print(cart)

# del keyword in list
cart=['mobile','earphone','laptop','microphone']
del cart[0]
print(cart)
del cart
print(cart)





