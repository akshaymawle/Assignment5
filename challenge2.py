#Challenge 2: Implement a Calculator Class
class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num2 - self.num1

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        # Ensure num1 is not zero to avoid division by zero
        if self.num1 != 0:
            return self.num2 / self.num1
        else:
            return "Cannot divide by zero"

calculator_instance = Calculator(10, 94)
print(calculator_instance.add())       
print(calculator_instance.subtract()) 
print(calculator_instance.multiply())   
print(calculator_instance.divide())     
