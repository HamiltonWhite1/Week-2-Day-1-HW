###Excerise #1: create a calculator using functions that asks for two numbers and performs a calculation that the user inputs.
###Loop until the user chooses not to perform any more calculations

def user_calculator():
    a_num = int(input("Please input your first number: "))
    b_num = int(input("Please input your second number: "))
    desired_calculations = {"ADDITION":a_num+b_num , "SUBTRACTION":a_num-b_num, "MULTIPLICATION":a_num*b_num, "DIVISION":a_num/b_num}
    desire = "Y"
    while True:
        would_calculate = input("Would you like to use the calculator? Y/N, input is not case sensitive: ").upper()
        desire = would_calculate
        if desire != "Y":
            break
        calculation = input("How would you like to calculate? Addition, Subtraction, Division, or Multiplication? Input is not case sensitive.: ").upper()
        if calculation in desired_calculations:
            print(desired_calculations[calculation])
user_calculator()

####Exercise #2 create a pyramid of X's for n number of levels.

def pyramid_of_x():
    n = int(input("How many rows of X's would you like?: "))
    spaces = 5
    num_x = 1
    for i in range(1, n+1):
        print((" " * spaces) + ("X" * num_x))
        spaces -= 1
        num_x += 2
pyramid_of_x()


