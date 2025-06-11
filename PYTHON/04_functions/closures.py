# def outer_function(num_1):
#   print("The value of num_1 is = ",num_1)
#   def inner_fun(num_2):
#     print("The value of num_2 is = ",num_2)
#     return num_1 + num_2
#   return inner_fun
# closure = outer_function(10)
# print(closure(5))

def outer_fun():
  msg = "Hello this is "
  def inner_fun(name):
    return msg + name
  return inner_fun
closure = outer_fun()
print(closure("Durgesh"))