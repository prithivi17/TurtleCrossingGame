from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1

    def p_level(self):
        self.goto(-220, 260)
        self.write(f"Level: {self.level}", align="center", font=("Courier", 20, "normal"))

    def increase_level(self):
        self.clear()
        self.level += 1
        self.p_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 20, "normal"))