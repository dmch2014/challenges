# Extra Challenge: Class of Cars
#
# b. Create three classes of three car brands – Ford, BMW, and
# Tesla. The attributes of the car's objects will be, model,
# color, year, transmission, and whether the car is
# electric or not (Boolean value.) Consider using inheritance
# in your answer.
# You will create one object for each car brand:
#     bmw1 : model: x6, Color: silver, Year: 2018, Transmission: Auto, Electric: False
# tesla1: model: S, Color: beige, Year: 2017, Transmission: Auto, Electric: True
# ford1 : model: focus, Color: white, Year: 2020, Transmission: Auto, Electric: False
# You will create a class method, called print_cars that will be
# able to print out objects of the class. For example, if you call the
# method on the ford1 object of the Ford class, your function
# should be able to print out car info in this exact format:
# car_model = focus
# Color = White
# Year = 2020
# Transmission = Auto
# Electric = False

class Car():
    def __init__(self, model, year, color, transmission, electric=False):
        self.model = model
        self.year = year
        self.color = color
        self.transmission = transmission
        self.electric = electric

    def print_car(self):
        print("Car_model = ", self.model)
        print("Color = ", self.color)
        print("Year = ", self.year)
        print("Transmission = ", self.transmission)
        print("Electric = ", self.electric)


class Ford(Car):
    def __init__(self, model, year, color, transmission, electric=False):
        Car.__init__(self, model, year, color, transmission, electric=False)

class BMW(Car):
    def __init__(self, model, year, color, transmission, electric=False):
        Car.__init__(self, model, year, color, transmission, electric=False)

class Tesla(Car):
    def __init__(self, model, year, color, transmission, electric=False):
        Car.__init__(self, model, year, color, transmission, electric=False)




bmw = BMW('x6', 2018, 'silver', 'Auto',  False)
bmw.print_car()
print("--------------------------------")
# tesla1: model: S, Color: beige, Year: 2017, Transmission: Auto, Electric: True
# ford1 : model: focus, Color: white, Year: 2020, Transmission: Auto, Electric: False

ford= Ford("Focus", 2020, 'white', 'Auto', False)
ford.print_car()
print("--------------------------------")


tesla = Tesla('S', 2017, 'beige', 'Auto',  True)
tesla.print_car()