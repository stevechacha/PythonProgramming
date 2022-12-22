# List
names = ["Chacun", "David", "Mita"]
print(names)

# Accessing Elements in a list
print(names[0])

# modifying Elements in a list
names[0] = "Chacha"
print(names)
print("names list length: ", len(names))

# Adding EElements in a list

names.append("Marwa")
print(names)

# List Methods
numbers = [1, 2, 3, 4, 5]
numbers.insert(-1, 10)
numbers.pop(0)  # Remove by index
numbers.remove(10)  # Remove by value
numbers.sort()

# Organizing a list

values = [2, 4, 6, 3, 6, 12, 4, 2, 4, 612, 4, 53, 1, 3]
values.sort()  # sort permanently
print(values)

sorted(names)
print(names)

values.reverse()
print(values)

print(10 in numbers)  # Returns boolean if exist in the number
print(len(numbers))  # Return the number of the values

# While Loop

i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1

# For Loops
for item in numbers:
    print(item)

# Range
numbers = range(0, 10)
for number in numbers:
    print(number)

# range(start value, end value, step)
for value in range(0, 20, 2):
    print(value)
