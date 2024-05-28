from Car import *


class Truck(Car):

    def __init__(self, brand, car_mileage, **args):
        super().__init__(brand, car_mileage)
        self.carring_cargo = (
            (args.get("carring_cargo"))
            if (args.get("carring_cargo") is not None)
            else False
        )
        self.APROPRIATE_FUEL = "disel"

    def load_cargo(self):
        if not self.carring_cargo:
            self.carring_cargo = True
            print("The cargo was loaded.")
        else:
            print(
                "The truck already had a cargo. No more room for the additioal cargo."
            )

    def remove_cargo(self):
        if self.carring_cargo:
            self.carring_cargo = False
            print("The cargo was removed.")
        else:
            print("There is no cargo to remove yet.")

    def beep(self):
        print("BEEEEEEP!!! I'm a truck!")
