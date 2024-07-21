""" Errors Handling & Debugging """

" Errors Handling "
def divide(numerator,denominator):
  try:
    result = numerator / denominator
  except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
  else:
    print(f"The result of {numerator} / {denominator} is: {result}")
  finally:
    print("This block always executes regardless of exceptions.")

divide(10, 2)
divide(10, 0)
print("Hello")


# Practical 1
def transfer(from_account, to_account, amount, pin):
  
  if from_account not in valid_accounts or to_account not in valid_accounts:
    raise ValueError("Invalid Account")
  
  if balances[from_account] < amount:
    raise ValueError("Balance Is Not Enough")
  
  if pin != CORRECT_PIN:
    raise ValueError("Incorrect PIN")
  
  balances[from_account] -= amount
  balances[to_account] += amount
  print(f"Successfully transferred ${amount} from {from_account} to {to_account}.\n")
  print(f"{from_account} Balance Now Is {balances[from_account]}")
  print(f"{to_account} Balance Now Is {balances[to_account]}")

valid_accounts = ["ACC123", "ACC456"]
CORRECT_PIN = 1234
balances = {"ACC123": 1000, "ACC456": 500}

try:
  transfer("ACC123", "ACC456", 200, 1234)
except ValueError as m:
  print(f"Error:{m}")

try:
  transfer("ACC123", "ACC789", 200, 1234)
except ValueError as e:
  print(f"Error: {e}")

try:
  transfer("ACC123", "ACC456", 1200, 1266)
except ValueError as e:
  print(f"Error: {e}")


" Debugging "

# Practical 2
from random import random

def loop_division(dividend, divisor):
  if divisor == 0:
    raise ZeroDivisionError("You Can Not Divide By Zero!")
  
  result = 0
  while dividend >= divisor and divisor != 0:
    dividend -= divisor
    result += 1
  return result

for i in range(10):
  dividend , divisor = int(random()*100) , int(random()*10)

  try:
    print(f"{dividend} / {divisor} = {loop_division(dividend, divisor)}")
  except ZeroDivisionError as M:
    print(M)


# Practical 3
def sort_numbers(nums):
  for i in range(len(nums)-1):
    for j in range(len(nums)-1):
      if nums[j] > nums[j+1]:
        nums[j] , nums[j+1] = nums[j+1] , nums[j]

  return nums

numbers = [2,9,19,6,10,3,55,32,4,8,10,12,8,1,0]
print(sort_numbers(numbers))