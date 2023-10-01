class Student:
  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa

def sort_students(student_list):
  #sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list,
                          key=lambda student: 
                          student.cgpa,reverse=True)
  #syntax - lambda
  return sorted_students
#example usage
students = [
    Student("Tom", "A123", 7.8),
    Student("Jerry", "A124", 7.6),
    Student("Bheem", "A125", 9.9),
    Student("Shin Chan", "A126", 7.3),
]
#print the sorted list of students
sorted_students = sort_students(students)

for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA:{}".format(student.name,
                                                     student.roll_number,
                                                  student.cgpa))
