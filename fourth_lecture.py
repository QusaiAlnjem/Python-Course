" Comparison Operators "
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
a = 5
b = 10
print(a == b)
print(a != b)
print(a < b)
print(a <= b)
print(a > b)
print(a >= b)

" if , elif , else "
# if condition:
#     code to execute if the condition is True

num = 5
if num < 10:
    print("number is less than 10")
elif num < 15:
    print("number is less than 15")
else:
    print("number is out of range")

num = 20
numbers = [1,2,3,4,5,6,7,8,9,10]
if num in numbers:
    print(f"{num} is in numbers")
else:
    print(f"{num} is NOT in numbers")

" Practical 1 "
blacklist = ("Qusai", "Waleed", "Ayham", "Layan", "Alaa", "Mohammed", "Maryam")
name = input("Enter The Name: ").capitalize()
if name in blacklist:
    print(f"{name} IS IN the blacklist!")
else:
    print(f"{name}is NOT the blacklist.")

" Empty OR NO? "
x = input("Enter any value\n")
if x:
    print(x)
else:
    print("Empty variable")

" Logical Operators "
# and - all conditions must be True
# or - at least one True condition is enough
# not - the condition must be False

n1 = 15
n2 = 40
n3 = 100
n4 = 40

if n1 <= n2 and n3 > n1:
    print("both conditions are true")
if n2 == n1 or n2 == n4:
    print("one of the conditions are true")
if not n1 == n3:
    print("the condition is False")

" Conditional Expressions "
age = int(input("Enter your age: "))
# is_adult = "Adult" if age>=18 else "Minor"
age_to_vote = "Eligible" if age>=18 else "Not Eligible"
print(f"{age} years old, You are {age_to_vote} to vote.")

""" For Loop """
# for element in collection_of_elements:
#     print(element)
num = [1, 2, 3, 4, 5]
for i in num:
    print(f"Square Of {i} is {i*i}")

for i in range(1 , 11):
    print(f"Square Of {i} is {i*i}")

" Practical 2 "
youtuber = dict(name = "MrBeast" , age = 55 , subs = "243M")
for i in youtuber.items():
    print(f"{i[0]} : {i[1]}")


" Break , Continue , Pass "
# break
numbers = [1, 4, 2, 8, 5, 10]
for i in numbers:
    if i == 2:
        print(i)
        break

# continue
fruits = ["apple", "banana", "orange", "cherry", "grape"]
for f in fruits:
    if f.startswith('b'):
        continue
    print(f)

# pass
for i in fruits:
    pass

if "apple" in fruits:
    pass

" Range In For Loop "
group1 = ['qusai' , 'ayham' , 'waleed']
group2 = ['leo' , 'jax' , 'pablo']

for i in range(len(group1)):
    print(f"Team {i+1}: {group1[i]} with {group2[i]}")

" Practical 3 "
product_names = ["Laptop", "Phone", "Headphones", "Watch", "Intel Core i5"]
prices = [800, 400, 100, 250, 350]
quantities = [20, 50, 100, 30, 10]

print("{:<20} | {:>8} | {:>10}".format("Product" , "Price" , "Quantity"))
print("-" * 45)
for i in range(len(product_names)):
    print(f"{product_names[i]:<20} |    ${prices[i]:<4} | {quantities[i]:>6}")

" List Comprehinsion "
nums = range(1,21)
# even_nums = []
# for n in nums:
#     if n%2 == 0:
#         even_nums.append(n)

even_nums = [n for n in nums if n%2==0]
print(even_nums)

""" While Loop """
# while condition:
    
#     execute code

#     increamnet or condition to break

i = 0
while i < 6:
    i += 1
    if i == 3:
        print("Skiped.")
        continue
    print(i)

" Practical 4 "
secret_number = 16
guesses = 0

while True:

    user_guess = int(input("Guess a number between 1 and 25: "))
    guesses+=1

    if user_guess == secret_number:
        print(f"Congratulations! You guessed the number in {guesses} tries.")
        break
    # Hints
    elif secret_number-3 <= user_guess <= secret_number+3:
        print("Your guess is too close. Try again.")
    elif user_guess > secret_number:
        print("Your guess is too high. Try again.")
    else:
        print("Your guess is too low. Try again.")


