# def greet_simple():
#     "Display a simple greeting"
#     print("Hello world!")


# greet_simple()


# def greet_user(name):
#     "Display a simple greeting to the provided user's name"
#     print(f"Hello {name.lower().title()}!")


# greet_user("sEveryN")


# def function_with_2_arg(arg_1="Seveyn", arg_2="Kurach"):
#     "Just a simplest function with 2 arguments"
#     print(f"Argument 1 was: {arg_1}, 2nd argument was: {arg_2};")


# function_with_2_arg("A.C.", 666)
# function_with_2_arg(
#     "A.C.",
# )
# function_with_2_arg(arg_2=333)
# function_with_2_arg()


# def fullname(firstname, secondname):
#     "returns the formated fullname"
#     return f"{firstname.lower().title()} {secondname.lower().title()}"


# myFullname = fullname("Severyn", "Kurach")
# print(f"myFullname now stores the value: {myFullname}")


# def personDataColector(name, age):
#     "Colects the person's data and return a dictionary"
#     return {"name": name.lower().title(), "age": age}


# severyn = personDataColector("seveyn", 22)
# print(f"Information about the person: {severyn}")

# facebook_users = ["severy", "molly", "ann"]
# instagram_users = ["annet", "den", "boris", "winston"]


# def greet_all_users(users):
#     "Greet all the users from the provided list"
#     for user in users:
#         print(f"Hello {user.lower().title()}!")
#     print("\n")


# greet_all_users(facebook_users)
# greet_all_users(instagram_users)


# def waiter():
#     "He'll record all the ingredients you want."
#     dressings = []
#     while True:
#         dressing = input("Enter the dressing title, or enter 'x' to quit: ").lower()
#         if dressing == "x":
#             break
#         else:
#             dressings.append(dressing)
#     print("\n")
#     return dressings


# products = waiter()


# def pizzaiolo(ingredients):
#     "He'll cook any pizza you like, just tell him all dressings you want!"
#     print("Cooking the pizza with:")
#     for ingredient in ingredients:
#         print(f"-{ingredient.title()}")
#     print("\n")


# pizzaiolo(products)


# def pizzaiolo(*ingredients):
#     "He'll cook any pizza you like, just tell him all dressings you want!"
#     print("Cooking the pizza with:")
#     for ingredient in ingredients:
#         print(f"-{ingredient.title()}")
#     print("\n")


# pizzaiolo(products[0], products[1], products[2])


# def pizzaiolo(size, *ingredients):
#     "He'll cook any pizza you like, just tell him all dressings you want!"
#     size = f'{size}"' if type(size) == int else size
#     print(f"Cooking the {size}-size pizza with:")
#     for ingredient in ingredients:
#         print(f"-{ingredient.title()}")
#     print("\n")


# pizzaiolo(22, "tomatos", "cheese", "salami")
# pizzaiolo("XL", "tomatos", "cheese", "salami")


# def build_profile(first, last, **user_info):
#     "Building a dictionary containinng everything we  know about the user"
#     user_info["first_name"] = first.lower().title()
#     user_info["last_name"] = last.lower().title()
#     return user_info

# I import method:
import profile_manager

user_profile_1 = profile_manager.build_profile(
    "albert", "einsteing", location="princeton", field="physics"
)

print(user_profile_1)

# II import method:
from name_lib import fullname

myFullname = fullname("severyn", "kurach")
print(myFullname)

# III import method:
from name_lib import fullname as createFullname

myFullname = createFullname("severyn", "kurach")
print(myFullname)

# IV import method:
import profile_manager as p_m

user_profile_1 = p_m.build_profile(
    "albert", "einsteing", location="princeton", field="physics"
)

print(user_profile_1)

# V import method:

from profile_manager import *

user_profile_1 = build_profile(
    "albert", "einsteing", location="princeton", field="physics"
)

print(user_profile_1)
