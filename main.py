class Student:
  def __init__(self,id,name,grade,age):
    self.id=id
    self.name=name
    self.grade=grade
    self.age=age
  def display(self):
    print(f"id:{self.id},name:{self.name},grade:{self.grade},age:{self.age}")
class Teacher:
  def __init__(self,name,designation,id,subject):
    self.name=name
    self.designation=designation
    self.id=id
    self.subject=subject
  def display(self):
    print(f"name:{self.name},designation:{self.designation},id:{self.id},subject:{self.subject}")
class SCHOOLMANAGMENTSYSTEM:
  def __init__(self):
    self.students=[]
    self.teachers=[]
  def add_student(self):
    id=input("enter student id:")
    name=input("enter student name:")
    grade=input("enter student grade:")
    age=input("enter student age")
    student=Student(id,name,grade,age)
    self.students.append(student)
    print("student added successfully:")
  def view_student(self):
    for student in self.students:
      student.display()
    print()
    if not self.students:
      print("no student found")
      return
  def search(self):
    id=input("enter student id to search:")
    for student in self.students:
      if student.id==id:
        student.display()
        return
    print("student not found")
  def add_teacher(self):
    name=input("enter teacher name:")
    designation=input("enter teacher designation:")
    id=input("enter teacher id:")
    subject=input("enter teacher subject:")
    teacher=Teacher(name,designation,id,subject)
    self.teachers.append(teacher)
    print("teacher added successfully:")
  def view_teacher(self):
    for teacher in self.teachers:
      teacher.display()
    print()
    if not self.teachers:
      print("no teacher found")
      return
  def search_teacher(self):
    id=input("enter teacher id to search:")
    for teacher in self.teachers:
      if teacher.id==id:
        teacher.display()
        return
    print("teacher not found")
  def menu(self):
    while True:
      print("school managment system")
      print("1.add student")
      print("2.view student's")
      print("3.search student")
      print("4.add teacher")
      print("5.view teachers")
      print("6.search teacher")
      print("7.exit")
      choice=input("enter your choice(1-7):")
      if choice=="1":
        self.add_student()
      elif choice=="2":
        self.view_student()
      elif choice=="3":
        self.search()
      elif choice=="4":
        self.add_teacher()
      elif choice=="5":
        self.view_teacher()
      elif choice=="6":
        self.search_teacher()
      elif choice=="7":
        break
      else:
        print("invalid choice.please try again.")
sms=SCHOOLMANAGMENTSYSTEM()
sms.menu()
