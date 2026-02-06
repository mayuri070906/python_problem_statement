count=0
for num in range(10001):
	square=num**2
	palindrome=num[::-1]
	if square==palindrome:
		count+=1
print(f"total count perfect square number is also palindrome number is:{count}")
	