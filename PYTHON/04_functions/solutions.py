# def square(number):
#   return number**2
# result = square(5)
# print(result)

# Problem: Create a function that takes two numbers as parameters and returns their sum.

# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.
# def multiply(P1, P2):
#   return (P1 * P2)
# print(multiply(5,4))
# print(multiply("chai", 5))

# Problem: Create a function that returns both the area and circumference of a circle given its radius.

# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.
# def greet(str = "Durgesh Tiwari"):
#   print("Hello", str, "Good Morning!")
# greet("Shubham Tiwari")

# Problem: Create a lambda function to compute the cube of a number.
# cube = lambda x : x**3
# print(cube(5))

# Problem: Write a function that takes variable number of arguments and returns their sum.
# def sum_arg(*args):
#   return sum(args)
# print(sum_arg(1,5,7,8,65,48,70))
# print(sum_arg(1,5,7,8))
# print(sum_arg(1,5,6))

# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.
# def print_Kargs(**kwargs):
#   for key, value in kwargs.items():
#     print(f"{key} : {value}")
# print_Kargs(name = "Shaktiman", power="Lazer")
# print_Kargs(name = "Shaktiman")
# print_Kargs(name = "Shaktiman", power="Lazer", enemy="Dr. Jackaal")

# Problem: Write a generator function that yields even numbers up to a specified limit.
# def even_Generator(limit):
#   for i in range(2, limit + 1, 2):
#     yield i
# for num in even_Generator(10):
#   print(num)

# Problem: Create a recursive function to calculate the factorial of a number.
# def factorial(num):
#   if(num == 0):
#     return 1
#   else:
#     return num * factorial(num - 1)
# print(factorial(5))
