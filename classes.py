class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am a {self.gender}.")
        
person1 = Person('Rachael', 25, 'Female')

print(person1.introduce())