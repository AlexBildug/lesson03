from les09sol01 import Car


def main():
    car = Car("Mercedes", "E500", 2000)
    while car.speed < 100:
        car.increase_speed()
    car.print_speed()


if __name__ == "__main__":
    main()