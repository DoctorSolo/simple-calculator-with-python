from options import Calculator

num1 = float(input('Enter a first number: '))
num2 = float(input('Enter a second number: '))

calculator0 = Calculator(num1, 1, num2)
calculator0 = Calculator(calculator0.result, 1, 10)

print(calculator0.result)