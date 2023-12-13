from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 30, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("red")
        self.penup()

        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-60, 240)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(60, 240)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score +=1
        self.update_scoreboard()

    def r_point(self):
        self.r_score +=1
        self.update_scoreboard()




    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game over!", align=ALIGNMENT, font=FONT)

    # def increase_score(self):
    #     self.score += 1
    #     self.clear()
    #     self.update_scoreboard()
