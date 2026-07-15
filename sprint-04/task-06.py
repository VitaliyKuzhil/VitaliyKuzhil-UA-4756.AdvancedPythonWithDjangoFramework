
class Car:
    def __init__(self, model, year, color, speed):
        self.model = model
        self.year = year
        self.color = color
        self.speed = speed


    def accelerate(self, speed_to_increase):
        old_speed = self.speed
        self.speed += speed_to_increase
        # print(f'The speed for "{self.model}" increased from {old_speed} to {self.speed} km/h.')


    def __lt__(self, other):
        return self.speed < other.speed


    def __str__(self):
        return f'{self.model} - Year: {self.year}, Color: {self.color}, Speed: {self.speed} km/h'


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.model}', {self.year}, '{self.color}', {self.speed})"




class ElectricCar(Car):
    def __init__(self, model, year, color, speed, battery_capacity):
        super().__init__(model, year, color, speed)
        self.battery_capacity = battery_capacity


    def accelerate(self, speed_to_increase):
        # old_speed = self.speed
        
        self.speed += speed_to_increase
        return f'Electric car accelerates by {speed_to_increase} km/h, current speed {self.speed}'
        
        # print(f'The speed for "{self.model}" increased from {old_speed} to {self.speed} km/h.')


    def __str__(self):
        return f'{self.model} - Year: {self.year}, Color: {self.color}, Speed: {self.speed} km/h, Battery Capacity: {self.battery_capacity} kWh'


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.model}', {self.year}, '{self.color}', {self.speed}, {self.battery_capacity})"




class HybridElectricCar(Car):
    def __init__(self, model, year, color, speed, fuel_consumption):
        super().__init__(model, year, color, speed)
        self.fuel_consumption = fuel_consumption


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.model}', {self.year}, '{self.color}', {self.speed}, {self.fuel_consumption})"




class CarFleet:

    def __init__(self):
        self.cars = list()


    def add_car(self, new_car):
        if isinstance(new_car, Car):
            self.cars.append(new_car)
            # print('New car added to the list of cars.')
        else:
            print('You should create car before adding it to the list.')


    def sort_cars_by_speed(self):
        self.cars.sort()
        # print('All the cars are sorted by field "speed".')
        return self.cars


    def __str__(self):
        return str(self.cars)



car1 = Car("Sedan", 2022, "Blue", 120)
electric_car1 = ElectricCar("Tesla", 2023, "Black", 150, 60)
hybrid_car1 = HybridElectricCar("Toyota", 2022, "Silver", 130, 0.05)
car_fleet = CarFleet()
car_fleet.add_car(car1)
car_fleet.add_car(electric_car1)
car_fleet.add_car(hybrid_car1)
car1.accelerate(10)
electric_car1.accelerate(20)
hybrid_car1.accelerate(15)

sorted_cars = car_fleet.sort_cars_by_speed()
for car in sorted_cars:
    print(car)