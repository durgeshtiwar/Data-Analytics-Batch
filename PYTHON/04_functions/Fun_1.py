# def check(List_1):
#   emptyList = []
#   if(type(List_1) == list):
#     for i in List_1:
#       emptyList.append(i)
#   return emptyList


# List_1  = [1,2,3,4,5, [True, False], "Durgseh", "Shubham", (10,12,"Tiwari")]
# print(check(List_1))

def print_str(row, column):  
  for i in range(1, row):
    for j in range(0, i):
      print("*", end=" ")
    print("\n")
    
print_str(10,10)