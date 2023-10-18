from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.score_right = 0
        self.score_left = 0
        self.color('white')
        self.penup()
        self.goto(0, 250)
        self.write(f"{self.score_left} :Score: {self.score_right}", align= "center", font=("Arial",30, "normal"))
        self.hideturtle()

    def count_right(self):
        self.score_right += 1
        self.clear()
        self.write(f"{self.score_left} :Score: {self.score_right}", align= "center", font=("Arial",30, "normal"))

    def count_left(self):
        self.score_left += 1
        self.clear()
        self.write(f"{self.score_left} :Score: {self.score_right}", align= "center", font=("Arial",30, "normal"))
    
    def end(self):
        self.color('red')
        self.goto(0, 0)
        self.write(f"You win, he lost", align= "center", font=("Arial",30, "normal"))

        