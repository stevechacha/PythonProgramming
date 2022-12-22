# Functions
def function_name(parameter, parameter2):
    print("Hellow world")
    print(parameter, parameter2)


function_name("argument of  parameter", "argument of parameter2")


def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")


greet("Stephen", "Chacha")


# Types of Functions
# 1 - Perform a task
# 2 = Return a value

def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Stephen Chacha")
file = open("content.xls", "w")
file.write(message)


# Keyword arguments

def increment(number, by):
    return number + by


print(increment(2, by=1))


# Return default value
# optional parameters should come after the default parameters

def increments(number, another, by=3):
    return number + another + by


print(increments(2, 2))


# Multiple numbers in a functions
def multiply(*values):
    total = 1
    for number in values:
        total = total * number
    return total


print(multiply(2, 4, 5, 6, 7))


# Functions with args

def save_user(**user):
    print(user)


save_user(id=1, first_name="Stephen", last_name="Chacha")


def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz(8))

secrete_value = 9
guess = 0
guess_limit = 3

while guess < guess_limit:
    guess_value = int(input("Guess: "))
    guess += 1
    if guess_value == secrete_value:
        print("You Won")
        break

else:
    print("You failed")


def emoji_converter(message):
    words = message.split("")
    emojis = {
        ": )": "lag",
        ": (": "Sad"
    }
    output = ""
    for word in words:
        output += emojis.get(word, words) + ""
    return output


message = input(">")
print(emoji_converter(message))
