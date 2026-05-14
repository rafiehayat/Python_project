class Calculator:
    num=100

    def __init__(self,a,b):
        self.firstNumber = a
        self.secondNumber = b
        print("I'm calledutoamtically when object is created")

    def getData(self):
        print("I'm executing a method in class")

    def summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num
        
obj = Calculator(3,2)
obj.getData()
print(obj.num)
print(obj.summation())

obj = Calculator(4,5)
obj.getData()
print(obj.summation())


