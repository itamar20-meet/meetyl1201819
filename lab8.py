import turtle
from turtle import*
import random
class ball(Turtle):
	"""docstring for ball"""
	def __init__(self,radius,color,speed):
		turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
		
ball_1 = ball(3,"green",4)
ball_2 = ball(7,"red",2)

def check_collision(ball_1,ball_2):
	if ball_2[3]+ball_1[3] > 0: 
		print("they collide!!")
	elif ball_2[3]+ball_1[3] < 0:
		print("touching")
    else :
    	print("not touching")