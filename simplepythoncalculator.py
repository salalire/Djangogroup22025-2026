def add(number1,number2):
      return number1+number2

def multiply(number1,number2):
      return number1*number2

def divide(number1,number2):
      if number2==0:
            print("Division by zero is illegal")
            return
      return number1/number2

def subtract(number1,number2):
      return number1-number2

print("Enter two numbers")
x=int(input("First Number: "))
y=int(input("Second Number: "))
print("The addition result is ",add(x,y))
print("The multplication result is ",multiply(x,y))
print("The division result is ",divide(x,y))
print("The subtraction result is ",subtract(x,y))
      
      
      
      
