class Car:
    def __init__(self, make, model, year, odometer_reading = 0):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = odometer_reading
    
    def get_descriptive_name(self):
        print(f"{self.year}  {self.make} {self.model}")
        
    def read_odometer(self):
        print(f"Your current odometer reading is: {self.odometer_reading}")
        
    def drive(self, miles):
        if miles < 0:
            print("Cant run the car for a negative amount of miles...\nPlease enter a valid amount")
            return
        self.odometer_reading += miles
    
    def __str__(self):
        return(f"{self.year} {self.make} {self.model},  ran {self.odometer_reading} miles")
    
class ElectricCar(Car):
    def __init__(self, make, model, year, odometer_reading=0, battery_size = 75):
        super().__init__(make, model, year, odometer_reading)
        self.battery_size = battery_size
        
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
        
    def read_odometer(self):
        print(f"Your current odometer reading is: {self.odometer_reading}")
        print("Your car is being run by electricity")
        
my_car1 = Car(make="Tesla", model="Model 3", year=2024 ,odometer_reading=48.5)
my_car2 = ElectricCar(make="Tesla", model="Model 4", year=2026 ,odometer_reading=99.9, battery_size= 100)

def service_check(vehicle):
    print(vehicle.odometer_reading)

print(my_car1)
print(my_car2)

service_check(my_car1)
service_check(my_car2)