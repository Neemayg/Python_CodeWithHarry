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
