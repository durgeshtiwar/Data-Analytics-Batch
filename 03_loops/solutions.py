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
# list_1 = []
# for i in range(0, len(str)):
#   for j in range(i, len(str)):
#     if str[i] == str[j]:
#       break