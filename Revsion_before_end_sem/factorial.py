#Take a number from user and calculate the factorial of it
n=int(input("Enter the number for which you want the factorial of: "))
def fact(n):
  if n==0 or n==1:
    return 1
  else:
    return n * fact(n-1)
print(f"Factorial of {n} is {fact(n)}")