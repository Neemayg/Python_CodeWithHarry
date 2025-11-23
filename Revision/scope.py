print("To Check the local_scope and global_scope")
global_var="global variable"
def scope():
  local_var="Local variable"
  print("Inside the function")
  print(global_var)
  print(local_var)

run=scope()
print("Outside the function")
print(global_var)
# print(local_var) showing namerror

    