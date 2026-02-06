import math
count=0
for num in range(1,int(math.sqrt(100000))):
	sq=num**2
	square=str(sq)
	palindrome=square[::-1]
	if square==palindrome:
		count+=1
print(f"total count perfect square number is also palindrome number is:{count}")
	