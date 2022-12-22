# Input function

name = input("what is your name? ")
print("Hellow world \n" + name)  # new line
print("Hellow world \t" + name)  # tab space

birth_year = input("Enter the year of birt:  ")
current_age = 2022 - int(birth_year)
print(current_age)

# Calculate

first_number = input(" Enter the first Number: ")
second_number = input("Enter the Second Number: ")

sum_integer = int(first_number) + int(second_number)
print("Sum of integer :", sum_integer)

float_first = float(input(" Enter the float_first Number: "))
float_second = float(input("Enter the float_second number: "))

sum_float = float_first + float_second
print("Sum of the float: ", sum_float)