n=int(input("Enter number:::"))
num=n
power=len(str(num))
sum=0
while num>0:
	digit=num%10
	sum=sum+(digit**power)
	num=num//10
if n==sum:
	print(f"{n} is Armstrong number!!")
else:
	print(f"{n} is not armstrong number!!")
	
	
	