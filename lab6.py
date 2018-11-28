import turtle 
import random 
from turtle import Turtle
from turtle import*
colormode(255)
colors =("blue","green","red","orange","purple","yellow")
class Square(Turtle):
	"""docstring for square"""
	def __init__(self, size,shape=turtle.shape("square")):
		self.size = size

	def random_color(self,red,blue,green):
		color = random.choice(colors)
		turtle.color(color)

a = Square(10)

a.random_color(50,50,0)

turtle.begin_poly()
turtle.forward(50)
turtle.left(60)
turtle.forward(50)
turtle.left(60)
turtle.forward(50)
turtle.left(60)
turtle.forward(50)
turtle.left(60)
turtle.forward(50)
turtle.left(60)
turtle.forward(50)
turtle.left(60)
turtle.end_poly()
S = turtle.get_poly()
register_shape("hexagon",S)

class Hexagon(Turtle):
	"""docstring for hexagon"""
	def __init__(self,size):
		self.size = size
		self.shape("hexagon")
		









turtle.mainloop()