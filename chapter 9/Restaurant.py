class Restaurant:
    "A simple attemp to model a restaurant"

    def __init__(self, title, isOpen):
        "A class constructor initializing title & isOpen properties."
        self.title = title
        self.isOpen = isOpen

    def get_opening_status(self):
        return "open" if self.isOpen else "closed"

    def toggle_restaurant_oneping_status(self):
        self.isOpen = not self.isOpen
        print(f'The restaurant "{self.title}" is {self.get_opening_status()} now.')
