# car = {"make":"Toyota","model":"Camry","year":2020,"color":"Blue"}
# print(car["model"])


# class BasicCalculator:
#     def __init__(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2
#     def Addition(self):
#         return self.num1 + self.num2
        
#     def Subtraction(self):
#         return self.num1 - self.num2
        
#     def Multiplication(self):
#         return self.num1 * self.num2
        
#     def Division(self):
#         return self.num1 / self.num2
        
# calc = BasicCalculator(10, 5)

# print("Addition:", calc.Addition())
# print("Subtraction:", calc.Subtraction())
# print("Multiplication:", calc.Multiplication())
# print("Division:", calc.Division())



# def GreetUser(username):
#     print(f"Hello, {username}! Welcome to the Python course.")
    
# GreetUser("John")


# def CalculateAverage(num1,num2,num3):
#     return (num1+num2+num3)/3
    
    
# average = CalculateAverage(10,20,30)

# print("The average of ",num1,num2,"and ",num3 ,"is",average)


def CalculateAverage(num1, num2, num3):
    return (num1 + num2 + num3) / 3

# Call the function
average = CalculateAverage(10, 20, 30)

print("Average:", average)