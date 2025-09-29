age=int(input("Enter age: "))
day=input("Enter it is weekday or weekend: ")
if age<5:
  print("Price=0")
elif age<18 and day=="weekeday":
  print("price is 50")
elif age<18 and day=="weekend":
  print("price is 70")
elif age<60 and day=="weekeday":
  print("price is 100")
elif age<60 and day=="weekend":
  print("price is 120")
else:
  if day=="weekday":
    print("price is 60")
  else:
    print("price is 80")
