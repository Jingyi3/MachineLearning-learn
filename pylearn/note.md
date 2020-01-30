### String

len()
.upper
.lower
.title 方法返回'标题化'的字符串,就是说所有单词都是以大写开始，其余字母均为小写
.find
.replace

'...' in string


### Arithmetic Operation
/ return float
// return  int
10 ** 3 10的三次方 10 to the power of 3
augumented assignment operator +=

order of operations:
    exponentiation 2 ** 3
    multiplication or division
    addition or subtraction

### Math Function
import math

### If statement

    else is ==> elif

```python
is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
elif is_cold:
    print("It's a cold day.")
else:
    print('It is a lovely day')
print('Enjoy your day!')
```  
```python
house_price = 1000000
# buyer_credit = int(input('Credit of the buyer: '))
# if buyer_credit > 5:
#     print('house price is: ' + str(house_price*0.9))
# else:
#     print('house price is: ' + str(house_price*0.8))

has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * house_price
else:
    down_payment = 0.2 * house_price

print(f"Down payment: ${down_payment}")
```

### Logical operators

`and`, `or`, `not`

```python
has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_good_credit and has_high_income and not has_criminal_record:
    print("Eligible for loan")


``` 


### comparision operators

`==`, `!=`

```python
name1 = input('input your name: ')
len_name = len(name1)
if len_name < 3:
    print('name must be at least 3 chars')
elif len_name > 10:
    print('name can be max of 50 chars')
else:
    print('good name!')
```

```python
weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
# if unit.__eq__('l'or'L'):
if unit.upper() == 'L':
    weight *= 0.45
    unit = 'kilos'
# elif unit.__eq__('k'or'K'):
else:
    weight /= 0.45
    unit = 'pounds'

print(f"You are {weight} {unit}")
```

### loop
#### while loop
``` 
while condition:
    ...
    if condition:
        break
else:
     if the if statement execute break
    then the else part will not execute
    ...
```

```python
i = 1
while i <= 5:
    print('*' * i)
    i += 1
```  

result  

```
*
**
***
****
*****

Process finished with exit code 0

```

#### for loop

```python
for item in range(2, 8, 2):
    print(item)
```

#### nested loop

like coordinates
```python
for x in range(4):
    for y in range(5):
        print(f"(x, y) = ({x}, {y})")

```

```python
numbers = [5, 2, 5, 2, 2]

for num in numbers:
    # print('*' * num)
    output = ''
    for count in range(num):
        output += '*'
    print(output)
```

Actually `print('*' * num)` is a loop, so if only write this code it is also a nested loop

### List

`[ : ]` it does not modify the original list, just simply return a new list
```python
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names[2:4])
```

#### remove an item
`remove(item)` remove the item  
`pop(index)` if `index` is empty, remove the last item, else remove the specific index item

```python
# remove duplicate

numbers = [3, 6, 2, 3, 8, 3, 6, 5, 9, 4]
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

curr_idx = 0
for num in numbers:
    dup_idx = curr_idx + 1
    for item in numbers[dup_idx :]:
        if item == num:
            numbers.pop(numbers[dup_idx])
        dup_idx += 1
    curr_idx += 1

print(numbers)
print(unique)
```

#### 2D List
```python
# matrix
matrix = [
    [1, 2, 3],
    [3, 4, 5],
    [6, 7, 8]]
print(matrix[1][2])

for row in matrix:
    for item in row:
        print(item)
```

### Tuple
tuple is immutable

### Unpacking
```python
coordinates = (1, 2, 3)
x, y, z = coordinates
```


### Dictionary

`customer.get('birthday', 'Jan 1 1999')` if the `key` does not exist, then will give it a default value


### Emoji Converter
`control`+`command`+`space`  
```python
message = input("> ")
words = message.split(' ')
emojis = {
    ":)": "😀",
    ":(": "😭"
}

output = ''
for word in words:
    output += emojis.get(word, word) + ' '

print(output)
```

result:
```
> good morning sunshine :)
good morning sunshine 😀 

```


### Function

 **always add two empty lines after a function**
 
 #### Parameter VS Argument
 
 `Parameter` define in the function definition  
 `Argument` is the really value passing in when calling the function
 
 #### Keyword argument
 
 - when passing the numerical value, improving the readability of your code
 the position of the argument doesn't matter  
 - when mixing the positional argument and keyword argument, you should always use positional arguments first and then keyword arguments  
 
 #### return statement
 
 By default, python return `None` of every function
 
 #### function: emoji converter
 
 ```python
def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😀",
        ":(": "😭"
    }
    output = ''
    for word in words:
        output += emojis.get(word, word) + ' '
    return output


message = input("> ")
print(emoji_converter(message))
```


### Exceptions

```python
try:
    age = int(input('Age: '))
    income = 20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print('age cannot be 0')
except ValueError:
    print('invalid value')
```


### Classes

`Pascal naming convention` define a `class` name capitalize the first letter of ever word


define a class Point, giving the object attributes
```python
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)
```


#### Constructor

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

###
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")


person1 = Person('John')
person1.talk()

bob = Person('Bob Smith')
bob.talk()
```


### Inheritance

```python
class Mammal:
    def walk(self):
        print("walk")
     
     
class Dog(Mammal):
    pass
```

### Module

two ways: import entire module or import specific functions
```python
import pylearn.converters
print(pylearn.converters.kg_to_lbs(70))

from pylearn.converters import kg_to_lbs
print(kg_to_lbs(70))
```

### Random

```python
import random


for i in range(5):
    random.random() # random float number from 0 to 1
    print(random.randint(1,20))

members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)


class Dice:
    def roll(self):
        result_tuple = (random.randint(1, 6), random.randint(1, 6))
        return result_tuple

    def roll2(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second  # automaticly convert them to tuple


dice1 = Dice()
print(dice1.roll())
print(dice1.roll2())
```

