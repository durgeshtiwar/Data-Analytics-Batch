# you have to write a fun which will take string and return a len of it without using a inbuilt fun len

# def Check_string(str):
#   cnt = 0
#   for i in str:
#     cnt = cnt + 1
#   return cnt
    
# print("Length of String is", Check_string("Durgesh Tiwari"))

# 2 . write a fun which will be able to print an index of all premitive element which you will pass

# def find_index(list_1):
#   for i in list_1:
#     print(i,"it's index no is",list_1.index(i), "and it's type is",type(i))
    
# list_1 = [2,5,8,9,20,"Duregsh", True,
#           ["xyz", True, False, 5],
#           (2,5,7,8,9)]
# find_index(list_1)

# 3 . Write a fun which will take input as a dict and give me out as a list of all the values even in case of 2 level nesting it should work.

def dict_to_list(dict_1):
  list_1 = []
  if(type(dict_1) == dict):
    for key, value in dict_1.items():
      if(type(value) == dict):
        for subkey, subavlue in value.items():
          list_1.append(subkey)
          list_1.append(subavlue)
      else:  
        list_1.append(key)
        list_1.append(value)
  return list_1

dict_1 = {
  "Name":"Durgesh",
  "Age":23,
  "Qualification":{
    "Course":"B.Tech",
    "Branch":"CSE",
    "Completion Year" : 2024
  }
}

print(dict_to_list(dict_1))