from turtle import Turtle, Screen

my_turtle = Turtle()
screen = Screen()

def move_forward():
    my_turtle.forward(10)

def move_backward():
    my_turtle.backward(10)

def move_clock():
    my_turtle.right(30)
def counter_clock():
    my_turtle.left(30)

def clear_screen():
    my_turtle.reset()
    
    



screen.listen()
screen.onkey(key="W", fun=move_forward)
screen.onkey(key="S", fun=move_backward)
screen.onkey(key="A", fun=move_clock)
screen.onkey(key="D", fun=counter_clock)
screen.onkey(key="C", fun=clear_screen)

screen.exitonclick()