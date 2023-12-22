"""
Take the Dog and Cat classes you built in the last practice and
override the greeting method to give the following output:

Dog: "Hello <NAME>, my name is <DOG_NAME> and I'm a dog! 🐶"
Cat: "Hello <NAME>, my name is <CAT_NAME> the cat and I hate you. 😾"
"""
class Animal:
    def __init__(self, animal_name):
        self.animal_name = animal_name

    def greeting(self, name):
        print(f"Hello {name}, I'm {self.animal_name}")

class Dog(Animal):
    def greeting(self, name):
        print(f"Hello {name}, my name is {self.animal_name} and I'm a dog! 🐶")

class Cat(Animal):
    def greeting(self, name):
        print(f"Hello {name}, my name is {self.animal_name} the cat and I hate you (unless you give me catnip). 😾")

new_dog = Dog("Spot")
new_cat = Cat("Mr Rogers")
new_dog.greeting("Colin")
new_cat.greeting("Colin")
