height = input("Enter your height: ")
weight = input("Enter your weight: ")

BMI = float(int(weight) / (float(height) ** 2))

if (BMI <= 35):
 if(BMI < 18.5):
  print("underweight")
 elif BMI < 25:
  print("normal weight")
 elif BMI < 30:
  print("overweight")
else:
 print("clinically obese")