alien_0 = {"color": "green", "points": 5}
print(alien_0["color"], alien_0["points"])

alien_0 = {}
alien_0["color"] = "green"
alien_0["points"] = 5
print(alien_0["color"], alien_0["points"])

alien_0["color"] = "yellow"
print(alien_0["color"], alien_0["points"])

alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium", "points": 5}

print(f"Original x-position: { alien_0['x_position']}")
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3
alien_0["x_position"] = alien_0["x_position"] + x_increment
print(f"New x-position: { alien_0['x_position']}")

print(f'Before the key-value pair "points" deletion: {alien_0}')
del alien_0["points"]
aliensPoints = alien_0.get("points", "No key-value pair assigned.")
# While alien_0["points"] instead of .get() would simly case an uncatched error.
print(f"Aliens points: {aliensPoints}")
print(f'After the key-value pair "points" deletion:  {alien_0}\n')

user_0 = {"username": "severynson", "first": "severyn", "last": "kurach"}

for key, value in user_0.items():
    print(f"KEY: {key};\nVALUE: {value}\n")

favourite_languages = {
    "severyn": "python",
    "andrew": "ruby",
    "dora": "go-lang",
    "john": "python",
}
for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language}.")

print("\n")

# for name in favourite_languages.keys():
for name in favourite_languages:  # Works exactly the same;
    print(f"{name.title()} participated in the poll.")

print("\n")

for language in favourite_languages.values():  # Works exactly the same;
    print(
        f"{language.title()} was mentioned in the poll, so it is a popular programing language."
        # Ooops, repeating happens here.
    )
print("\n")

favourite_languages_without_repeating = set(favourite_languages.values())
for language in favourite_languages_without_repeating:  # Works exactly the same;
    print(
        f"{language.title()} was mentioned in the poll, so it is a popular programing language."
        # Ooops, repeating happens here.
    )
print("\n")

alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
print("\n")

aliens = []
new_alien = {"color": "green", "points": 5, "speed": "slow"}
for alien_number in range(30):
    aliens.append(new_alien.copy())

print("Aleins: \n", *aliens, "\n")
print(f"The total number of aliens: {len(aliens)}\n")

pizza = {"crust": "thick", "toppings": ["mushrooms", "extra cheese"]}
print(f'\nYou ordered a {pizza.get("crust")}-crust pizza\nwith the following toppings:')
index = 0
for topping in pizza["toppings"]:
    index += 1
    print(f"{index}) With {topping}")
print("\n")

favourite_languages = {
    "jen": ["Go-lang", "Ruby"],
    "edward": ["Python", "JavaScript"],
    "sarah": ["TypeScript", "Ruby"],
    "phill": ["JavaScript"],
}

for name, languages in favourite_languages.items():
    if len(languages) > 1:
        print(f"{name.title()}'s favourite languages are:")
    else:
        print(f"{name}'s favourite language is:")
    index = 0
    for language in languages:
        index += 1
        print(f"{index}) {language};")
