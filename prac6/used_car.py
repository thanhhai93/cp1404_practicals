
from prac6.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car, fuel = {self.fuel}, odometer = {self.odometer}".format(self=my_car))

    limo = Car(100)
    limo.add_fuel(20)
    print("Limo's fuel = ",limo.fuel)
    limo.drive(115)
    print("limo's odometer reading: ", limo.odometer)



main()
