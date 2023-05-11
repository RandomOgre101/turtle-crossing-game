from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard:
    def __init__(self):
        self.score = 0
        self.pen = Turtle()
        self.pen.hideturtle()
        self.pen.color("black")
        self.pen.penup()
        self.pen.goto(-260,260)
        self.pen.write(f"Level: {self.score}", align="left", font=FONT)

    def game_over(self):
        self.pen = Turtle()
        self.pen.hideturtle()
        self.pen.write("GAME OVER", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.pen.clear()
        self.pen.write(f"Level: {self.score}", align="left", font=FONT)
