student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

max = student_scores[0]
for index in student_scores:
 if index > max:
  max = index
print(max)