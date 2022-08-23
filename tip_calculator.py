print("Welcome to the tip calculator")

bill = input("what is the total bill?   $")
split_bill = input("how many people split the bill?  ")
tip = input("what percentage tip would you like to give? 10, 12, or 15  ")

tip_percent = float(int(tip)/100) * float(bill)
sum_tip = float(tip_percent) + float(bill)

shared_bill1 = float(sum_tip) / int(split_bill)
shared_bill2 = round(shared_bill1, 2)

print(f"Each person should pay :  ${shared_bill2}")