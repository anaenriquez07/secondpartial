https://replit.com/join/zyrddyemeg-ana-lucialuc103

age = float(input("What is the patient's age? "))
weight = float(input("What is the weight of the patient? (in kg)"))
activity = input("Level of activity of the patient (sedentary, moderate, active)")
height = float(input("What is the height of the patient? (in meters) "))

if age <= float("18"):
  print ("The patient should have a high carbohydrate diet")
elif age > float("18") and age < float("35"):
  print ("We recommend a high protein and low carbohydrate diet")
elif age > float("35"):
  print ("We recommend a low sugar diet")

if (float("30") >= age >= float("18")) and str(activity == "sedentary" or "moderate"):
  print ("You need aerobic exercises")

BMI = float(weight)/float(height)**2
print (BMI)

if float("18") > BMI and activity == "sedentary":
  print ("You need to consult a nutritionist and increase your physical activity")
elif float("18") < BMI < float("25") and activity == "moderate" or float("18") < BMI < float("25") and activity == "active":
  print ("You are in good condition")
elif float("25") < BMI and activity == "sedentary":
  print ("You need to consult a nutritionist")
  print ("increase physical activity and reduce weight")
