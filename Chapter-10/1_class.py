class employee: # this is a class attribute
  language="python"
  salary=1200000
  name="Shreeman"

object1=employee() # this is an object attribute
object1.name="Neemay" # this is an instance attribute
print(object1.name,object1.language,object1.salary)

object2=employee()
object2.name="Sahil" # this is an instance attribute so it will overwrite the orignal name
print(object2.name,object2.language,object2.salary)