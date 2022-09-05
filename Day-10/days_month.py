def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True #Input is a leap year
      else:
        return False #Input is not a leap year
    else:
      return True #Input is a leap year
  else:
    return False #Input is not a leap year

def days_in_month(yr,mnt):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  
  if is_leap(yr) == True:
      month_days[1] = 29
      return month_days[(mnt - 1)]
  
  elif is_leap(yr) == False:
      return month_days[(mnt - 1)]
  

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)