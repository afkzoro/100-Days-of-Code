from itertools import count


student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

#To calculate length of list
count  = 0
for length in student_heights:
   count += 1

#Adding list
sum = 0
for index in range(count):
   sum += student_heights[index]

average_heigth = round(sum / count)

#   print(f"The average height of the group is {average_heigth}")