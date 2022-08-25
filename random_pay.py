from itertools import count
import random

names = input("Enter the names seperated by commas:  ")
name_split = names.split(", ")

count_list = len(name_split)

rand_name = random.sample(name_split, 1)[0]
print(f"{rand_name} is going to buy the meal today!")

