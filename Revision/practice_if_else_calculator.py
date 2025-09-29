num1=float(input("Enter the first number: "))
num2=float(input("Enter the second number: "))
operation=input("Enter operator from the following +,-,*,/,%,//: ")
if operation=='+':
  print(num1 + num2)
elif operation=='-':
  print(num1 - num2)
elif operation=='*':
  print(num1 * num2)
elif operation=='/':
  print(num1 / num2)
elif operation=='%':
  print(num1 % num2)
elif operation=='//':
  print(num1 // num2)
else:
  print("Enter a valid operator")