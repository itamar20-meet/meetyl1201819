import turtle
import time 
import math
import random 
from ball import Ball
from time import sleep
turtle.tracer(0,0)
turtle.hideturtle()
global RUNNING
global SLEEP
RUNNING = True
SLEEP = 0.0077
global SCREEN_HEIGHT
global SCREEN_WIDTH
screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2

global counter 
counter = 0
BALLS = []
Screen=turtle.Screen()
Screen.register_shape("park.gif")
Screen.bgpic("park.gif")
my_ball = Ball(0,0,2,2,60,"red")
scoreTurtle = turtle.clone()


NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 70
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

for i in range(NUMBER_OF_BALLS):
	x = random.randint(-screen_width + MAXIMUM_BALL_RADIUS, screen_width - MAXIMUM_BALL_RADIUS)
	y = random.randint(-screen_height + MAXIMUM_BALL_RADIUS, screen_height - MAXIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	color =(random.random(), random.random(), random.random())
	ball = Ball(x,y,dx,dy,radius,color)
	BALLS.append(ball)


def change_ball(ball_b):
	x = random.randint(-screen_width + MAXIMUM_BALL_RADIUS, screen_width - MAXIMUM_BALL_RADIUS)
	y = random.randint(-screen_height + MAXIMUM_BALL_RADIUS, screen_height - MAXIMUM_BALL_RADIUS)
	dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	color =(random.random(), random.random(), random.random())	
	ball_b.x = x
	ball_b.y = y
	ball_b.r = radius
	ball_b.penup()
	ball_b.goto(x,y)
	ball_b.color(color)
	ball_b.shape("circle")
	ball_b.shapesize(radius/10)
	ball_b.dx = dx
	ball_b.dy =dy
					
turtle.update()
def move_all_balls():

	for i in BALLS:
		i.move(screen_width,screen_height)

def collide(ball1 ,ball2):

	x1 = ball1.xcor() 
	y1 = ball1.ycor()
	x2 = ball2.xcor()
	y2 = ball2.ycor()
	

	d_between = math.sqrt(math.pow((x1 - x2),2) + math.pow((y1 - y2),2))
	sum_radius = ball1.r + ball2.r
	if ball1 == ball2:
		return False
	elif sum_radius >= d_between:
		return True
	else :
		return False
def check_all_ball_collsion():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a,ball_b):
				radius1 = ball_a.r
				radius2 = ball_b.r
				x = random.randint(-screen_width + MAXIMUM_BALL_RADIUS, screen_width - MAXIMUM_BALL_RADIUS)
				y = random.randint(-screen_height + MAXIMUM_BALL_RADIUS, screen_height - MAXIMUM_BALL_RADIUS)
				dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
				dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)
				radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
				color =(random.random(), random.random(), random.random())
				if radius1 >= radius2 :
					ball_a.r+= 1
					ball_a.shapesize(ball_a.r/10)
					change_ball(ball_b)
				elif radius1< radius2 :
					ball_b.r+= 1
					ball_b.shapesize(ball_b.r/10)
					change_ball(ball_a)

def check_my_ball_collsion():
	for ball_c in BALLS :
		if collide(my_ball,ball_c):
				radius3 = my_ball.r
				radius4 = ball_c.r
				if radius3 <=radius4 :
					 return False
				else :
					my_ball.r+= 1
					my_ball.shapesize(radius3/10)
					change_ball(ball_c)
				
	return True
score = 0

#scoreTurtle.write(int(score),align="center",font=("ariel", 20, "bold"))


	
	
def movearound(event):
	x = event.x - screen_width
	y = screen_height - event.y
	my_ball.goto(x,y)

turtle.getcanvas().bind("<Motion>", movearound)

turtle.listen()


while RUNNING :
	win = False	
	screen_width = turtle.getcanvas().winfo_width()/2
	screen_height = turtle.getcanvas().winfo_height()/2
	move_all_balls()
	check_all_ball_collsion()
	RUNNING = check_my_ball_collsion()
	if my_ball.r >= 275 :
		win = True
	turtle.update()
	time.sleep(SLEEP)
	if win  == True :
		break


