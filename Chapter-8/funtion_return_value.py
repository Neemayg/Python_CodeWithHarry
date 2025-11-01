def marks():
  user1=int(input("Enter the marks of user1: "))
  user2=int(input("Enter the marks of user2: "))
  user3=int(input("Enter the marks of user3: "))
  avg=(user1+user2+user3)/3
  print(f" Average marks of user1 ,user2, user3, are {avg}")
  return avg
a=marks()