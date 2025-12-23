# This is code to check if the user is eligible to vote or not
age_input=int(input("Enter your age: "))
Citizen_indian=input("Are you a citizen of India (yes/no): ").lower()
if age_input>18 and Citizen_indian=="yes":
  print("User can vote")
else:
  print("User cannot vote :(")