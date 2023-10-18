from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.position = (0, 0)
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(self.position)
        self.x_move = 10
        self.y_move = 10


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def faster(self):
        self.y_move *= 1.1
        self.x_move *= 1.1
    

    def bounce(self):
        self.y_move *= -1


    def paddle_bounce(self):
        self.x_move *= -1


    def reset_position(self):
        self.goto(0, 0)
        self.y_move = 10
        self.x_move = 10
        self.paddle_bounce()


        
        
        


        