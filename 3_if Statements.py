

# if statement

temperature = 35

if temperature > 30:
    print("it is a hot day")
    print("Drink alot of water")

voting_age = int(input("Enter your age: "))

if voting_age > 18:
    print("Can participate in Election  Voting")

else:
    print("Not valid for voting")

weight = float(input("Weight: "))
unit = input("(Kg) or (L)bs: ")

if unit.upper() == "Kg":
    converted = weight / 0.45
    print("weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))

