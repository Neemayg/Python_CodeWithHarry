class dogs:
  def __init__(self,name,breed):
    self.name=name
    self.breed=breed
    print(f"Name of the dog is {self.name} and the breed of the dog is {self.breed} it hasd been created")

  def bark(self):
    print(f"{self.name} says woof!!")

dog1=dogs("Lakshay","pitbull")
dog2=dogs("Krish","labrador")
print(f"Dog 1 name is {dog1.name}")
print(f"Dog 2 name is {dog2.name}")
dog1.bark()
dog2.bark()
