import time
from turtle import Screen
from CarManager import CarManager
from Scoreboard import Scoreboard
from Player import Player

BORDERS = [280, -280]

screen = Screen()

def create_screen():
    """
    create the screen
    """
    screen.setup(600, 600) # set up the screen
    screen.bgcolor("white")
    screen.title("Turtle Crossing")
    screen.tracer(0) # turn off automatic animation
def game():
    """
    move the player to forward until the game ends
    """
    car = CarManager() # create cars in random location with random color
    player = Player() # create player
    scoreboard = Scoreboard() # create scoreboard

    screen.listen()
    screen.onkey(player.up, "Up") # when click on an Up key, player moves forward

    is_game_on = True
    while is_game_on:  # while the game happens
        screen.update()  # show the initial game
        time.sleep(0.1) # a brief pause to show the movement

        car.move_cars() # move cars

        if player.is_at_finish_line(): # detect if need increase level
            scoreboard.increase_level() # increase level
            car.increase_speed_cars() # increase speed of cars
            player.go_to_start() # move player to start

        for current_car in car.all_cars: # detect collision with player and car
            if current_car.distance(player) < 5: # if the current car is close to player
                is_game_on = False # stop the game
                scoreboard.game_over()

create_screen() # create the screen
game() # move the player to forward until the game ends
screen.exitonclick()