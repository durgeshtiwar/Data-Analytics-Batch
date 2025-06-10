# def add(*args):
#   print(args)
#   sum = 0
#   for i in args:
#     print(i)
#     sum = i + sum
#   return sum
# print(add(12,5,6,9,2,45,67))

# def introduction(**kargs):
#   print(kargs)
#   for i in kargs.items():
#     print(i)
# introduction(Name = "Durgesh Tiwari", Age = 22, Profile = "Data Analyst")

# def introduction(Name, Age, Profile, /):
#   print(f"{Name, Age, Profile}")
# introduction("Durgesh Tiwari", 22, "Data Analyst")

def introduction(Name, Age, *, Profile):
  print(f"{Name, Age, Profile}")
introduction(Name = "Durgesh Tiwari", Age = 22, Profile = "Data Analyst")