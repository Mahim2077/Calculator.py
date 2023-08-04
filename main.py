#please try the code in a python IDE
def factorial(input_number):
    if input_number == 0:
        return 1
    else:
        return input_number * factorial(input_number - 1)
        ###
print("Methods available: Addition(+), Substraction(-), Multiplication(*), Division(/), power(^), root(#^) and factorial(!). ")
        ###
def calculator():
    input_method = (input("Please enter what you want to do:"))
    if input_method == '+':
        first_input = float(input("Please enter a number:"))
        second_input = float(input("Please enter another number:"))
        print("The answer is:", first_input + second_input)
    if input_method == "-":
        first_input = float(input("Please enter a number:"))
        second_input = float(input("Please enter another number:"))
        print("The answer is:", first_input - second_input)
    if input_method == '*':
        first_input = float(input("Please enter a number:"))
        second_input = float(input("Please enter another number:"))
        print("The answer is:", first_input * second_input)
    if input_method == '/':
        first_input = float(input("Please enter a number:"))
        second_input = float(input("Please enter another number:"))
        if second_input == 0:
            print("Math error.")
        else:
            print("The answer is:", first_input / second_input)
    if input_method == '^':
        first_input = float(input("Please enter a number:"))
        if first_input < 0:
            try:
                second_input = int(input("Please enter power:"))
            except ValueError:
                print("Math error.")
            else:
                print("The answer is",first_input ** second_input)
        else:
            second_input = float(input("Please enter power:"))
            print("The answer is:", first_input ** second_input)
    if input_method == "#^":
        first_input = float(input("Please enter a number:"))
        second_input =(input("Please enter another number(integers only):"))
        try:
            second_input = 1 / int(second_input)
            if first_input <= 0 and second_input == 1:
                print("The answer is", first_input ** second_input)
            elif first_input >= 0:
                print("The answer is", first_input ** second_input)
            else:
                print("Math error.")
        except ValueError or TypeError:
            print("Only integer numbers are executable.")
    if input_method == "!":
        factorial_input = (input("Please enter a number(integers only):"))
        try:
            factorial_input = int(factorial_input)
            print("The answer is:",factorial(factorial_input))
        except ValueError or TypeError:
            print("Only integer numbers are executable.")

calculator()
while True:
    y_or_n = input("Do you want to operate again?(y) or (n) :")
    if y_or_n == "y":
        calculator()
    else:
        break
print("Program finished.")


