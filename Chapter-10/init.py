class user:
  age=19
  location="Delhi"
  hobby="Badmintion"

  def __init__(self,name,age,profession):
    self.name= name
    self.age=age
    self.profession=profession
    print("I am creatinga. project")

  def grades(self):
    print(f"The age of Shreeman is {self.age} and the location is {self.location} and i think it is beautiful place to live!!")

  @staticmethod # Here you can also write staticmethod instead of self to run this..
  def greet():
    print("Good Morning!")

  


object3=user("Neemay",19,"Engineer")
# object3.name="Shreeman"
print(object3.name,object3.age,object3.location,object3.hobby)
object3.greet()
object3.grades()