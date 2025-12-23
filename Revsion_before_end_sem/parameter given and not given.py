# To get the sum of two numbers in which one is given if not provided
print("Enter a number for which you want to calculte the sum")
x=int(input("Enter number 1: "))
y=int(input("Enter number 2: "))
def normal_sum (x,y=10):
  total=x + y 
  print(f"Sum of the number {x} and {y} is {total}")
normal_sum(x,y)