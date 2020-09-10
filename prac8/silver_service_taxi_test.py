
from prac8.silver_sevice_taxi import SilverServiceTaxi


def main():

    taxi = SilverServiceTaxi("Limo", 100, 2)
    taxi.drive(20)
    print(taxi)

    taxi.add_fuel(8)
    print(taxi.get_fare())

main()