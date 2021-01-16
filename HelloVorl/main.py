
#A bugged out class
class Person:
    def __init__(self, name, age):
        self.name = age
        self.age = name

    def identify(self):
        print(f"Hello. My name is {self.name}, age {self.age}.")

age = int(input("How old are you?"))
name = input("What is your name?")
print(f"My name is {name}, and I am {age} years old.")

peepo = Person(name, age)
peepo.identify()

