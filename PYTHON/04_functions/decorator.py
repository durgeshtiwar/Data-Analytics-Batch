def decorator_func(func):
  def wrapper(*args, **kargs):
    print("This will execute before function")
    func(*args, **kargs)
    print("This will execute after function")
  return wrapper

# @decorator_func
# def say_hi():
#   print("Say hi")
# say_hi()

import time
def timer(func):
  def wrapper(*args, **kargs):
    start = time.time()
    func(*args, **kargs)
    print("Time taken by this function is",time.time() - start)
  return wrapper

@timer
@decorator_func
def list_parser(list):
  time.sleep(1)
  print(list)
  for i in list:
    print(i)
list_parser([1,5,6,7,9,3])