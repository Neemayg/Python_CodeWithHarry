# write a python program to create a dictionary from the "from keys "function in which you have to store and stuedent name as a key and student marks as a value default value will be 0
# later on in the loop for every student user will enter actual marks

student_names = ['Neemay', 'Krish', 'swastik', 'Lakshay']
student_marks = dict.fromkeys(student_names, 0)

print("Initial student marks dictionary:")
print(student_marks)

print("Please enter the marks for each student:")
for student in student_names:
        marks = int(input(f"Enter marks for {student}: "))
        student_marks[student] = marks
print("\nFinal student marks dictionary:")
print(student_marks)
