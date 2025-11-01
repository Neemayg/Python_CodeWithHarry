def factorial(n):
  if (n==0 or n==1):
    return 1
  else:
    return (n * factorial(n-1))
n=int(input("Enter a number for which you want a value: "))
print(f"Factorial of the number {n} is {factorial(n)}")