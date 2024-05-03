print("Hello World")
age = 29
first_name = "Smart"
last_name = "Chris"
is_online = False
print("He is", first_name, last_name)

print("He is", age)
print(is_online, "He is not online")
print("Happy birthday,", first_name, last_name, "in advance!")

# trying out input
name = input("What is your name? ")
print("Hello", name)
print("I will be ", age, "years old in few years time")
print("I am married to " + first_name + " " + last_name)

birth_year = input("Enter your birth year: ")
present_age = 2024 - int(birth_year)
print(present_age)

first = 10.1
second = 20
sum = first + second
# sum = float(first) + int(second)
print(sum)

course = 'Python for Beginner'
print(course.upper())
print(course.find('y'))
# python is case sensitive
print(course.replace('for', '4'))
print(course.find('for'))
print('Python' in course)

#Arithmetic Operations in Python
print(10 + 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

x = 10
# print(x := int(x + 3))  # is the same as # it is known as augmented assignment operator
x += 3
print(x)

x -= 3
print(x)

x *= 3
print(x)

x /= 3
print(x)

y = 4 + 5 * 2
print(y)

z = (4 + 5) * 2
print(z)

# comparism in python, == is use for comparism, we also have >=, <= and <b
x = 3 > 2
print(x)

y = 3 == 2
print(y)

z = 3 != 2
print(z)

# logical operators which are and, or and not
price = 25
time = 5
print(price > 10 and price < 30)
print(time > 10 or time < 30)
print(not time > 10)

# if statements in python
temperature = 35
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold")
else:
    print("It's cold")
print("Done")

weight = int(input("Weightt: "))
unit = (input("(K)g or (L)bs: "))
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kg: " + str(converted))






