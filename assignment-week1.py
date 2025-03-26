# Instructions:

# Basic Calculator Program

# Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
# Perform the operation based on the user's input and print the result.
# Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.



# Note: Upload the code to GitHub and submit the GitHub link

x = int(input("Enter your first number: "))
y = int(input("Enter your second number: "))
math_operator = input("Enter the mathematical operation (+,-,*,/): ")
if math_operator == "+":
    sum = x + y
    print("The resulting solution is: " + str(sum ))
elif math_operator == "-":
    difference = x - y
    print("The resulting solution is: " + str(difference))
elif math_operator == "*":
    product = x * y
    print("The resulting solution is: " + str(product))
elif math_operator == "/":
    division = x / y
    print("The resulting solution is: " + str(division))
