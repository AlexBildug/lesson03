class Car:

    def __init__(self, make: str, model: str, year: int, speed: int = 0):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def increase_speed(self):
        self.speed += 5

    def decrease_speed(self):
        self.speed -= 5

    def stop(self):
        self.speed = 0

    def reverse(self):
        self.speed *= -1

    def print_speed(self):
        print(self.speed)