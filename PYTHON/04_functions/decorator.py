# def decorator_func(func):
#   def wrapper():
#     print("This will execute before function")
#     func()
#     print("This will execute after function")
#   return wrapper

# @decorator_func
# def say_hi():
#   print("Say hi")
# say_hi()

import time
def timer(func):
  def wrapper(*args, **kargs):
    start = time.time()
    func(*args, **kargs)
    print("Time taken by the function is ",time.time() - start)
  return wrapper

@timer
def list_parser(list):
  time.sleep(2)
  print(list)
  for i in list:
    print(i)
list_parser([1,5,6,7,9,3])