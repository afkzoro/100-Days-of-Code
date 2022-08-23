print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name_one_lower = name1.lower()
name_two_lower = name2.lower()

name_one_lower_t = name_one_lower.count("t")
name_one_lower_r = name_one_lower.count("r")
name_one_lower_u = name_one_lower.count("u")
name_one_lower_e = name_one_lower.count("e")


name_one_lower_l = name_one_lower.count("l")
name_one_lower_v = name_one_lower.count("v")
name_one_lower_o = name_one_lower.count("o")

name_two_lower_t = name_two_lower.count("t")
name_two_lower_r = name_two_lower.count("r")
name_two_lower_u = name_two_lower.count("u")
name_two_lower_e = name_two_lower.count("e")


name_two_lower_l = name_two_lower.count("l")
name_two_lower_v = name_two_lower.count("v")
name_two_lower_o = name_two_lower.count("o")

total_count_true = name_one_lower_e + name_one_lower_u + name_one_lower_r + name_one_lower_t + name_two_lower_e + name_two_lower_u + name_two_lower_r + name_two_lower_t

total_count_love = name_two_lower_o + name_two_lower_v + name_two_lower_l + name_two_lower_e + name_one_lower_l + name_one_lower_o + name_one_lower_v + name_one_lower_e

scores = int(str(total_count_true) + str(total_count_love))

if scores < 10 and scores > 90:
 print(f"Your score is {scores}, you go together like coke and mentos.")
if (scores > 40 and scores < 50):
 print(f"Your score is {scores}, you are alright together.")
else:
 print(f"Your score is {scores}")