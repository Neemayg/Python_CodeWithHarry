num = int(input("Enter a number from 1 to 10: "))

def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact(num - 1)

final = fact(num)
print(f"Factorial of number is {final}")
