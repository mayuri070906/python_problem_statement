
class Test1:
	def __init__(self,marks1):
		self.marks1=marks1
class Test2:
	def __init__(self,marks2):
		self.marks2=marks2
class Average:
	def __init__(self,t1,t2):
		self.t1=t1
		self.t2=t2

	def average(self):
		avg=(self.t1.marks1+self.t2.marks2)/2
		print(f"Average::{avg}")
if __name__=="__main__":
	m1=int(input("Enter test1 marks:"))
	m2=int(input("Enter test2 marks:"))
	t1=Test1(m1)
	t2=Test2(m2)
	obj_avg=Average(t1,t2)
	obj_avg.average()


