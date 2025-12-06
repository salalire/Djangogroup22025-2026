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
operator=input("Enter opreator for your operation you want to perform in the above two numbers")
if operator=="+":
    print("The addition result is ",add(x,y))
elif operator=="*":
    print("The multplication result is ",multiply(x,y))
elif operator=="/":
    print("The division result is ",divide(x,y))
elif operator=="-":
    print("The subtraction result is ",subtract(x,y))
else:
    print("Invalid operator")
      
      
      
      
