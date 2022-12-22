# class Point:
#     def __int__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
#
# # Constructors
#
# point = Point(20, 30)
# print(point.x)
# print(point.y)


class User(object):
    def __int__(self, name):
        self.name = name

    def talk(self):
        print("talk")


# Constructors
john = User()
john.name = "Stephen"
print(john.name)
john.talk()


# Inheritance

# class Dog:
#     def walk(self):
#         print("walk")
#
#
# class Cat:
#     def walk(self):
#         print("walk")


class Mammal:
    def walk(self):
        print("walk")


class Cat(Mammal):
    def jumps(self):
        print("jumps")


cat1 = Cat()
cat1.walk()
cat1.jumps()


class Dog(Mammal):
    def bark(self):
        print("barks")


# pass # if no function is aligned to it


dog1 = Dog()
dog1.bark()
dog1.walk()
