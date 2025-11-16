class user:
  age=19
  location="Delhi"
  hobby="Badmintion"

  def grades(self):
    print(f"The age of Shreeman is {self.age} and the location is {self.location} and i think it is beautiful place to live!!")

  @staticmethod # Here you can also write staticmethod instead of self to run this..
  def greet():
    print("Good Morning!")
  


object3=user()
object3.name="Shreeman"
print(object3.name,object3.age,object3.location,object3.hobby)
object3.greet()
object3.grades()