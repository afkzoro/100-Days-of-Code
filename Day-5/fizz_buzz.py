from itertools import count


for number in range(1, 100):
 if number % 3 == 0 and number % 5 == 0:
  print("FizzBuzz")
  continue
 
 elif number % 3 == 0:
  print("Fizz")
  continue
 
 elif number % 5 == 0:
  print("Buzz")
  continue
 
 print(number)