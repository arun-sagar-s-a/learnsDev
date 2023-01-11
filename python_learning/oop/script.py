class Student:
  def __init__(self,name,roll,isfriendly=True):
    self.name = name
    self.roll = roll
    self.courses = []
    self.friendlist = []
    self.isfriendly = isfriendly

  def are_friends(self,other_student):
    if other_student.isfriendly and self.isfriendly:
      self.friendlist.append(other_student.name)
      other_student.friendlist.append(self.name)
  def add_course(self,course):
    self.courses.append(course.name)

  def __repr__(self):
    if self.friendlist:
      return f"{self.name} has roll number {self.roll} his list of friends ar {self.friendlist} has taken course(s){self.courses}"
    else:
      return f"{self.name} has roll number {self.roll} has no friends yet"


class Course:
  def __init__(self,name,difficlty,book,credit):
    self.name = name
    self.credit = credit
    self.difficlty = difficlty
    self.book = book
  
  def __repr__(self):
    return f"{self.name} has acredit of {self.credit} and its diffuclty level is {self.difficlty}, to ace this course you need to read {self.book}"


course1 = Course(name="Embedded",credit="4.5",difficlty="S",book="EmbeddedSystem")
student1 = Student("Arun","10")
student2 = Student("ArunS","11")
student2.are_friends(student1)
student1.add_course(course1)

print(student1)
print(student2)
print(course1)
