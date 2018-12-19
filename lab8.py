import turtle
from turtle import*
import random
class ball(Turtle):
	"""docstring for ball"""
	def __init__(self,radius,color,speed,x,y):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed = speed
		self.x = x
		self.y = y
		'''self.dx = dx
		self.dy = dy'''

		
	def check_collision(ball_1,ball_2):
		D = math.squr(math.pow(ball_1[3]-ball_2[3])+math.pow(ball_1[4]-ball_2[4]))
		if ball_2[0]+ball_1[0] > D : 
			print("they collide!!")
		elif ball_2[0]+ball_1[0] == D:
			print("touching")
		else:
			print("not touching")

ball_1 = ball(3,"green","fast",100,400)
ball_2 = ball(7,"red","normal",-100,20)


