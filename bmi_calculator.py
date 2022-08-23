import math

height = input("Enter your height: ")
weight = input("Enter your weight: ")

BMI = int(weight) / (float(height) ** 2)

print(int(BMI))