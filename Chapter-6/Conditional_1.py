num1=int(input("Enter a number between 1-10: "))
num2=int(input("Enter a number between 1-10: "))
num3=int(input("Enter a number between 1-10: "))
if(num1>num2 and num1>num3):
  print(f"First number is heighest which is {num1}")
elif(num2>num1 and num2>num3):
  print(f"Second number is heighest which is {num2}")
else:
  print(f"Third number is heighest which is {num3}")