sub1 = int(input("enter the marks of sub1 : "))
sub2 = int(input("enter the marks of sub 2  :"))
sub3 = int(input("enter the marks of sub 3 : "))
 
percentage = (sub1 + sub2 + sub3)/3
if (sub1>=33 and sub2>=33 and sub3>=33 and percentage>=40):
    print(f"student passed with percentage of {percentage}")
else:
    print(f"student failed with the percentage of {percentage}")
