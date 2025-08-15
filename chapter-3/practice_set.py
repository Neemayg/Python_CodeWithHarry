name=(input("Enter your username: "))
print(f"Good Afternoon {name} ")

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace("<|Name|>","Neemay Gupta").replace("<|Date|>","15th August 2025"))

b="Neemay  Gupta  is good "
print(b.replace("  "," "))

letter = "Dear Harry,\n \tThis python course is nice.\n Thanks!"
print(letter)