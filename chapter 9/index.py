from Dog import Dog

myDog = Dog("Willie", 3)

myDog.bark_age()
myDog.roll_over()
myDog.sit()
myDog.roll_over()

print(f"My dog's name is {myDog.name}.\n")

myDog = Dog("Rex", 1)
myDog.roll_over()
myDog.bark_age()
myDog.display_bride()
myDog.bride = "Terier"
myDog.display_bride()

print(myDog)
# print(myDog.hasFifthLeg) # It is possible to add a new property to the existing object, but just prohibited to access them before their creation
myDog.mutate()
print(myDog.hasFifthLeg)

from Restaurant import Restaurant

mc_donalds = Restaurant("MC donald's", False)
tim_hortons = Restaurant("Tim hortons", False)

print(
    f"The inital MC Donald's status: isOpen = {mc_donalds.isOpen}, so {mc_donalds.get_opening_status()}."
)
mc_donalds.toggle_restaurant_oneping_status()
mc_donalds.toggle_restaurant_oneping_status()
mc_donalds.toggle_restaurant_oneping_status()
print(
    f"The inital MC Donald's status: isOpen = {tim_hortons.isOpen}, so {tim_hortons.get_opening_status()}."
)

print(
    f"The inital MC Donald's status: isOpen = {tim_hortons.isOpen}, so {tim_hortons.get_opening_status()}."
)
mc_donalds.toggle_restaurant_oneping_status()
mc_donalds.toggle_restaurant_oneping_status()
print(
    f"The inital MC Donald's status: isOpen = {tim_hortons.isOpen}, so {tim_hortons.get_opening_status()}."
)

from Car import Car

merzedes = Car("Merzedes", 12)

merzedes.update_odometer(16)
merzedes.update_odometer(1)
merzedes.update_odometer(2)
merzedes.update_odometer(300)
merzedes.update_odometer(299)
merzedes.update_odometer(301)

merzedes.increment_odometer(-21)
merzedes.increment_odometer(9)
merzedes.increment_odometer(25)

from Truck import Truck

general_motors = Truck("GM", 2522, carring_cargo=True)
general_motors.print_mileage()
general_motors.remove_cargo()
general_motors.load_cargo()
general_motors.load_cargo()
general_motors.remove_cargo()

general_motors.fill_gas_tank()
merzedes.fill_gas_tank()

general_motors.beep()
merzedes.beep()

from random import randint


def roll_a_dice():
    "Simulate rolling a standard 6 sides dice and print the result."
    six_sides_dice = randint(1, 6)
    print(six_sides_dice)


roll_a_dice()
roll_a_dice()

team_1 = ("severyn", "roman", "natalie", "deniel", "ann")
team_2 = ["john", "betty", "marry", "dean", "zbignew"]


def russian_roulette(players):
    from random import choice

    chosen_player = choice(players)
    print(f"{chosen_player.title()} died this time :/")
    if type(players) == list:
        players.remove(chosen_player)
        print(f"List of players who stayed alive: {players}")


russian_roulette(team_1)
russian_roulette(team_2)
russian_roulette(team_2)
russian_roulette(team_2)
russian_roulette(team_2)
