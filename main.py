import time
from turtle import Screen
from player import Player
from car import Cars
from scoreboard import Score


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)


player = Player()
car_manager = Cars()
score = Score()


screen.listen()
screen.onkeypress(player.move, "w")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_car()
    score.p_level()



    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_on = False
            score.game_over()


    # detect finishing line
    if player.ycor() > 290:
        player.reset_game()
        car_manager.level_up()
        score.increase_level()





screen.exitonclick()