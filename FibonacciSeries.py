class FibonacciSeries:
    def __init__(self):
        self.n = int(input("Enter number:: "))

    def fibonacciSeries(self):
        a, b = 0, 1
        for i in range(self.n):
            print(a, end=" ")
            a, b = b, a + b


if __name__ == "__main__":
    obj = FibonacciSeries()
    obj.fibonacciSeries()
			
