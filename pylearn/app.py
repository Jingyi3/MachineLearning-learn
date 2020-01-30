# print("Hello! Olivia!")
#
# print('o----')
# print(' ||||')
# print('*' * 10) # expression : a piece of code that produce a value
# #interpreter execute linebyline
#
# price = 10
# # convert to binary and store in
# rating = 4.9
# label = 'Olivia'
# is_published = False
# #variable should be lowercase, simple value up
# print(price)
#
# full_name = 'John Smith'
# age = 20
# is_exist = False
#
# # receive input
# # () calling the function
# name = input('what is your name? ')
# color = input('what is your favorite color? ')
# print(name + ' likes ' + color)


# # type conversion
# # int() function
# birth_year = input('Birth year: ')
# print(type(birth_year)) # <class 'str'>
# age = 2020 - int(birth_year) # <class 'int'>
# print(type(age))
# print(age)

# weight_pounds = input("what is your weight? ")
# weight_kg = float(weight_pounds) * 0.45
# print('weight in pounds is ' + weight_pounds + ', weight in kg is ' + str(int(weight_kg)))

# # Strings
# course = '''Python's for "Beginners"'''
# course2 = '''
# Hi John,
#
# Here is our first email to you
#
# Thank you,
# Support Team
#
# '''
# course3 = 'Python for beniggners'
# another = course3[:]
# print(another)
#
# # formatting String
# first = 'John'
# last = 'Smith'
#
# # John [Smith] is a coder
#
# message = first +' [' + last + '] is a coder'
# print(message)
#
# msg = f'{first} [{last}] is a coder'
# # define fromatting string use prefix f and use curly braces{to dynamiclly insert value to string}
# print(msg)

# # String Methods
# course = 'Python for Beginners'
# print(len(course))
# # len is general purpose fuc
#
# print(course.lower())
# # the String method does not change the original string and create a new string and return it
# print(course)
#
# print(course.replace('Beginners', 'Absolute Beginners'))
# print('Absolute' in course)

#  Arithmetic Operation

# x = 2.9
# print(round(x))

# import math
# print(math.floor(2.9))


# is_hot = False
# is_cold = False
#
# if is_hot:
#     print("It's a hot day")
# elif is_cold:
#     print("It's a cold day.")
# else:
#     print('It is a lovely day')
# print('Enjoy your day!')


# house_price = 1000000
# # buyer_credit = int(input('Credit of the buyer: '))
# # if buyer_credit > 5:
# #     print('house price is: ' + str(house_price*0.9))
# # else:
# #     print('house price is: ' + str(house_price*0.8))
#
# has_good_credit = True
#
# if has_good_credit:
#     down_payment = 0.1 * house_price
# else:
#     down_payment = 0.2 * house_price
#
# print(f"Down payment: ${down_payment}")
#
#


# has_high_income = True
# has_good_credit = True
# has_criminal_record = False
#
# if has_good_credit and has_high_income and not has_criminal_record:
#     print("Eligible for loan")
#


# temperature = 30
#
# if temperature > 30:
#     print('hot')
# else:
#     print('not hot')

# name1 = input('input your name: ')
# len_name = len(name1)
# if len_name < 3:
#     print('name must be at least 3 chars')
# elif len_name > 10:
#     print('name can be max of 50 chars')
# else:
#     print('good name!')


# weight = int(input('Weight: '))
# unit = input('(L)bs or (K)g: ')
# # if unit.__eq__('l'or'L'):
# if unit.upper() == 'L':
#     weight *= 0.45
#     unit = 'kilos'
# # elif unit.__eq__('k'or'K'):
# else:
#     weight /= 0.45
#     unit = 'pounds'
#
# print(f"You are {weight} {unit}")


# help_info = '''start - to start the car
# stop - to stop the car
# quit - to exit'''
# is_start = False
#
# while True:
#     usr_input = input('> ').lower()
#     if usr_input == 'quit':
#         break
#     elif usr_input == 'help':
#         print(help_info)
#     elif usr_input == 'start' and not is_start:
#         is_start = True
#         print('Car started ... Ready to go!')
#     elif usr_input == 'start' and is_start:
#         print('Car is already started!')
#     elif usr_input == 'stop' and is_start:
#         is_start = False
#         print('Car stopped.')
#     elif usr_input == 'stop' and not is_start:
#         print('Car is already stopped!')
#     else:
#         print("I don't understand that... ")
#

# for item in 'Python':
#     print(item)

#
# for item in ['bob', 'olivia', 'max']:
#     print(item)

# for item in range(2, 8, 2):
#     print(item)

# prices = [10, 20,30]
# sum = 0
# for price in prices:
#     sum += price
#
# print(f"total: {sum}")


# for x in range(4):
#     for y in range(5):
#         print(f"(x, y) = ({x}, {y})")

# numbers = [5, 2, 5, 2, 2]
#
# for num in numbers:
#     # print('*' * num)
#     output = ''
#     for count in range(num):
#         output += '*'
#     print(output)

# names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
# names[0] = 'Jon'
# print(names[2:4])
# print(names)
#

# # find the largest number
# numbers = [3,6,2,8,4]
# max_num = numbers[0]
# for num in numbers:
#     if num > max_num:
#         max_num = num
# print(f"Max number is {max_num}")

# # matrix
# matrix = [
#     [1, 2, 3],
#     [3, 4, 5],
#     [6, 7, 8]]
# print(matrix[1][2])
#
# for row in matrix:
#     for item in row:
#         print(item)


# numbers = [3,6,2,3,8,4]
# numbers_copy = numbers.copy()
#
# numbers.append(20)
# numbers.insert(1, 10)
# print(numbers)
# numbers.remove(20)
# print(numbers)
# numbers.pop()
# print(numbers)
# print(numbers.index(6))
# print(50 in numbers)
# print(numbers.count(3))
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
#
# print(numbers_copy)

# # remove duplicate
#
# numbers = [3, 6, 2, 3, 8, 3, 6, 5, 9, 4]
# unique = []
#
# for num in numbers:
#     if num not in unique:
#         unique.append(num)
#
# curr_idx = 0
# for num in numbers:
#     dup_idx = curr_idx + 1
#     for item in numbers[dup_idx :]:
#         if item == num:
#             numbers.pop(numbers[dup_idx])
#         dup_idx += 1
#     curr_idx += 1
#
# print(numbers)
# print(unique)

#
# # Tuple
# coordinates = (1, 2, 3)
# x, y, z = coordinates
# print(z)


# # dictionary
# customer = {
#     "name": "John",
#     "age": 30,
#     "is_verified": True
# }
#
# # add new key and value
# customer["sex"] = "male"
#
# print(customer.get('birthday', 'Jan 1 1999'))
# print(customer['sex'])
#
# digits_mappinf = {
#     '1': 'one',
#     '2': 'two',
#     '3': 'three',
#     '4': 'four'
# }
# input_phone = input('Phone: ')
# output = ''
# for item in input_phone:
#     output += digits_mappinf.get(item, '!') + ' '
# print(output)
#
# message = input("> ")
# words = message.split(' ')
# emojis = {
#     ":)": "😀",
#     ":(": "😭"
# }
#
# output = ''
# for word in words:
#     output += emojis.get(word, word) + ' '
#
# print(output)

#
# # Functions
#
# def greet_user(first_name, last_name):
#     print(f'hi {first_name} {last_name}！')
#     print('welcome!!!')
#
#
# print("start")
# greet_user("john", "smith")
# greet_user("mary", "zhao")
# greet_user(last_name='Zhuang', first_name='Jenny')
# print("finish")
#


# def square(number):
#     return number * number
#
#
# result = square(3)
# print(result)


# def emoji_converter(message):
#     words = message.split(' ')
#     emojis = {
#         ":)": "😀",
#         ":(": "😭"
#     }
#     output = ''
#     for word in words:
#         output += emojis.get(word, word) + ' '
#     return output
#
#
# message = input("> ")
# print(emoji_converter(message))
#
# try:
#     age = int(input('Age: '))
#     income = 20000
#     risk = income/age
#     print(age)
# except ZeroDivisionError:
#     print('age cannot be 0')
# except ValueError:
#     print('invalid value')

# Classes

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()
#
# point2 = Point()
# point2.x = 1
# print(point2.x)


# point = Point(10, 20)
# point.x = 11
# print(point.x)

# class Person:
#     def __init__(self, name):
#         self.name = name
#     def talk(self):
#         print(f"Hi, I am {self.name}")
#
#
# person1 = Person('John')
# person1.talk()
#
# bob = Person('Bob Smith')
# bob.talk()


# class Mammal:
#     def walk(self):
#         print("walk")
#
#
# class Dog(Mammal):
#     def bark(self):
#         print("bark!!")
#
#
# class Cat(Mammal):
#     def walk(self):
#         print("cat walk")
#
#
# dog1 = Dog()
# dog1.walk()
# dog1.bark()
#
# cat1 = Cat()
# cat1.walk()

# Module


