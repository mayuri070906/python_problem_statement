class Student:
	def __init__(self,roll_no,name,course):
		self.roll_no=roll_no
		self.name=name
		self.course=course
	def display(self):
		print(f"Roll No:{self.roll_no}")
		print(f"Name:{self.name}")
		print(f"Course:{self.course}")
if __name__=="__main__":
	students=[]
	for i in range(3):
		print(f"Enter details for student{i+1}:")
		roll_no=int(input("Enter roll no::"))
		name=input("Enter student name::")
		course=input("Enter course name::")
	
		student=Student(roll_no,name,course)
		students.append(student)
	print("student details:")
	for student in students:
		student.display()
