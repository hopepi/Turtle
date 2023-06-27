import turtle
import random
from turtle import Turtle

screen= turtle.Screen()
screen.bgcolor("green")
screen.title("TURTLE")
score=0
x_list =[-200,-100,0,100,200]
y_list =[200,100,0,-100]
turtle_list=[]
score_turtle: Turtle = turtle.Turtle()
countdown_turtle =turtle.Turtle()
game_over=False
def scoreTurtle():

    score_turtle.color("dark blue")
    top_height = screen.window_height() / 2
    score_turtle.penup()
    score_turtle.hideturtle()
    y = top_height * 0.9
    score_turtle.setpos(0, y)
    score_turtle.write(arg="Score: 0", move=False, align="center", font=('Arial', 30, 'bold'))

def make_turtle(x,y):
    turtleee=turtle.Turtle()

    def handle_click(x,y):
        global score
        score+=1
        score_turtle.clear()
        score_turtle.write(arg=f"Score: {score}", move=False, align="center", font=('Arial', 30, 'bold'))
        #print(x,y)
    turtleee.onclick(handle_click)
    turtleee.penup()
    turtleee.shape("turtle")
    turtleee.shapesize(2,2)
    turtleee.color("yellow")
    turtleee.goto(x,y)
    turtle_list.append(turtleee)

def speed_turtle():
    for x in x_list:
        for y in y_list:
            make_turtle(x, y)

def hide_turtles():
    for j in turtle_list:
        j.hideturtle()

def random_list():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(random_list, 750)

def count_time(time):
    global game_over
    countdown_turtle.color("dark blue")
    top_height = screen.window_height() / 2
    countdown_turtle.penup()
    countdown_turtle.hideturtle()
    y = top_height * 0.9
    countdown_turtle.setpos(0, y-50)
    countdown_turtle.clear()
    if time >0:
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Time: {time}", move=False, align="center", font=('Arial', 30, 'bold'))
        screen.ontimer(lambda :count_time(time-1),1000)
    else:
        game_over=True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game over", move=False, align="center", font=('Arial', 30, 'bold'))

count_time(10)
turtle.tracer(0)
speed_turtle()
hide_turtles()
random_list()
scoreTurtle()
turtle.tracer(1)


turtle.mainloop()