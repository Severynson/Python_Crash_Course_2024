class Car:
    def __init__(self, brand, car_mileage):
        self.brand = brand
        self.car_mileage = car_mileage
        self.APROPRIATE_FUEL = "gas"

    def print_mileage(self):
        print(f"{self.brand}'s current mileage is {self.car_mileage} miles.")

    def update_odometer(self, new_mileage):
        if new_mileage >= self.car_mileage:
            self.car_mileage = new_mileage
            print(f"{self.brand}'s mileage was updated to: {new_mileage} miles.")
        else:
            print(
                "Don't cheat against the next owner, you can not decrease the mileage."
            )

    def increment_odometer(self, miles_to_add):
        old_mileage = self.car_mileage
        if miles_to_add < 0:
            print("Don't try to trick me, I catched your intend ;D")
        else:
            self.car_mileage += miles_to_add
            print(
                f"{self.brand}'s mileage was incremented by {miles_to_add} miles, before it was {old_mileage} miles and now is {self.car_mileage} miles."
            )

    def fill_gas_tank(self):
        print(
            f"{self.brand}'s tank was filled with {self.APROPRIATE_FUEL} up to the 100%"
        )

    def beep(self):
        print("Beep. I'm a tiny car.")
