class Vehicle:
    def __init__(self, wheel_size, wheel_number, year):
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number
        self.year = year

    def go(self):
        return "vrrrrrrrooom!"

    def fill_up_tank(self):
        return "filling up!"