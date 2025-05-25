student_marks = {'Rashi':45, 'Nehal':57, 'Sachin': 40, 'harsh': 78 }

name = input('Enter the student name:')
if name in student_marks:
    print(f'{name}, marks {student_marks[name]}')

else:
    print('Student not found in records')