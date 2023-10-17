https://replit.com/join/laxvyruyrt-ana-lucialuc103

grade = 0
project = 0
students = input("How many students will be evaluated? ")
number_students = []

for i in range(int((students))):
  grade = float(input ("What is the average grade? "))
  participation = input("Did the student participate in class? ")
  project = float(input("What was the grade the student got on their project? "))
  number_students.append(i)
  if grade >= int("75") and participation == "Yes":
    print ("The student is in good academic standing")
  elif grade < int("60") or participation == "No":
    print ("The student needs to improve their performance")
  else:
    print ("The student is neither good nor bad")
  if project > 90:
    print ("The student has a distinction")
    
