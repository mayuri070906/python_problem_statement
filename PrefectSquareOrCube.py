count=0
for i in range(1,1001):
	root=round(i**(1/6))
	if root**6==i:
		count+=1
print(f"prefect square or cube are same count::{count}")
