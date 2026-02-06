class Marks:
    def __init__(self):
        self.n = int(input("Enter number of students: "))
        self.markList = []
        for i in range(self.n):
            mark = int(input("Enter marks: "))
            self.markList.append(mark)
    def marks(self):
        first_class = 0
        second_class = 0
        pass_count = 0
        fail_count = 0
        for mark in self.markList:
            if 90 < mark <= 100:
                first_class += 1
            elif 80 < mark <= 90:
                second_class += 1
            elif mark >= 35:
                pass_count += 1
            else:
                fail_count += 1
        total_pass=first_class+second_class+pass_count
        print("Total first class students:", first_class)
        print("Total second class students:", second_class)
        print("Total pass students:", total_pass)
        print("Total fail students:", fail_count)
if __name__ == "__main__":
    obj = Marks()
    obj.marks()
