# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = [human.name for human in humans if human.name[0] == 'D']
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [human.name for human in humans if human.name[-1] == 'e']
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = [human.name for human in humans if human.name[0] in ['C','D','E','F','G']]
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [(human.age+10) for human in humans]
print(d)
dplus = [(f"{human.name}'s age in 10 yrs",human.age + 10) for human in humans]
print(dplus)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [f'{human.name}-{human.age}' for human in humans]
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(human.name,human.age) for human in humans if human.age in range(27,33)]
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase: with age + 5\n")
olderhumans = map(lambda h : Human(h.name,h.age+5),humans)  #using map and a lambda func

print('original humans', humans)

print('\nolder humans using map\n') 
print(list(olderhumans))

print('\nolder humans using list comprehension:\n')
olderhumanscomprehension = [Human(h.name,h.age+5) for h in humans]  #using list comp
print(olderhumanscomprehension)



# olderhumans = [*humans]
# print('copy of humans array', olderhumans)
# for h in olderhumans:
#     h = Human(h.name, h.age+5)  #not sure why this didn't map each human to be a new human instance
# print('olderhumans', olderhumans)
# print('original humans', humans)

# newhuman = Human(humans[0].name, humans[0].age+10)  #testing out creating new human instance
# print('newhuman', newhuman)

# Write a list comprehension that contains the square root of all the ages.

print("Square root of ages:")
import math
h = [round(math.sqrt(human.age),2) for human in humans]
print(h)
