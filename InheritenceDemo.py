from calculator import Calculator


class Inhheritance(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self,2,10)

    def getCompleteData(self):
        return self.num + self.num2 + self.summation()
    
obj = Inhheritance()
print(obj.getCompleteData())