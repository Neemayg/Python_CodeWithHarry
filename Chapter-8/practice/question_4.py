a = int(input("Enter the number till which you want to calculate sum of natural numbers: "))

def calc_sum(n):
    if n == 1:
        return 1
    else:
        return calc_sum(n - 1) + n

b = calc_sum(a)
print(f"Sum of first {a} natural numbers is: {b}")
