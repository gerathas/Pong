# -*- coding: utf-8 -*-
#This is a simple version of Pong created with Turtle on Python

import turtle

#Initializes the main screen size
wn=turtle.Screen()
wn.title("Pong by Gautham")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#Paddle 1
paddle_1=turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.shapesize(stretch_wid=5,stretch_len=1)
paddle_1.color("white")
paddle_1.penup()
paddle_1.goto(-350,0)

#Paddle 2
paddle_2=turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.shapesize(stretch_wid=5,stretch_len=1)
paddle_2.color("white")
paddle_2.penup()
paddle_2.goto(350,0)

#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white") 
ball.penup()
ball.goto(0,0)
#Ball speed
ball.dx=0.4
ball.dy=0.4

#Center
center_line=turtle.Turtle()
center_line.speed(0)
center_line.shape("square")
center_line.shapesize(stretch_wid=600,stretch_len=0.5)
center_line.color("red")
center_line.goto(0,0)

#Score
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
score_1=0
score_2=0
pen.write("Player 1: {}  Player 2: {}".format(score_1,score_2),align="center",font=("courier",24,"normal"))

#Functions to control the movement of the paddles
def paddle_1_up():
    y=paddle_1.ycor()
    if y>240:
        y+=0
    else:
        y+=20
    paddle_1.sety(y)

def paddle_1_down():
    y=paddle_1.ycor()
    if y<-220:
        y-=0
    else:
        y-=20
    paddle_1.sety(y)

def paddle_2_up():
    y=paddle_2.ycor()
    if y>240:
        y+=0
    else:
        y+=20
    paddle_2.sety(y)

def paddle_2_down():
    y=paddle_2.ycor()
    if y<-220:
        y-=0
    else:
        y-=20
    paddle_2.sety(y)
    
#Keyboard binding
#Player 1 will use W and S keys to move their paddle up and down
#Player 2 will use up and down arrow keys to move the paddle
wn.listen()
wn.onkeypress(paddle_1_up,"w")
wn.onkeypress(paddle_1_down,"s")
wn.onkeypress(paddle_2_up,"Up")
wn.onkeypress(paddle_2_down,"Down")

#Main loop
#Ball starts to move in initialized speed when game starts
while True:
    wn.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    
    #Boundaries
    #If the ball hits the upper or lower parts of the screen, it will deflect
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1

    #Returns to center after a goal
    #Score increases by 1 when a player scores
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score_1+=1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1,score_2),align="center",font=("courier",24,"normal"))
    
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score_2+=1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1,score_2),align="center",font=("courier",24,"normal"))
    
    #Paddle bounce
    #This is what makes the ball to bounce of the paddles
    if (ball.xcor()<paddle_1.xcor()+10 and ball.ycor()<paddle_1.ycor()+40 and ball.ycor()>paddle_1.ycor()-40):
        ball.setx(paddle_1.xcor()+10)
        ball.dx*=-1

    if (ball.xcor()>paddle_2.xcor()-10 and ball.ycor()<paddle_2.ycor()+40 and ball.ycor()>paddle_2.ycor()-40):
        ball.setx(paddle_2.xcor()-10)
        ball.dx*=-1
