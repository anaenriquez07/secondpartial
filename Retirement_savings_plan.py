https://replit.com/join/oqaqshxbmt-ana-lucialuc103
current_age = int(input("What is your age right now? "))
retire_age = int(input("At what age do you want to retire? "))
FV = input("How much money do you want to have? ")
t = int(retire_age) - (current_age)
n = int(t)*12
start_value = 0
PMT = float(FV)/float(n)

print("To reach your retirement goal, you have to save approximately",PMT, "per month")
