# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).
age_group = int(input('Enter Your Age group'))
if(age_group < 13):
  print("Child")
elif(age_group < 19):
  print("Teenager")
elif(age_group < 59):
  print("Adult")
else:
  print("Senior")