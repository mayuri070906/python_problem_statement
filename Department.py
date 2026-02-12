#Define a class ‘Department’ having data members: name_of_hod,
#total_students and per_of_result. Define appropriate methods to initialize
#and display the values of these data members. Input values for two objects
#and determine whose average result per student is better.
class Department:
	def __init__(self):
		self.name_of_hod=input("Enter name of HOD::")
		self.total_students=int(input("Enter total students of department::"))
		self.per_of_result=float(input("Enter percentage of result::"))
	def average_result(self):
		if self.per_of_result==0:
			return 0
		else:
			return self.per_of_result/self.total_students
	def display(self):
		print(f"HOD name::{self.name_of_hod}")
		print(f"Total students of department::{self.total_students}")
		print(f"percentage of result::{self.per_of_result}")
if __name__=="__main__":
	CSE=Department()
	ENTC=Department()
	print("Information about CSE department::")
	CSE.display()
	print("Information about ENTC department::")
	ENTC.display()
	a1=CSE.average_result()
	a2=ENTC.average_result()
	if a1>a2:
		print("CSE average result per student is better")
	elif a1<a2:
		print("ENTC average result per student is better")
	else:
		print("CSE and ENTC average result per student is same")

