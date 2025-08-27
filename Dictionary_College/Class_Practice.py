d1={}
d={
  'First_Name':'Krish',
  'eid':2007
}
print(d.get("Krish2"))
# print(d["Krish2"])
print(d.values())
print(d.keys())
print(d.items())
d.update({
  "gender": 'Male',
  "Marks": '100'
})
print(d)
d.pop("eid")
print(d)
d.popitem()
print(d)
a=d.setdefault('gender','Male')
print(a)
l=[(1,2),(3,4)]
d=dict(l)
print(d)
#  write a python program to create a dictionary from the "from keys "function in which you have to store and stuedent name as a key and student marks as a value default value will be 0
# later on in the loop for every student user will enter actual marks


