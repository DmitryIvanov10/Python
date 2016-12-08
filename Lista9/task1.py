# Lesson9, Task1

# import from modules
import matplotlib.pyplot as plt
import numpy as np

# create new class car 
class Car:
    """The class for the car"""

    def __init__(self, max_speed = 250, fuel_efficiency = 13.8):
        """Car attributes"""
        self.max_speed = max_speed # max speed in km/h
        self.fuel_efficiency = fuel_efficiency # fuel_efficiency in l per 100km
        self.speed = 0.0 # initial speed
        self.distance = 0.0 # initial distance
        self.time = 0.0 # initial time
        self.speed_data = [] # vector for saving speed data through the travel
        self.distance_data = [] # vector for saving distance data through the travel
        self.time_data = [] # # vector for saving time data through the travel
    
    def __str__(self): # prints info about class
        return "Car: max_speed = {}, fuel_efficiency = {}"\
                .format(self.max_speed, self.fuel_efficiency)
    
    def __repr__(self): # shows info about class
        return "Car({}, {})"\
                .format(self.max_speed, self.fuel_efficiency)

    def accelerate(self, value):
        """Accelerates the car by the value of the speed given"""
        if value >= 0:
            self.speed += value
            if self.speed > self.max_speed:
                self.speed = self.max_speed

    def deaccelerate(self, value):
        """Deaccelerates the car by the value of the speed given"""
        if value >= 0:
            self.speed -= value
            if self.speed < 0:
                self.speed = 0

    def stop(self):
        """Stops the car"""
        self.speed = 0

    def turbo(self):
        """Accelerates the car to the max_speed"""
        self.speed = self.max_speed

    def go(self, distance):
        """Changes distance value and updates time of the travel"""
        self.distance += distance
        self.time += distance/self.speed
        
        # save data about travel
        self.speed_data.append(self.speed)
        self.distance_data.append(self.distance)
        self.time_data.append(self.time)

    def travel(self):
        """Prints details of the travel"""
        # calculate time in hours and minutes
        time_hours = self.time // 1
        time_minutes = round(60 * (self.time % 1))

        # print details 
        print ()
        print ("The distance of the travel is {}km.".format(round(self.distance, 2)))
        print ("It took {}h {}m to travel that far with the average speed of {}km/h."\
            .format(time_hours, time_minutes, round(self.distance/self.time, 2)))
        print ("{} litres of fuel has been incinerated.".format( \
                round(self.distance/self.fuel_efficiency, 2)))

    def get_distance_data(self):
        """Returns distance data from the travel"""
        return self.distance_data
    
    def get_speed_data(self):
        """Returns speed data from the travel"""
        return self.speed_data
    
    def get_time_data(self):
        """Returns time data from the travel"""
        return self.time_data

# check results
# create an object - car with max_speed 200km/h and fuel_efficiency of 10 l per 100km
car = Car(200, 10)

# travel
car.accelerate(100)
car.go(100)
car.turbo()
car.go(100)

# print results
car.travel()

def plotWithMatplotlib(x, y, name):
    """Plot with MatPlotLib by x and y"""
    plt.plot(x, y)
    if name == 'S':
        plt.ylabel(name + ", km")
    else:
        plt.ylabel(name + ", km/h")
    plt.xlabel('t, h')
    plt.show()

# get data about changes in distance, speed and time
distance_data = car.get_distance_data()
speed_data = car.get_speed_data()
time_data = car.get_time_data()

# plot S(t)
plotWithMatplotlib(time_data, distance_data, "S")