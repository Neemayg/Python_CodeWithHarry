#number guessing game
value=17
while True:
  user=int(input("Enter the number:"))
  if user<value:
    print("The guess is too low")
  elif user>value:
    print("the guess is too high")
  elif user==value:
    print("the guess is correct")
    break
  else:
    print("user entered wrong number")