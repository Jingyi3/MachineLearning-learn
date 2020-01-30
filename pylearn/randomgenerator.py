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
