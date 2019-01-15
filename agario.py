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

my_ball = Ball(0,0,4,-1,50,"orange")


NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
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

for i in BALLS:
	ball.move(400,300)

def collide(ball1 ,ball2):

	x1 = ball1.xcor() 
	y1 = ball1.ycor()
	x2 = ball2.xcor()
	y2 = ball2.ycor()

	d_between = math.sqrt(math.pow((x1 - x2),2) + math.pow((y1 - y2),2))
	sum_radius = ball1.r + ball2.r
	if ball1 == ball2:
		return "false"
	elif sum_radius >= d_between:
		return "True"
	else :
		return "false"
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
				Radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
				colour =(random.random(), random.random(), random.random())
				if radius1> radius2 :
					ball_a.r+= 1
					ball_b = Ball(x, y, dx, dy, Radius, colour)
				elif radius1< radius2 :
					ball_b.r+= 1
					ball_a = Ball(x, y, dx, dy, Radius, colour)

def check_my_ball_collsion():
	for ball_c in BALLS :
		if collide(my_ball,ball_c):
				radius3 = my_ball.r
				radius4 = ball_c.r
				if radius3 > radius4:
					my_ball.r+= 1
					ball_c = Ball(x, y, dx,dy, Radius, colour )
				elif radius3 < radius4 :
					return "false"
	return "True"
			
def movearound(event):
	x = event.x - screen_width
	y = screen_height - event.y
	my_ball.goto(x,y)

turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()



check_all_ball_collsion()
check_my_ball_collsion()


turtle.mainloop()