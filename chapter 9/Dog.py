class Dog:
    "A simple attemp to model a dog"

    def __init__(self, name, age, bride="mixed"):
        "Initialize name & age attributes."
        self.age = age
        self.name = name
        self.bride = bride

    def sit(self):
        "Simulate a dog sitting in response to a command."
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        "Simulate a roll over in response to a command."
        print(f"{self.name} rolled over.")

    def display_bride(self):
        print(f'{self.name}\'s bride is "{self.bride}"')

    def bark_age(self):
        "God will bark as many times as its age is (1 bark = 1 year)."
        for _ in range(self.age):
            print("Bark!", end=" ")
        print("\n")

    def mutate(self):
        print(
            f"Trying to access the fifth leg variable before its clear declaration..."
        )
        self.hasFifthLeg = True
        print(
            f"Now the {self.name} has five legs :/ and hasFifthLeg = {self.hasFifthLeg}"
        )

