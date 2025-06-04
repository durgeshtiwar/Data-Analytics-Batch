# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.

# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def fullName(self):
#     return f"{self.brand} {self.model}"

# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model) 
# print(my_car.fullName())

# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.
# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#   def fullName(self):
#     return f"{self.brand} {self.model}"
# class ElectricCar(Car):
#   def __init__(self, brand, model, battery_size):
#     super().__init__(brand, model)
#     self.battery_size = battery_size

# my_tesla = ElectricCar("Tesla", "Model S", "85KWH")
# print(my_tesla.brand)
# print(my_tesla.model)
# print(my_tesla.battery_size)
# print(my_tesla.fullName())

# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.fullName())

# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it
# class Car:
#   def __init__(self, brand, model):
#     self.__brand = brand
#     self.model = model
#   def fullName(self):
#     return f"{self.__brand} {self.model}"
#   def get_brand(self):
#     return self. __brand
# class ElectricCar(Car):
#   def __init__(self, brand, model, battery_size):
#     super().__init__(brand, model)
#     self.battery_size = battery_size

# my_tesla = ElectricCar("Tesla", "Model S", "85KWH")
# print(my_tesla.get_brand())
# print(my_tesla.model)
# print(my_tesla.battery_size)
# print(my_tesla.fullName())

# my_car = Car("Toyota", "Corolla")
# print(my_car.get_brand())
# print(my_car.model)
# print(my_car.fullName())

# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

# class Car:
#   def __init__(self, brand, model):
#     self.__brand = brand
#     self.model = model
#   def fullName(self):
#     return f"{self.__brand} {self.model}"
#   def get_brand(self):
#     return self. __brand
#   def fuel_type(self):
#     print("This is oil car")
# class ElectricCar(Car):
#   def __init__(self, brand, model, battery_size):
#     super().__init__(brand, model)
#     self.battery_size = battery_size

#   def fuel_type(self):
#     print("This is charging type")

# my_tesla = ElectricCar("Tesla", "Model S", "85KWH")
# print(my_tesla.get_brand())
# print(my_tesla.model)
# print(my_tesla.battery_size)
# print(my_tesla.fullName())
# my_tesla.fuel_type()

# my_car = Car("Toyota", "Corolla")
# print(my_car.get_brand())
# print(my_car.model)
# print(my_car.fullName())
# my_car.fuel_type()

# Problem: Add a class variable to Car that keeps track of the number of cars created.
# class Car:
#   total_car = 0
#   def __init__(self, brand, model):
#     self.__brand = brand
#     self.model = model
#     Car.total_car = Car.total_car + 1

#   def fullName(self):
#     return f"{self.__brand} {self.model}"
  
#   def get_brand(self):
#     return self. __brand
  
#   def fuel_type(self):
#     print("This is oil car")

# my_car = Car("Toyota", "Corolla")
# my_car = Car("Toyota1", "Corolla1")
# print(my_car.get_brand())
# print(my_car.model)
# print(my_car.fullName())
# my_car.fuel_type()
# print(Car.total_car)

# Problem: Add a static method to the Car class that returns a general description of a car.
# class Car:
#   total_car = 0
#   def __init__(self, brand, model):
#     self.__brand = brand
#     self.model = model
#     Car.total_car = Car.total_car + 1

#   def fullName(self):
#     return f"{self.__brand} {self.model}"
  
#   def get_brand(self):
#     return self. __brand
  
#   def fuel_type(self):
#     print("This is oil car")

#   @staticmethod 
#   def genral_description():
#     return"Car is means of transport"

# my_car = Car("Toyota", "Corolla")
# my_car = Car("Toyota1", "Corolla1")
# print(my_car.get_brand())
# print(my_car.model)
# print(my_car.fullName())
# my_car.fuel_type()
# print(Car.total_car)
# print(Car.genral_description())

# Problem: Use a property decorator in the Car class to make the model attribute read-only.
# class Car:
#   total_car = 0
#   def __init__(self, brand, model):
#     self.__brand = brand
#     self.__model = model
#     Car.total_car = Car.total_car + 1

#   def fullName(self):
#     return f"{self.__brand} {self.__model}"
  
#   def get_brand(self):
#     return self. __brand
  
#   def fuel_type(self):
#     print("This is oil car")

#   @staticmethod 
#   def genral_description():
#     return"Car is means of transport"
#   @property
#   def get_model(self):
#     return self.__model

# my_car = Car("Toyota", "Corolla")
# my_car1 = Car("Toyota1", "Corolla1")
# print(my_car.get_brand())
# # print(my_car.model)
# print(my_car.fullName())
# my_car.fuel_type()
# print(Car.total_car)
# print(Car.genral_description())
# print(my_car.get_model)

# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.

class Car:
  total_car = 0
  def __init__(self, brand, model):
    self.__brand = brand
    self.__model = model
    Car.total_car = Car.total_car + 1

  def fullName(self):
    return f"{self.__brand} {self.__model}"
  
  def get_brand(self):
    return self. __brand
  
  def fuel_type(self):
    print("This is oil car")

  @staticmethod 
  def genral_description():
    return"Car is means of transport"
  @property
  def get_model(self):
    return self.__model

my_car = Car("Toyota", "Corolla")
my_car1 = Car("Toyota1", "Corolla1")
print(my_car.get_brand())
# print(my_car.model)
print(my_car.fullName())
my_car.fuel_type()
print(Car.total_car)
print(Car.genral_description())
print(my_car.get_model)
print(isinstance(my_car, Car))