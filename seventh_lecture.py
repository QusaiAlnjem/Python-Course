""" Modules """
# import random
from random import randint, random
print(dir(random))
print(random())
print(random)
print(randint(1,10))

# Pandas
import pandas as pd # type: ignore
dataframe = pd.read_csv(r"C:\Users\HP\Documents\csv\employees.csv")
print(dataframe.to_string())

# Time
import time
start_time = time.time()
# Program #
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
  def __init__(self, name, price, quantity, brand):
    super().__init__(name, price, quantity)
    self.brand = brand

  def display_info(self):
    super().display_info()
    print(f"Brand: {self.brand}")

# Create product instances
laptop = Electronic("Laptop", 599.99, 10, "Dell")
shirt = Product("T-Shirt", 19.99, 25)

# Display product information
laptop.display_info()
print("\n")
shirt.display_info()
# Program Ends #
end_time = time.time()
print(f"Program took {end_time - start_time:.5f} seconds to finish")

""" Decorators """
def f1():
  print("function f1 was called")

def f2(func):
  func()

print(f1)
f2(f1)

# wrapper function
def note(func):
  def wrapper():
    print("Starting...")
    func()
    print("Ended.")
  return wrapper

note(f1)
print(note(f1))
note(f1)()
x = note(f1)
x()

@note
def f1():
  print("function f1 was called")

f1()

" Practical "
from functools import lru_cache
from time import time

def running_time(func):
  def wrapper(*Args, **Kwargs):
    start_time = time()
    value = func(*Args, **Kwargs)
    end_time = time()
    print(f"Running Time: {end_time - start_time:.3f}s")
    return value
  return wrapper

@lru_cache(maxsize=4)
def fibonacci(n):
  """Calculates the nth fibonacci number."""
  if n < 2:
    return n
  return fibonacci(n-1) + fibonacci(n-2)

@running_time
def main():
  for i in range(41):
    print(i, fibonacci(i))

main()

" Class Decorators "
class Student():

  students_names = []
  
  def __init__(self, name, age, grade) -> None:
    self.name = name
    self.age = age
    self.grade = grade
    Student.add(self.name)

  @classmethod
  def add(cls , name):
    cls.students_names.append(name)
  
  @staticmethod
  def division(x , y):
    return x / y

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
  
  @property
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

print(Student.students_names)
print(Student.division(10 , 5))
print(calculus.get_average_grade)

" if __name__ == '__main__' "
print(dir())

def fun():
  print("hello")

if __name__ == '__main__':
  print(f"__name__ of file is: {__name__}")
  fun()