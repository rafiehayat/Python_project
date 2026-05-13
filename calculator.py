class Calculator:
    num=100

    def __init__(self):
        print("I'm calledutoamtically when object is created")

    def getData(self):
        print("I'm executing a method in class")

    # def summation(self):
        
obj = Calculator()
obj.getData()
print(obj.num)
