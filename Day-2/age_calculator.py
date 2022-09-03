age = input("Enter your age: ")

age_int = int(age)

age_sub = 90 - age_int


days = int(age_sub *  365)

weeks = age_sub * 52

months = age_sub * 12

print(f"You have {days} days left,  {weeks} weeks  left,  {months} months lenft")
