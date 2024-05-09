""" Object Oriented Programming """

# FP(Functional Programming) VS OOP(Object Oriented Programming)
def square(x):
  return x * x

def map_square(numbers):
  return list(map(square, numbers))

numbers = [1, 2, 3, 4]
squared_numbers = map_square(numbers)
print(squared_numbers)

" What is Object? "
x = "ff"
y = "qusai"
print(type(x))
print(type(y))

def hello():
  print("hello")

print(type(hello))

" Class "
class Player:
  health = 100
  power = 5

Player1 = Player()
Player2 = Player()
print(Player1.power)
print(Player2.power)

" Methods "
class Animals:
  x = 10
  y = 9
  def mammals(self): # الثديات
    return ["Lion" , "Tiger" , "Panda"]
  
  def reptile(self): # الزواحف
    return ["Snake" , "Turtle" , "Snail"]
  
  def aquatic(self): # الحيوانات المائية
    return ["Dolphin" , "Shark" , "Whale"]

an = Animals()
print(an.aquatic())

" __init__ Constructor "
class Person:
  def __init__(self, name , age, nation):
    self.name = name
    self.age = age
    self.nation = nation
  
  def info(self):
    print(f"My Name Is {self.name}\nI'm {self.age} Years Old\nI'm From {self.nation}")

p1 = Person("Mohammed" , 25 , "Syria")
p2 = Person("Khaled" , 21 , "Saudi")
# print(p1.name)
# print(p2.name)
p2.info()

" Practical 1 "
class Rectangle:
  def __init__(self , width , Length) -> None:
    self.width = width
    self.length = Length

  def area(self):
    return self.width * self.length
  
  def perimeter(self):
    return 2 * (self.width + self.length)

rec1 = Rectangle(50, 100)
area1 = rec1.area()
perimeter1 = rec1.perimeter()
print(f"Area Of The Rectangle 1: {area1}")
print(f"Perimeter Of The Rectangle 1: {perimeter1}")

rec2 = Rectangle(15, 35)
area2 = rec2.area()
perimeter2 = rec2.perimeter()
print(f"Area Of The Rectangle 2: {area2}")
print(f"Perimeter Of The Rectangle 2: {perimeter2}")

" Practical 2 "
class Student():
  def __init__(self, name, age, grade) -> None:
    self.name = name
    self.age = age
    self.grade = grade

class Course():
  def __init__(self, name, max_students) -> None:
    self.course_name = name
    self.max = max_students
    self.students = []
  
  def add_students(self, student):
    if len(self.students) < self.max:
      self.students.append(student)
      return True
    else:
      return False
  
  def get_average_grade(self):
    total = 0
    for s in self.students:
      total += s.grade
    return f"The Average Of Grades Is {total / len(self.students)}"

st1 = Student("Khaled" , 21 , 75)
st2 = Student("Braa" , 26 , 90)
st3 = Student("Qusai" , 20 , 99.9)
st4 = Student("Ayham" , 21 , 80)

calculus = Course("Calculus 1" , 20)
calculus.add_students(st1)
calculus.add_students(st2)
calculus.add_students(st3)
calculus.add_students(st4)

print(calculus.students[2].grade)
print(calculus.get_average_grade())

" Inheritance "
class Animal:
  def __init__(self, name, weight, price):
    self.name = name
    self.weight = weight
    self.price = price

  def sleep(self):
    print("The Animal Is Sleeping")


class Dog(Animal):
  def __init__(self, name, weight, price, trained:bool, competitve:bool):
    super().__init__(name, weight, price)
    self.trained = trained
    self.competitve = competitve
  
  def speak(self):
    print("عوعو")

dog = Dog("Dembele" , 79 , 0.5, False , False)
print(dog.name)
print(dog.weight)
print(dog.price)
print(dog.trained)
print(dog.competitve)
dog.speak()

" Practical 3 "
class Product():
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity

  def display_info(self):
    print(f"Name: {self.name}")
    print(f"Price: ${self.price:.2f}")
    print(f"Quantity: {self.quantity}")

class Electronic(Product):
  def __init__(self, name, price, quantity, brand, assurance):
    super().__init__(name, price, quantity)
    self.brand = brand
    self.assurance = assurance

  def display_info(self):
    super().display_info()
    print(f"Brand: {self.brand}")
    print(f"Assurance: {self.assurance}")

laptop = Electronic("Laptop" , 200 , 100 , "HP" , "2 years")
laptop.display_info()
phone = Electronic("Mobile" , 300 , 50 , "Samsung S24 Ultra" , "5 years")
phone.display_info()
