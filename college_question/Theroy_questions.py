# Question-1
# for ch in "Hi":
#   print(ch)
#question-2
# for i in range(1,11):
#   for j in range (1,11):
#     print(i*j,end=" ")
#   print('')

# print 1,3,5,7 starts

# for i in range(1,5):
#   for j in range(1,2*i):
#     print("*",end =" ")
#   print()
#Reversing A number
num = 12345
rev=0
length=len(str(num))
for i in range(length) :
  digit=num%10
  rev=rev * 10 +digit
  num //=10
print(rev)
#use a while loop to keep asking the user to enter a number until they enter zero finally print ten sum of the entered numbers
sum=0
while True:
  user=int(input("Enter a number of your choice: "))
  if(user!=0):
    sum+=user
  else:
    break
print(sum)