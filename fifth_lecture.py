""" Functions """

def shop_products():
    product_names = ["Laptop", "Phone", "Headphones", "Watch"]
    prices = [800, 400, 100, 250]
    quantities = [20, 50, 100, 30]

    print("{:<20} | {:>8} | {:>10}".format("Product", "Price", "Quantity"))
    print("-" * 45)  # Divider
    for i in range(len(product_names)):
        print(f"{product_names[i]:<20} | ${prices[i]:>7.2f} | {quantities[i]:>10}")

for i in range(5):
    print(i)
    if i == 3:
        shop_products()

" Parameters "
def shop_products(products:list, prices:list, quantities:list):

    print("{:<20} | {:>8} | {:>10}".format("Product", "Price", "Quantity"))
    print("-" * 45)  # Divider
    for i in range(len(products)):
        print(f"{products[i]:<20} | ${prices[i]:>7.2f} | {quantities[i]:>10}")

def inputs():
    products = []
    prices = []
    quantities = []
    for i in range(1,11):
        if i == 1:
            prod = input(f"Enter Product {i} : ").strip()
        else:
            prod = input(f"Enter Product {i} (E for exit) : ").strip().capitalize()

        if prod == "E":
            break
        pri = int(input(f"Enter The Price : " ))
        qun = int(input(f"Enter The Quantity : "))

        products.append(prod)
        prices.append(pri)
        quantities.append(qun)

    return products, prices, quantities

p , pr , q = inputs()
shop_products(p , pr , q)

# return
def add(x:int,y:int) -> int:
    return x + y

print(add(2,4))

" *Args & Unpacking "
def students(grade:int = 10, *names):
    print(f"Students In Grade {grade} are:")
    for i in names:
        print(i)
    return len(names)

names = ["Mohammed", "Osama", "Waleed", "Tarek"]
print(students(*names))

def numbers():
    nums = []
    for i in range(10):
        nums.append(i)
    return nums
print(*numbers())

" Recursion Function "
def factorial(num):
    if num == 0:
        return 1
    else:
        result = num * factorial(num-1)
        return result

print(factorial(10))

" Lambda Function "
def add(x,y):
    return x + y

# lambda inputs : output
result = lambda x,y : x+y
print(result(5,10))

nums = [1,2,3,4,5,6,7,8,9,10]
square = map(lambda x : x*x , nums)
print(*square)

celsius_temps_AbuDhabi = (30,33,32,30,31)
kelvin_temps_AbuDhabi = map(lambda t : f"\bCelsius: {t} -> Kelvin: {t+273}\n", celsius_temps_AbuDhabi)
fahrenheit_temps_AbuDhabi = map(lambda t : f"\bCelsius: {t} -> Fahrenheit: {t*9/5+32}\n", celsius_temps_AbuDhabi)
print(*kelvin_temps_AbuDhabi)
print(*fahrenheit_temps_AbuDhabi)
