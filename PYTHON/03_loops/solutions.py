# Problem: Given a list of numbers, count how many are positive.
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# count_Positiov_Number = 0
# for num in numbers:
#   if(num > 0):
#     count_Positiov_Number = count_Positiov_Number + 1
# print("There are",count_Positiov_Number,"positive number")

# Problem: Calculate the sum of even numbers up to a given number n.
# number = int(input("Enter any number"))
# sum_Of_Even = 0
# for i in range(1,number + 1):
#   if(i % 2 == 0):
#     print(i)
#     sum_Of_Even = sum_Of_Even + i
# print("Sum of even numbers upto given numbers is", sum_Of_Even)

# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.
# number = int(input("Enter any number"))
# for i in range(1, 11):
#   if(i == 5):
#     continue
#   print(number,"*",i,"=",number*i)

# Problem: Reverse a string using a loop.
# str = input("Enter any String \n")
# str_length = len(str)
# for i in range(0,str_length):
#   print(str[str_length - i - 1])

# str = input("Enter any string")
# for i in str:
#   if str.count(i) == 1:
#     print("First Non Reapeated Char is", i)
#     break
    
# Problem: Keep asking the user for input until they enter a number between 1 and 10.

# while(1):
#   number = int(input("Enter any Number\n"))
#   if(number > 1 and number < 10):
#     print("This is a Valid Number")
#     break
#   else:
#     print("This is not A Valid No.")

# Problem: Check if a number is prime.
# number = int(input("Enter any number"))
# is_Prime = True
# for i in range(2, number):
#   if (number%i == 0):
#     is_Prime = False
#     break
# if(is_Prime):
#   print("This is a Prime Number")
# else:
#   print("This is not a Prime Number")

# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.
# items = ["apple", "banana", "orange", "apple", "mango"]
# unique_item = set()
# for i in items:
#   if i in unique_item:
#     print(i,"is the duplicate item of List")
#     break
#   unique_item.add(i)

# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

# import time
# wait_Time = 1
# max_Retries = 5
# attempt = 0

# while attempt < max_Retries :
#   print("Wait Time = ",wait_Time, "Attempt = ",attempt + 1)
#   time.sleep(wait_Time)
#   wait_Time = wait_Time * 2
#   attempt = attempt + 1
