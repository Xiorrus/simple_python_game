import turtle
import random

# Create a screen
window = turtle.Screen()
window.title('Moving Block')
window.bgcolor('black')
# Set up the screen's attributes, including the border
window.setup(width=600, height=400) # Set the window size
window.tracer(0) # Turn off automatic screen updates

# Create a turtle shape
shape = turtle.Turtle()
shape.shape('square')
shape.color('white')
shape.penup()

# print(shape.xcor(), shape.ycor())

# List to store obstacle
obstacles = []

# List of obstacles already passed
passed_obstacle = []

# Set the boundaries
border_left = -290
border_right = 290
border_top = 190
border_bottom = -190

# Set the speed
speed = 20

# Set the score
score = 0

# speed increase based on score
if score/10 > speed:
	speed+=20

# Function that outputs when you run the game
def main_menu():
	# Write on screen new game
	turtle.penup()
	turtle.goto(-280, 0)
	turtle.color('white')
	turtle.write('New Game? (press enter to start)', align='left', font=('comicsans', 20, 'bold'))

    # Hide the turtle
	turtle.hideturtle
	
    # Bind key Enter to main
	window.onkeypress(main, key='Return')
	
    # Listen for key event
	window.listen()
	
    # Keep the window open
	turtle.done()
	
# Function to move the shape forward
def move_forward():
	new_x = shape.xcor() + speed
	if border_left < new_x < border_right:
		shape.setx(new_x)

# Function to move the shape backward
def move_backward():
	new_x = shape.xcor() - speed
	if border_left < new_x < border_right:
		shape.setx(new_x)

# Function to move shape up
def move_up():
	new_y = shape.ycor() + speed
	if border_bottom < new_y < border_top:
		shape.sety(new_y)

# Function to move shape down
def move_down():
	new_y = shape.ycor() - speed
	if border_bottom < new_y < border_top:
		shape.sety(new_y)

# Function to create a random obstacle
def createObstacle():
	obstacle = turtle.Turtle()

	obstacle.shape('circle')  # You can change the shape as desired
	obstacle.color('red')
	obstacle.penup()
	# obstacle.goto(border_right, random.randint(border_bottom, border_top))
	obstacle.goto(border_right + random.randint(0, 100), random.randint(border_bottom, border_top))
	obstacles.append(obstacle)

def display_score():
	turtle.penup()
	turtle.goto(-60, 180)
	turtle.color('white')
	turtle.clear()  # Clear the previous score display
	turtle.write(f'Score: {score}', align='left', font=('comicsans', 14, 'bold'))

	turtle.hideturtle()

# Function to move obstacles to the left
def move_obstacles():
	for obstacle in obstacles:
		if score > 0:
			obstacle.setx(obstacle.xcor() - (score/100))# speed increase based on score
		else:
			obstacle.setx(obstacle.xcor() - .1)# You can adjust the speed as needed by changing the value of .1

		if obstacle.xcor() < border_left:
			obstacles.remove(obstacle)
			obstacle.hideturtle()

# Function to check for collisions
def check_collisions():
	for obstacle in obstacles:
		if shape.distance(obstacle) < 20:  # You can adjust the collision threshold as needed
			shape.goto(0, 0)  # Reset the shape's position
			died()
			return True
	return False

def check_obstacles():
	# return True if all obstacles have been passed behind the shape
	for obstacle in obstacles:
		if obstacle.xcor() > border_left and obstacle.xcor() < border_right and obstacle.xcor() > shape.xcor():
			return False
	return True

def clearObstacles():
	for obstacle in obstacles:
		obstacle.hideturtle()
	obstacles.clear()

# Function that outputs when you lose
def died():
	clearObstacles()
	# Write on the screen
	turtle.penup()
	turtle.goto(-280, 100) # Set the position where the text will be written
	turtle.color('white')
	turtle.write('You Died', align='left', font=('comicsans', 20, 'bold'))

	# Write on the screen Play Again
	turtle.penup()
	turtle.goto(-280, 50) # Set the position where the text will be written
	turtle.color('white')
	turtle.write('Play Again ? ( press space to start again )', align='left', font=('comicsans', 20, 'bold'))

	# Write on the screen Quit
	turtle.penup()
	turtle.goto(-280, 0) # Set the position where the text will be written
	turtle.color('white')
	turtle.write('Quit ?  ( press Esc to Quit )', align='left', font=('comicsans', 20, 'bold'))

	# hide the turtle
	turtle.hideturtle()


def quitGame():
	window.bye()


def main():
	global score
	score = 0

	# Clear the obstacles
	clearObstacles()

	# Reset the shape's position
	shape.goto(0, 0)

	# clear the screen
	turtle.clear()

	# Bind the key right arrow to forward
	window.onkeypress(move_forward,key='Right')

	# Bind key left arrow to backward
	window.onkeypress(move_backward, key='Left')

	# Bind key UP arrow to up
	window.onkeypress(move_up, key='Up')

	# Bind key down arrow to down
	window.onkeypress(move_down, key='Down')

	# Bind key space to restart
	window.onkeypress(main, key='space')

	# Bind key Esc to quit
	window.onkeypress(quitGame, key='Escape')

	# Listen for key events
	window.listen()

	# Continuous movement loop
	while True:

		move_obstacles()
		display_score()
		if check_collisions():
			break
		window.update() # Update the screen

		# Randomly create obstacles
		# check if all obstacles have been passed behind the shape
		if len(obstacles)<15 or check_obstacles(): # create an obstacle if there are no obstacles
			if random.randint(1, 50) == 1:  # controls the frequency of obstacle creation by changing the value of 50
				createObstacle()

		for obstacle in obstacles:
			if obstacle.xcor() < shape.xcor() and obstacle not in passed_obstacle:
				score += 1
				display_score()
				passed_obstacle.append(obstacle)

	# Keep the window open
	turtle.done()
	print('Game Over')


if __name__ == '__main__':
	main_menu()