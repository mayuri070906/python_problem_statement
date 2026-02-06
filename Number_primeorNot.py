n=int(input("Enter number::"))

if n<=1:
	print("Number is not prime number!!")
count=0
for i in range(2,int(n**0.5)+1):
	if n%i!=0:
		continue
	count+=1
if count==0:
	print(f"{n} is prime number")
else:
	print(f"{n} is not prime number")