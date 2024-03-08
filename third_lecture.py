" Lists "
names = ["Khaled Kashmery" , "Khidir Karawita" , "Mohammed Sumbol" , "bebo"]
print(type(names))
print(names)
print(names[1])
print(names[:2])

list1 = [1.4,10.2,100.2,1000]
print(list1)

list2 = [True  ,False]
print(list2)

list3 = ["abc", 10 , False , 2.55]
print(list3)

lists = [[1,2] , [3,4] , [5,6]]
print(lists)

biglist = [1,22,4,5,23,57,89,22,1,221,34,98,876,7,65,78,22,866,54,55,89,11]
print(len(biglist))
print(biglist.count(22))

# Practical
grade10 = input("Enter the names of the students in grade 10(first name only):\n").title().split(' ')
print(len(grade10))
print(grade10)

# Updating: add remove replace

# add
names.append("Abdul Alrahman Alzubda")
print(names)
names.insert(1 , "Messi")
print(names)
# remove
names.remove("Khaled Kashmery")
print(names)
names.pop(2)
print(names)
names.pop()
print(names)
names.clear()
print(names)
# replace
numbers = [1, 2, "True", 4, 5, "6", 7]
numbers[2] = 3
numbers[numbers.index("6")] = 6
print(numbers)

# joining lists
list1 = [1.4,10.2,100.2,1000]
list2 = ["abc", 10 , False , 2.55]
NewList = list1 + list2
print(NewList)

list1.extend(list2)
print(list1)

# sorting lists
biglist = [1,22,4,5,23,57,89,22,1,221,34,98,876,7,65,78,22,866,54,55,89,11]
biglist.sort()
print(biglist)
names.sort()
print(names)
names.sort(reverse=True)
print(names)
biglist.reverse()
print(biglist)


print(ord('C'))
# CAPITAL LETTERS IN RANGE 65 - 90
# small letters in range 97 - 122

# copying
list1 = [1, 2, 3, 4, 5]
list2 = list1
list3 = list1.copy()
print(list1)
print(list2)
print(list3)

" Tuples "
my_tuple = (1,2,3,1,4,"qusaai",1)
print(type(my_tuple))
print(len(my_tuple))
print(my_tuple)
# Tuples are ordered and not changable
# order cannot be changed
# items cannot be changed
# items are indexed
# duplicates allowed
# purpose? for storing data that should not be modified, such as database records.
print(my_tuple.count(1))
print(my_tuple.index(3))

" Sets "
fruits = {"apple" , "banana" , "cherry"}
print(type(fruits))
print(len(fruits))
print(fruits)
# unordered
# unchangable but can add and remove
# do not accept duplicates
fruits.add("watermelon")
print(fruits)
fruits.remove('apple')
print(fruits)

# Duplicates
set1 = {"apple", "banana", "cherry", "apple", "banana", 55, 22}
print(set1)
set2 = {"apple", "banana", "cherry", True, 1, 2}
print(set2)
set2 = {"apple", "banana", "cherry", False, 0, 2}
print(set2)

# Joining Sets
veg = {"Tomato" , "Cucumber" , "lettuce"}
set3 = fruits.union(veg)
print(fruits)
print(veg)
print(set3)

fruits.update(veg)
print(fruits)

new = set1.intersection(set2)
print(set1)
print(set2)
print(new)
set1.intersection_update(set2)
print(set1)

# Practical 2
service_A_subscribers = {"xhamoodx_10", "moxsniper", "gamerxxx", "3bood_jld"}
service_B_subscribers = {"vemto_killer", "moxsniper", "xx_Ms_xx", "gamerxxx", "user902947"}

common_subAB = service_A_subscribers.intersection(service_B_subscribers)
print(service_A_subscribers)
print(service_B_subscribers)
print(common_subAB)

diff = service_A_subscribers.symmetric_difference(service_B_subscribers)
print(service_A_subscribers)
print(service_B_subscribers)
print(diff)

" Dictionaries "
student = {
    "Name":"Jamal",
    "Age":19,
    "Grade":10,
    "Number":"0553221",
    "ID":112233440
}
# changable
# ordered
# no duplicates
print(type(student))
print(len(student))
print(student)
print(student["ID"])

id = student["ID"]
print(id)
name = student.get("Name")
print(name)

keys = student.keys()
print(keys)
values = student.values()
print(values)

# replacing & adding
student["ID"] = 3321
print(student["ID"])
student.update({"Grade":11})
print(student["Grade"])
#replacing
student["ID"] = 3321
print(student["ID"])
student.update({"Grade":11})
print(student["Grade"])
#adding
student["Address"] = "UAE-Fujairah"
print(student["Address"])
student.update({"Score":82})
print(student["Score"])
print(student)

# removing
student.pop("ID")
print(student)
student.popitem()
print(student)
student.clear()
print(student)

# nested dictionaries
Players = {
    "Messi":{
        "Phone":90098731,
        "Address":"USA",
        "Position":"CAM"
    },
    "Ronaldo":{
        "Phone":21029382,
        "Address":"KSA",
        "Position":"ST"
    }
}
print(Players)
Players["Ronaldo"]["Address"] = "Madrid"
print(Players["Ronaldo"]["Address"])

" dict constructor "
# dict()
youtuber = dict(name = "MrBeast" , age = 55 , subs = "243M")
print(youtuber["name"])
#----------------------------------------------------------------------#