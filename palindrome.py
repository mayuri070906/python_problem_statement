n=int(input("Enter number:"))
num=str(n)
reverse=num[::-1]
if num==reverse:
	print("Entered numbers are palindrome")
else:
	print("Entered numbers are not palindrome")