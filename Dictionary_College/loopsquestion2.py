# write a python program to find factorial in for loop and the number will be entered by user
try:
    num = int(input("Enter a non-negative integer to find its factorial: "))
except ValueError:
    print("Invalid input. Please enter a whole number.")
    exit()

if num < 0:
    print("Factorial does not exist for negative numbers.")

elif num == 0:
    print("The factorial of 0 is 1.")

else:
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    print(f"The factorial of {num} is {factorial}.")
