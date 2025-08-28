# print multiplication using loop
num=int(input("Enter any number of which you want multiplication"))
print(f"Multiplication table of {num}:")
for i in range (1,11):
  print(f"{num} x{i} ={num*i}")