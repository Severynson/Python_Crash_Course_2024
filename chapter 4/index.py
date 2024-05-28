# magicians = ["alice", "david", "carolina"]
# print(magicians)
# for magician in magicians:
#     print(magician)

# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait your next trick {magician.title()}\n")

# print("Thank you everyone, yhat was a great show!")

# for value in range(1, 5):
#     print(value)

# print("\n")

# for value in range(6):
#     print(value)

# print("\n")

# numbers = list(range(1, 6))
# print(numbers, "\n")

# evenNumbers = list(range(2, 11, 2))
# print(evenNumbers, "\n")

# squares = []
# for value in range(1, 11):
#     square = value**2
#     squares.append(square)

# print(squares, "\n")

# digits = list(range(1, 10))
# digits.append(0)
# print(digits, "\n")
# digitsMin = min(digits)
# digitsMax = max(digits)
# digitsSum = sum(digits)
# print("minimum: ", digitsMin, "maxium: ", digitsMax, "sum: ", digitsSum, "\n")

# squares = [value**2 for value in range(1, 11)]
# print(squares)

# Try it yourself section:

# # 1:
# for value in range(1, 21):
#     print(value, "\n")

# # 2:
# oneMilion = list(range(1, 1_000_001))
# for element in oneMilion:
#     print(element)
# print("\n")

# ## 3:
# oneMilionMin = min(oneMilion)
# oneMilionMax = max(oneMilion)
# print(f"min: {oneMilionMin}, max: {oneMilionMax}")
# oneMilionSum = sum(oneMilion)
# print(f"sum: {oneMilionSum}\n")

# ## 4:
# oddNumbers = list(range(1, 21, 2))
# for num in oddNumbers:
#     print(num)
# print("\n")

# ## 5:
# multiplesOf3 = list(range(3, 31, 3))
# for num in multiplesOf3:
#     print(num)
# print("\n")

# ## 6:
# cubes = [value**3 for value in range(1, 11)]
# for cube in cubes:
#     print(cube)

# players = ["ron", "severyn", "ann", "davis"]
# # print(players[0:3])
# # print(players[:3])
# # print(players[3:])
# # print(players[:-3])
# # print(players[-3:])
# # print(players[0:-1:2])

# # loop through last 3 players:
# for player in players[-3:]:
#     print(player)
# print("\n")

# # loop through first 3 players:
# for player in players[:3]:
#     print(player)
# print("\n")

# my_foods = ["protein shake", "apples", "peanut butter", "milk"]
# my_friends_foods = my_foods[
#     :
# ]  # Now we can add favorite food not changing the initial my_foods list.

# # my_friends_foods = my_foods # This way we would break everythink,
# # # creating a reference for the same place in memory instead of making a copy!

# print(
#     f"My favourite foods are: {my_foods};\nMy friend's favourite foods are: {my_friends_foods};"
# )  # Copy, but not a reference!

# my_foods.insert(0, "Bagels")
# my_friends_foods.append("wafles")
# print(
#     f"Now my favourite foods are: {my_foods};\nAnd now my friend's favourite foods are: {my_friends_foods};"
# )  # Proving now, that it is a copy, but not a reference!

# # Try it yourself section:

# # # 1:
# print(f"The first 3 items in the list of my favourite foods are: {my_foods[:4]}")
# # # 2:
# print(f"The middle 3 items in the list of my favourite foods are: {my_foods[1:4]}")
# # # 3:
# print(f"The last 3 items in the list of my favourite foods are: {my_foods[-3:]}")


# # Tuple:

dimensions = (200, 50)
print(dimensions[1])  # Like a list, but immutable

tuple1 = (
    1,
)  # Tuple with 1 element necessarely has to have a coma after the first element,
# oterwise - it is just an integer surrounded by a rounded brackets.
print(*tuple1)

# dimensions[0] = 20 # Will cause an error - tuples are immutable!

dimensions = (200, 50)
print(dimensions)
dimensions = (400, 100)  # Reasigning a variable is fine, just don't change values.
print(dimensions)

print("\nMenue:")
buffet = ("piza", "burger", "beer", "cola", "grilled chicken")
index = 1
for meal in buffet:
    print(f"{index})The restaurant's buffet offers: {meal}")
    index = index + 1

print("\n\tMenue update for 2 meals\t\n")

buffet = (
    "piza",
    "burger",
    "wine",
    "sprite",
    "grilled chicken",
)  # reastaurant changes the menue. 2 meals are changed now.
index = 1
for meal in buffet:
    print(f"{index})The restaurant's buffet offers: {meal}")
    index = index + 1
