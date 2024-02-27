""" Strings """

"Quick Recap"
print(" Strings ")
x = " Strings "
print(x)

""" Strings Indexing """
x = "Hello YouTube"
# H e l l o   Y o u T u b e
# 0 1 2 3 4 5 6 7 8 8 10 11 12
print(x[6])
print(x[-5])

""" Strings Slicing """
y = "Hello Mikel, My Name Is Qusai"
st0 = y.find("My")
en0 = y.find(" " , y.find("Qusai"))
en1 = y.find(",")
print(y[st0:en0])
print(y[:en1])
print(y[-13:-8])

""" Strings Methods """

# split
print('qusai mohammed amer ahmed'.split())

# capitalize
print('Qusai mohammed'.capitalize())

# title
var0 = 'qusai mohammed amer ahmed'.title().split()
print(var0)

# upper
print("university".upper())

# lower
print("UNIVERSITY".lower())

# count
print('qusai mohammed amer ahmed'.count('a'))

# startswith , endswith
print("hello".endswith('o'))
print("hello".startswith('h'))

# join
print(' '.join(var0))

# strip
print("   hello world       ".strip())

# removesuffix , removeprefix
path = "C:\\Users\\HP\\Desktop\\Main-WorkSpace\\File Orgnizer\\Main.py"
print(path.removesuffix('\\Main.py'))

extension = path[path.find('.'):]
print(extension.removeprefix('.'))


""" Strings Formatting """
age = 20
name = "Layla"
txt = "My name is {}, I am {} yers old".format(name , age)
print(txt)

age = 25
name = "Mikasa"
city = "Dubai"
txt = f"My name is {name}, I am {age} yers old, I live in {city}"
print(txt)

title = "product"
column = "name"
print("{:>15} | {:s}".format(title , column))

""" Escaping Characters"""
# \'	Single Quote
# \\	Backslash
# \n	New Line
# \t	Tab
# \b	Backspace

# \'	Single Quote
text = "Issac Newton once said \"I Love Mikasa\""
print(text)

# \\	Backslash
p = "C:\\Users\\HP\\Desktop\\Main-WorkSpace\\File Orgnizer\\Main.py"
p = r"C:\Users\HP\Desktop\Main-WorkSpace\File Orgnizer\Main.py"
print(p)

# \n	New Line
print("Qasem:Hello Mohammed!\nMohammed:Hey bro wassup")

# \t	Tab
print("Name\tAge\tGrade\tCountry\nMustafa\t23\t11\tSudan")

# \b	Backspace
text = "The weather is wonderful today!\b "
print(text)

""" Homework """

paragraph = """Data sources and definitions: Different countries have different methodologies for collecting and reporting crime data, making direct comparisons challenging. Additionally, crime definitions can vary, leading to discrepancies.
Social and economic context: Crime rates are often influenced by factors like poverty, inequality, and social unrest. Generalizing about crime rates without considering these underlying factors can be misleading.
Types of crime: Distinguishing between different types of crime, such as violent crime versus property crime, is crucial for understanding the nature of crime in a specific country.
Trends over time: Crime rates can fluctuate over time, so it's important to consider recent trends rather than relying solely on outdated data.
With those points in mind, here's a brief overview of some countries that consistently rank high on crime indices, according to sources like the World Population Review and Numbeo:
High Crime Rates Venezuela: Struggles with poverty, corruption, and political instability, leading to high rates of violent crime and homicide.
Papua New Guinea: Faces challenges with corruption, gang violence, and limited law enforcement resources.
South Africa: Experiences high rates of violent crime, including assault and robbery, often linked to poverty and social inequality.
Afghanistan: Ongoing conflict and political instability contribute to high levels of violent crime and insecurity.
Honduras: Gang violence and drug trafficking significantly impact crime rates, particularly in major cities."""
