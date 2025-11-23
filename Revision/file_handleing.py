f=open("file1.txt","w")
f.write("Lakshay Sharma: 12")
f.write("Krish Jagya: 11")
f.close()

f=open("marks.txt","r")
print(f.read())
f.close()