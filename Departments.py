#Define a class ‘Department’ having data members: name_of_hod, total_students and per_of_result. Define overloaded constructors to #initialize and method to display the values of these data members. Input values for two objects and determine whose average #result per student is worse.
class Departments:
        def __init__(self, name_of_hod="Unknown", total_students=0, per_of_result=0.0):
        self.name_of_hod = name_of_hod
        self.total_students = total_students
        self.per_of_result = per_of_result

    def average_result(self):
        if self.total_students == 0:
            return 0
        return self.per_of_result / self.total_students

    def display(self):
        print("HOD Name:", self.name_of_hod)
        print("Total Students:", self.total_students)
        print("Percentage of Result:", self.per_of_result)
        print("Average Result per Student:", self.average_result())


print("Enter details of First Department")
n1 = input("Enter HOD name: ")
t1 = int(input("Enter total students: "))
p1 = float(input("Enter percentage of result: "))

d1 = Departments(n1, t1, p1)

print("\nEnter details of Second Department")
n2 = input("Enter HOD name: ")
t2 = int(input("Enter total students: "))
p2 = float(input("Enter percentage of result: "))

d2 = Departments(n2, t2, p2)


print("Department with worse average result per student:")

if d1.average_result() < d2.average_result():
    d1.display()
elif d2.average_result() < d1.average_result():
    d2.display()
else:
    print("Both departments have equal average result.")
