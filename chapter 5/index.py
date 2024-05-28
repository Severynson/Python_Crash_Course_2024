cars = ["audi", "subaru", "toyota", "bmw"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car)
print("\n")

answer = 17
if answer != 21:
    print("That is not a correct answer.")
print("\n")

age_1 = 21
age_2 = 16

if (age_1 and age_2) >= 21:
    print("Both people are older than 21.")
else:
    print("At least 1 person is younger than 21.")


if (age_1 or age_2) >= 21:
    print("At least 1 person is older than or exactly 21.")
else:
    print("Both people are younger than 21.")

existingUsers = ["user_1", "user_2", "user_3"]
new_user = "user_4"

# userAlreadyExist = False
# for user in existingUsers:
#     if user == new_user:
#         userAlreadyExist = True

# if userAlreadyExist:
#     print(f'User "{new_user}" already exist!')
# else:
#     existingUsers.append(new_user)
#     print("New user was added successfuly!")


if new_user not in existingUsers:
    existingUsers.append(new_user)
    print("New user was added successfuly!")
else:
    print(f'User "{new_user}" already exist!')

# if new_user in existingUsers:
#     print(f'User "{new_user}" already exist!')
# else:
#     existingUsers.append(new_user)
#     print("New user was added successfuly!")

cars = ["audi", "subaru", "merzedes"]

car = "subaru"
print("\nis car == 'subaru'? I predict True")
print(car == "subaru")
print("\nis car == 'audi'? I predict False")
print(car == "audi")
