class Car():
    def __init__(self,make, model, year):
        self.make = make
        self.model = model
        self.year = year


    def get_description(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name


new_car = Car('Audi', 'A6', 2018)
print(new_car.get_description())