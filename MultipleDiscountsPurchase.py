https://replit.com/join/mnfikhkatd-ana-lucialuc103
purchase = int(input("How much did you pay?"))
category = input("Which category? (A,B,C)")
number = int(input("How many items?"))

def typea(purchase):
  A = int(purchase) - int(purchase)*0.1
  return A

def typeb(purchase):
  B = int(purchase) - int(purchase)*0.05
  return B

def typec(purchase):
  C = int(purchase) - int(purchase)*0.02
  return C

if number >= 10: 
  if category == "A":
    totala = typea(purchase) - typea(purchase)*0.05
    print ("The discount will be 10%")
    print("You will have to pay",totala)
  elif category == "B":
    totalb = typeb(purchase) - typeb(purchase)*0.05
    print ("The discount will be 5%")
    print("You will have to pay",totalb)
  elif category == "C":
    totalc = typec(purchase) - typec(purchase)*0.05
    print ("The discount will be 2%")
    print("You will have to pay",totalc)
if number < 10:
  if category == "A":
    print ("The discount will be 10%")
    print("You have to pay",typea(purchase))
  elif category == "B":
    print ("The discount will be 5%")
    print("You have to pay",typeb(purchase))
  elif category == "C":
    print ("The discount will be 2%")
    print("You have to pay",typec(purchase))
