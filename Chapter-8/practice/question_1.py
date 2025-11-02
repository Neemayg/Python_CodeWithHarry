def greatest():
  if a>b and a>c:
    print(f"{a} is the greatest number")
  elif b>c and b>a:
    print(f"{b} is the greatest number")
  elif c>a and c>b:
    print(f"{c} is the greatest number")
  elif a==b==c:
    print(f"{a} is the greatest number")

a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
greatest()