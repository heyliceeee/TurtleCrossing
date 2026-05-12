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
MIN_X_SPACING = 80
"""
minimum distance between cars horizontal
"""
MIN_Y_SPACING = 30
"""
minimum distance between cars vertical
"""
LANES = list(range(-250, 260, 40))
"""
list of all lanes
"""


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = START_MOVE_DISTANCE
        self.create_cars()

    def create_cars(self):
        """
        create all cars
        """
        random.shuffle(LANES) # shuffle the lanes

        for i in range(100):
            new_car = Turtle("square") # create a new car
            new_car.color(random.choice(COLORS)) # set color
            new_car.penup() # no draw while move
            new_car.shapesize(stretch_wid=1, stretch_len=2) # set size

            lane = LANES[i % len(LANES)] # distribute cars in lanes
            new_car.goto(310, lane) # set position
            new_car.start_delay = random.randint(0, 200) # random delay before starting move

            self.all_cars.append(new_car) # add new_car to the list
    def move_cars(self):
        """
        move the car (right to left)
        """
        for car in self.all_cars:
            if car.start_delay > 0: # not yet start moving
                car.start_delay -= 1
                continue

            car.backward(self.car_speed) # start moving to the left

            if car.xcor() < -320: # when a car gets out the screen, show up in right side
                new_y = random.randint(-250, 250)

                while True: # make sure that no show up overlay to another car in the same lane
                    new_x = 300 # show up again always on the right side
                    if all(other_car is car or other_car.ycor() != new_y or abs(other_car.xcor() - new_x) > MIN_X_SPACING for other_car in self.all_cars): # check if there is a car too close in the same lane
                        break # valid position found
                car.goto(new_x, new_y)
                car.start_delay = random.randint(0, 200)
    def increase_speed_cars(self):
        """
        increase the speed of cars
        """
        self.car_speed += MOVE_INCREMENT