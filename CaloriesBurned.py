https://replit.com/join/qnfpwazwvb-ana-lucialuc103
weight = float(input("How much do you weight? "))
duration = int(input("What was the duration of the activity in minutes?"))
activity = input("Did you swim, dance, walk, run, or cycle?")

def cycling():
  cals = int(weight) + int(duration)/0.32
  return cals

def swimming():
  cals = int(weight)*3.43533 + int(duration)*.29
  return cals

def dancing():
  cals = int(weight)*3.3747 / (int(duration)/99)
  return cals

def walking():
  cals = int(duration)**1.28967 * int(weight)/50
  return cals

def running():
  cals = (int(duration) + int(weight)) + int(weight)*7.9483548
  return cals

if activity == "dance":
  print("You burned",dancing(),"calories")
elif activity == "cycle":
  print("You burned",cycling(),"calories")
elif activity == "run":
  print("You burned",running(),"calories")
elif activity == "walk":
  print("You burned",walking(),"calories")
elif activity == "swim":
  print("You burned",swimming(),"calories")
