# message = input("Tell me smth, and I'll repeat it back to you: ")
# print(message)

# # Personalized output:
# name = input("Please enter your name: ")
# print(f"Hello, {name}!")


# # How to treat input if we want to gather an integer from there:
# age = int(input("How old are you? : "))
# if age >= 18:
#     print("You can vote.")
# else:
#     print("You are too young to vote!")


# # My first python while loop!
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# numbersSize = int(input("Enter how many numbers are you going to store: "))
# index = 1
# numbers = []
# while index <= numbersSize:
#     numToStore = int(input(f"Enter your {str(index)} number for me to memorize: "))
#     numbers.append(numToStore)
#     index += 1


# print("Your numbers were:")
# for number in numbers:
#     print(f"{number},")

# # Count until user will decide to exit:

# # Implementation 1:

# index = 0
# print("I'll count until you'll decide to exit:")
# while (
#     input('Enter "x" if you want me  to stop or any other letter to proceed: ').lower()
#     != "x"
# ):
#     index += 1
#     print(index)
# print("Ok, I'll stop to count.")

# # Implementation 2:

# print("I'll count until you'll decide to exit:")
# want_to_stop = False
# index = 0
# while not want_to_stop:
#     match input(
#         'Enter "x" if you want me  to stop or any other letter to proceed: '
#     ).upper():
#         case "X":
#             print("Ok, I'll stop to count.")
#             want_to_stop = True  # Or we can just use break to exit the loop
#         case _:
#             index += 1
#             print(index)

# # Implementation 3:

# index = 0
# while True:
#     inputLetter = input(
#         'Enter "x" if you want me  to stop or any other letter to proceed: '
#     ).upper()

#     if inputLetter == "X":
#         print("Ok, I'll stop to count.")
#         break
#     index += 1
#     print(index)

# Python infinite loop runs successfuly very long without crushing, exceeding memory like in JS in some reason!
# infiniteLoopIteration = 0
# while True:
#     infiniteLoopIteration += 1
#     print(f"Infinite python loop iterates {infiniteLoopIteration} time")


# pizza_toppings = []
# new_toping = ""

# while True:
#     new_toping = input("Enter the next topping for a pizza, or enter 'x' to finish: ")
#     if new_toping.upper() == "X":
#         break
#     else:
#         pizza_toppings.append(new_toping)

# if len(pizza_toppings) > 0:
#     print("Pizza with the following toppings")
#     for topping in pizza_toppings:
#         print(f"{topping},")
#     print("is ready now!")
# else:
#     print("Pizza basis with no toppings is ready")

# unconfirmed_users = ["severyn", "den", "bria", "alla", "nick", "alice"]
# confirmed_users = []

# print("Starting verification process:")
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     confirmed_users.append(current_user)
#     print(f"\t- {current_user.title()} was verified and confirmed successfuly.")
# print("All users were verified successfuly.")

# cocentration_camp = ["jew", "aryan", "indian", "gypsy", "black", "asian", "jew"]
# while "jew" in cocentration_camp:
#     cocentration_camp.remove("jew")
#     print("Jew was destroyed")
# print("New ideal society is ready! (NO, never again...)")

# responses = {}
# polling_active = True
# while polling_active:
#     name = input("\nWhat is your name? :")
#     response = input("\nWhich mountain would you like to climb some day? :")
#     responses[name] = response
#     if input("\nWould you like to let another person respond?").upper() == "NO":
#         polling_active = False
# print("\nPoll results:")
# for name, response in responses.items():
#     print(f'-{name} responds: "{response}"')
