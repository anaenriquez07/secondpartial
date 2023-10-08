https://replit.com/join/tjdpkcjrqy-ana-lucialuc103
print("The values that can be used are:")
print("fahrenheit, miles, liters, kilometers, gallons, celsius ")
origin = input("What is the unit of origin? ") 
destination = input("Which unit would you like to convert it to? ")
quantity = float(input("Enter the quantity "))
ctof = float(quantity)/1.8 + 32
ftoc = float(quantity)*1.8 + 32
mtokm = float(quantity)*1.609344
kmtom = float(quantity)/1.609344
ltog = float(quantity)*0.264172
gtol = float(quantity)/0.264172

if origin == "kilometers" and destination == "miles":
  print(quantity,"kilometers is approximatly equal to",kmtom,"miles")
elif origin == "farenheit" and destination == "celsius":
  print(quantity,"farenheit is approximatly equal to",ftoc,"celsius")
elif origin == "miles" and destination == "kilometers":
  print(quantity,"miles is approximatly equal to",mtokm,"kilometers")
elif origin == "liters" and destination == "gallons":
  print(quantity,"liters is approximatly equal to",ltog,"gallons")
elif origin == "gallons" and destination == "liters":
  print(quantity,"gallons is approximatly equal to",gtol,"liters")
elif origin == "celsius" and destination == "farenheit":
  print(quantity,"celsius is approximatly equal to",ctof,"farenheit")
else:
  print ("Please enter two valid units") 
