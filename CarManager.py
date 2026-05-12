import random
from turtle import Turtle
"""
list of all cars
"""
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
"""
color of the car
"""
START_MOVE_DISTANCE = 5
"""
number of the starting steps that car move 
"""
MOVE_INCREMENT = 10
"""
number of increment steps that car move
"""


class CarManager:
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = START_MOVE_DISTANCE

    def create(self):
        """
        create a car
        """
        random_chance = random.randint(1, 6) # random chance to create a car

        if random_chance == 1:
            new_car = Turtle("square") # create a new car
            new_car.color(random.choice(COLORS)) # set color
            new_car.penup() # no draw while move
            new_car.shapesize(stretch_wid=1, stretch_len=2) # set size
            random_y = random.randint(-250, 250) # get random y
            new_car.goto(300, random_y) # set position

            self.all_cars.append(new_car) # add new_car to the list
    def move_cars(self):
        """
        move the car (right to left)
        """
        for car in self.all_cars:
            car.backward(self.car_speed) # start moving to the left
    def increase_speed_cars(self):
        """
        increase the speed of cars
        """
        self.car_speed += MOVE_INCREMENT