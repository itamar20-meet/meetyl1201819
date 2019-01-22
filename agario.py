import turtle
import time 
import math
import random 
from ball import Ball
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

BALLS = []

my_ball = Ball(0,0,2,2,50,"red")


NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 60
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
				elif radius1< radius2 :
					ball_b.r+= 1
					ball_a.x = x
					ball_a.y = y
					ball_a.r = radius
					ball_a.penup()
					ball_a.goto(x,y)
					ball_a.color(color)
					ball_a.shape("circle")
					ball_a.shapesize(radius/10)
					ball_a.dx = dx
					ball_a.dy =dy

def check_my_ball_collsion():
	for ball_c in BALLS :
		if collide(my_ball,ball_c):
				radius3 = my_ball.r
				radius4 = ball_c.r
				if radius3 <=radius4 :
					 return False
				else :
					my_ball.r+= 1
					ball_c.x = x
					ball_c.y = y
					ball_c.r = radius
					ball_c.penup()
					ball_c.goto(x,y)
					ball_c.color(color)
					ball_c.shape("circle")
					ball_c.shapesize(radius/10)
					ball_c.dx = dx
					ball_c.dy =dy
				
	return True
	
			
def movearound(event):
	x = event.x - screen_width
	y = screen_height - event.y
	my_ball.goto(x,y)

turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()


while RUNNING == True:
	screen_width = turtle.getcanvas().winfo_width()/2
	screen_height = turtle.getcanvas().winfo_height()/2
	move_all_balls()
	check_all_ball_collsion()
	RUNNING = check_my_ball_collsion()
	turtle.update()
	time.sleep(SLEEP)


