# Class
class Car:
    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    @classmethod
    def set_wheels(cls, amount):
        cls.wheels = amount

    def drive(self):
        print(f"Driving the {self.make} {self.model} with {self.wheels} wheels.")

    @staticmethod
    def car_description(color):
        print(f"A {color}car is a vehicle that drives on wheels.")


# # Subclasses
# class ElectricCar(Car):
#   def __init__(self, make, model, range_km):
#     super().__init__(make, model)
#     self.range_km = range_km

#   def charge(self):
#     print(f"Charging the {self.make} {self.model}")


# class GasolineCar(Car):
#     def __init__(self, make, model, fuel_capacity):
#       super().__init__(make, model)
#       self.fuel_capacity = fuel_capacity

#     def refuel(self):
#         print(f"Refueling the {self.make} {self.model}")

my_car = Car("Mustang", "Shelby")
your_car = Car("Toyota", "Rav4")

print(my_car.wheels)

Car.set_wheels(3)

print(your_car.wheels)
