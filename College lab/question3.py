# print prime number using while loop in python
n = int(input("Enter limit: "))
num = 2
while num <= n:
    i = 2
    prime = True
    while i < num:
        if num % i == 0:
            prime = False
            break
        i += 1
    if prime:
        print(num, end=" ")
    num += 1



