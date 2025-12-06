def factorial(number):
    if number==1 or number==0:
        return number
    else:
        return number*factorial(number-1)



number=int(input("Enter number:"))
if number<0:
    print("Factorial is not defined for negative numbers")
else:
    print("The factorial of",number,"is",factorial(number))
        
