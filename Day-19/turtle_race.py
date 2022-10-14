from turtle import Turtle, Screen, color
import random
screen = Screen()

race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_position = -100
turtle_list = []

for i in range(len(colors)):
    my_turtle = Turtle(shape="turtle")
    my_turtle.color(colors[i])
    my_turtle.penup()
    my_turtle.goto(x=-230,y=y_position)
    y_position += 30
    turtle_list.append(my_turtle)

if user_bet:
    race_on = True
    
while race_on:
    for turtles in turtle_list:
        if turtles.xcor() > 230:
            race_on = False
            winner = turtles.pencolor()
            if winner == user_bet:
                print(f"You've won!. The {winner} turtle is the winner")
            print(f"You've lost!. The {winner} turtle is the winner")
        
        rand_dist = random.randint(0, 10)
        turtles.forward(rand_dist)
        
        

screen.exitonclick()