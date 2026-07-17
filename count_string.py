# input 
# str_1="a,a,a,b,b,c,c,c"
# output
# a=3,b=2,c=3

str_1="a,a,a,b,b,c,c,c"
mylist=str_1.split(',')
visited=[]
final_list=[]
for ch in mylist:
    if ch not in visited:
        final_list.append(f"{ch}={mylist.count(ch)}")
        visited.append(ch)
print(",".join(final_list))


