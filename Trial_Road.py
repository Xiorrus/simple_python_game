import turtle
import random

# Create a screen
window = turtle.Screen()
window.title('Moving Block')
window.bgcolor('black')

# Set up the screen's attributes, including the border
window.setup(width=600, height=400)  # Set the window size
window.tracer(0)  # Turn off automatic screen updates

# Create a turtle shape
shape = turtle.Turtle()
shape.shape('square')
shape.color('white')
shape.penup()

# List to store obstacle
obstacles = []

# Set the boundaries
border_left = -290
border_right = 290
border_top = 190
border_bottom = -190

# Function to move the shape foward
def move_forward():
    new_x = shape.xcor() + 10
    if border_left < new_x < border_right:
        shape.setx(new_x)

# Function to move the shape backward
def move_backward():
    new_x = shape.xcor() - 10
    if border_left < new_x < border_right:
        shape.setx(new_x)

# Function to move shape up
def move_up():
    new_y = shape.ycor() + 10
    if border_bottom < new_y < border_top:
        shape.sety(new_y)

# Function to move shape down
def move_down():
    new_y = shape.ycor() - 10
    if border_bottom < new_y < border_top:
        shape.sety(new_y)

# Function to create a random obstacle
def create_obstacle():
    obstacle = turtle.Turtle()
    obstacle.shape('circle')  # You can change the shape as desired
    obstacle.color('red')
    obstacle.penup()
    obstacle.goto(border_right, random.randint(border_bottom, border_top))
    obstacles.append(obstacle)

# Function to move obstacles to the left
def move_obstacles():
    for obstacle in obstacles:
        obstacle.setx(obstacle.xcor() - 1)
        if obstacle.xcor() < border_left:
            obstacles.remove(obstacle)
            obstacle.hideturtle()

# Function to check for collisions
def check_collisions():
    for obstacle in obstacles:
        if shape.distance(obstacle) < 20:  # You can adjust the collision threshold as needed
            shape.goto(0, 0)  # Reset the shape's position
            died()

# Bind the key d to foward
window.onkeypress(move_forward, 'd')

# Bind key a to backward
window.onkeypress(move_backward, 'a')

# Bind key w to up
window.onkeypress(move_up, 'w')

# Bind key s to down
window.onkeypress(move_down, 's')

# Listen for key events
window.listen()

# Function that outputs when you lose
def died():
    # Write on the screen
    turtle.penup()
    turtle.goto(-50, 100)  # Set the position where the text will be written
    turtle.color('white')
    turtle.write('You Died', align='left', font=('comicsans', 20, 'bold'))

# Continuous movement loop
while True:
    move_obstacles()
    check_collisions()
    window.update()  # Update the screen

    # Randomly create obstacles
    if random.randint(1, 100) == 1:
        create_obstacle()

# Keep the window open
turtle.done()
