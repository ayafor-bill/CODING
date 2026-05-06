class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def describe_car(self):
        """Describe the car"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Read the car's odometer"""
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        """Set the odometer to a given value
            Rejects if the new mileage attempts to roll back the odometer
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back the odometer!")
        
    def increment_odometer(self, miles):
        """Increment the odometer by a given value"""
        self.odometer_reading += miles
        
new_car = Car('audi', 'outback', 2020)
print(new_car.describe_car())
new_car.read_odometer()

## Updating the odometer reading
new_car.odometer_reading = 23
new_car.read_odometer()

## Updating the odometer using a method
new_car.update_odometer(45)
new_car.read_odometer()

## Incrementing the odometer
old_car = Car('subaru', 'forester', 2015)
print(old_car.describe_car())
old_car.read_odometer()

old_car.update_odometer(100)
old_car.read_odometer()