from time import time


number = int(input("Enter number of your choice:  "))

multiple = 1

#while (multiple <= 10):
 #times = multiple * number
 #multiple += 1
 #print(times)

for multiple in range(1, 11):
 times = multiple * number
 print(times)