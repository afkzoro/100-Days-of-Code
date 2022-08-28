print("""
      
 .d8888b 8888b. 888  888 .d88b. 88888b.d88b.  8888b. 88888b.  
d88P"       "88b888  888d8P  Y8b888 "888 "88b    "88b888 "88b 
888     .d888888Y88  88P88888888888  888  888.d888888888  888 
Y88b.   888  888 Y8bd8P Y8b.    888  888  888888  888888  888 
 "Y8888P"Y888888  Y88P   "Y8888 888  888  888"Y888888888  888   
      
      
 """)

print("Welcome to Caveman Island!\nYour mission is to successfully leave the island.")

move = input("Pick an action. Left or Right?   ")

move_low = move.lower()

if move_low == "left":
 swim = input("You've seen a river. Cross or Stay?   ")
 swim_low = swim.lower()
 if swim_low == "stay":
  print("Smart! onto the next stage")
  escape = input("You've seen a cave. Advance or Turn back")
  escape_low = escape.lower()
  if escape_low == "advance":
   print("Yayyyyyyyy! You escaped Caveman Island")
  else:
   print("The island doesn't want you to leave. Game Over")
 else:
  print("You got eaten by a crocodile. Game Over!")
else:
 print("You got swallowed by the Daemogorgon. Game Over!")