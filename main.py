#Наслідування класів
class Grandparent:
    height = 170
    eyes = "green"
    age = 70
class Parent(Grandparent):
    age = 40
class Child(Parent):
    age = 15
    height = 165
    def __init__(self):
        print(self.height)
        print(self.eyes)
        print(self.age)

max = Child()
#приклад
class Human:
    height = 170
class Student(Human):
    pass
class Worker(Human):
    pass

nick = Student()
kate = Worker()
print(nick.height, kate.height)

#метод super()
class Hello:
    def __init__(self):
        print("Hello!")

class Hello_world(Hello):
    def __init__(self):
        super().__init__()
        print("World")

obj = Hello_world()