#Define a class ‘Salary’ which will contain data members basic, TA, DA, HRA.
#Write a program using constructors which will initialize these values for
#object. Calculate total salary of the employee using the method.
class Salary:
	def __init__(self,basic):
		self.basic=basic
		self.TA=0
		self.DA=0
		self.HRA=0
	def check(self):
		self.TA=0.10*self.basic
		self.DA=0.15*self.basic
		self.HRA=0.20*self.basic
	def display(self):
		total_salary=self.basic+self.TA+self.DA+self.HRA
		print(f"basic salary::{self.basic}")
		print(f"TA::{self.TA}")
		print(f"DA::{self.DA}")
		print(f"HRA::{self.HRA}")
		print(f"Total salary::{total_salary}")
if __name__=="__main__":
	s=Salary(200000)
	s.check()
	s.display()
	

		