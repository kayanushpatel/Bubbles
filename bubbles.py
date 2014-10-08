""" Draws bubble figures in a random colored fashion
    using the turtle graphics module in python.

    File: bubbles.py
    Author: Kayanush Patel
    Created: 09/14/2014 (put on github 10/08/2014)

"""

import turtle
import random

""" Pre-condition: N/A

    Post-condition: Constant values are created as bounds
    on the range of a legal value. The purpose of these
    functions is so that we do not hardcode magic numbers
    in the code and we can call these functions when we need
    these constants.
"""

def MAX_BUBBLES():
    return 500

def MIN_BUBBLES():
    return 0

def BOUNDING_BOX():
    return 200

def MAX_DISTANCE():
    return 20

def MAX_RADIUS():
    return 20

def MAX_ANGLE():
    return 30


def draw_bounding_box():
    """Pre-condition: Empty turtle canvas is created.

    Post-condition: Draws a 2 dimensional boundry 400x400
    which the bubbles cannot pass.
    """
    
    turtle.up()
    turtle.goto(BOUNDING_BOX(), BOUNDING_BOX())
    turtle.down()
    turtle.goto(BOUNDING_BOX(), -BOUNDING_BOX())
    turtle.goto(-BOUNDING_BOX(), -BOUNDING_BOX())
    turtle.goto(-BOUNDING_BOX(), BOUNDING_BOX())
    turtle.goto(BOUNDING_BOX(), BOUNDING_BOX())
    turtle.up()
    turtle.goto(0,0)

def set_window():
    """Pre-condition: Prepares to draw bounding box function.

    Post-condition: Hides the turtle triangle so that it cannot
    be seen when drawing.
    - Calls draw_bounding_box() function.
    - Moves turtle to original position.
    - Puts turtle pen down and increases the speed of drawing.
    """
    
    turtle.hideturtle()
    draw_bounding_box()
    turtle.right(270)
    turtle.down()
    turtle.speed(0)

def color(radius):
    """Pre-condition: Function created for randomizing color
    of each circle.

    Post-condition: Creates random colors using (r, g, b) and
    random module. Also fills the circle with the color using
    the cirucles radius method.
    """
    
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor(r, g, b)
    turtle.begin_fill()
    turtle.fillcolor(r, g, b)
    turtle.circle(radius)
    turtle.end_fill()
    turtle.pencolor(1, 1, 1,)

def check_direction():
    """Pre-condition: Checks to see what direction the circle
    will be drawn in.

    Post-condition: Finds the position of turtle.
    - Sets conditions for certain cases and sets the heading of
    the turtle accordingly.
    """
    
    x, y = turtle.position()
    if x - 20 < -180:
        turtle.setheading(0)
    elif x + 20 > 180:
        turtle.setheading(180)
    elif y - 20 < -180:
        turtle.setheading(90)
    elif y + 20 > 180:
        turtle.setheading(270)

def draw_rec(bubbles, radius_total):
    """Pre-condition: Creates recursive version of the draw function.

    Post-condition: Creates a random radius for a circle.
    - Finds the entire area of the circle and then calls the color
    function to fill the circle with the color.
    - Lifts turtle up and finds a random angle to turn checks the
    direction and then creates next circle.
    """
    
    if(bubbles <= 0):
        pass
    else:
        radius = random.randint(1, MAX_RADIUS())
        radius_total += radius
        color(radius)
        turtle.up()
        angle = random.randint(-MAX_ANGLE(), MAX_ANGLE())
        turtle.left(angle)
        check_direction()
        turtle.forward(random.randint(1, MAX_DISTANCE()))
        turtle.down()
        return draw_rec(bubbles -1, radius_total)
    return radius_total

def draw_iter(bubbles):
    """Pre-condition: Creates interative version of the draw function.

    Post-condition: Creates a random radius for the circle
    - Colors the circle in just like recursive function.
    - Creates a random angle, checks the direction, and then moves a
    random distance.
    - Does that for each bubble called and subtracts by one until function
    hits zero.
    """
    radius_total = 0
    while(bubbles > 0):
        radius = random.randint(1, MAX_RADIUS())
        radius_total += radius
        color(radius)
        turtle.up()
        angle = random.randint(-MAX_ANGLE(), MAX_ANGLE())
        turtle.left(angle)
        check_direction()
        turtle.forward(random.randint(1, MAX_DISTANCE()))
        turtle.down()
        bubbles = bubbles - 1
    return radius_total

def main():
    """Pre-condition: Calls all important functions needed to
    create both recursive and iterative versions respectively.

    Post-condition: Calls the set_window() funtion and creates boundries.
    - Asks user to enter a number of bubbles to draw (has to be between
    0 and 500).
    - Checks to see if bubbles entered fits criteria and draws bubbles.
    - Prints out the bubbles' total radius for the user to see.
    - Once function is done running turtle resets itself and sets up for
    the iterative function.

    - For iterative: gets radius and draws bubbles.
    - Prompts the user to hit ENTER to end the program.
    - Turtle closes the program.
    - Else statement used: if user entered a number out of range of the
    legal values prompts the user again to enter number between 0 and 500.
    """
    
    bubbles = int(input("Enter the number of bubbles (0-500): "))
    set_window()
    if(bubbles <= MAX_BUBBLES()) and (bubbles >= MIN_BUBBLES()):
        radius = draw_rec(bubbles, 0)
        print("The bubbles' total radius is " + str(radius) + " units.")
        input("Press ENTER to continue.")
        turtle.reset()
        
        set_window()
        radius = draw_iter(bubbles)
        print("The bubbles' total radius is " + str(radius) + " units.")
        input("Press ENTER to end program.")
        turtle.bye()

    else:
        input("Bubbles must be between 0 and 500 inclusive.")
        turtle.bye()

main()
