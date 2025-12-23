#To check that the number entered by the user is divisible by 3,5 or both or none
num1=int(input("Enter the number for which you want to check the divisibilty for: "))
if num1%3==0 and num1%5==0:
  print("Number is divisible by both 3 and 5")
elif num1%3==0:
  print("Number is divisible by 3 ")
if num1%5==0:
  print("Number is divisible by 5 ")
if num1%3!=0 and num1%5!=0:
  print("Number is not divisible by both 3 and 5")