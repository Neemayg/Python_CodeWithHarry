user1=int(input("Enter 1st number: "))
user2=int(input("Enter 2nd number: "))
user3=int(input("Enter 3rd number: "))
user4=int(input("Enter 4rth number: "))

if(user1>user2 and user1>user3 and user1>user4):
  print("User1 is Greatest number: ",user1)
elif(user2>user3 and user2>user1 and user2>user4):
  print("User2 is Greatest number")
elif(user3>user1 and user3>user2 and user3>user4):
  print("User2 is Greatest number")
else:
  print("User4 is greates number: ",user4)
