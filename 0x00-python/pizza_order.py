print("Welcome to Python Pizza Deliveries")
size = input("What size of pizza do you want? S, M or L  ")
add_pepperoni = input("DO you want pepperon? Y or N   ")
extra_cheese = input("Do you want extra cheese? Y or N  ")

if size == "S":
 bill = 15
 if add_pepperoni == "Y":
  bill += 2
 if extra_cheese == "Y":
  bill += 1

if size == "M":
 bill = 20
 if add_pepperoni == "Y":
  bill += 3
 if extra_cheese == "Y":
  bill += 1
 
if size == "L":
 bill = 20
 if add_pepperoni == "Y":
  bill += 3
 if extra_cheese == "Y":
  bill += 1

message = print(f"your bill is ${bill}")