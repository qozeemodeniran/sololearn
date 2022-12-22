# Complete the given code to define a static add() method for the Calculator class, which returns the sum of its parameters. The code takes two numbers as input, and should return their sum using the Calculator class's add() method.

class Calculator:
    #your code goes here
    @staticmethod
    def add(a, b):
        return a + b
        
n1 = int(input())
n2 = int(input())

print(Calculator.add(n1, n2))