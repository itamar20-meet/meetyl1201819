import turtle 
import random 
from turtle import Turtle
import colormode(255 )
colors =("blue","green","red","orange","purple","yellow")
class Square(Turtle):
	"""docstring for square"""
	def __init__(self, size,shape=turtle.shape("square")):
		self.size = size

	def random_color(self,red,blue,green):
		color = random.choice(colors)
		turtle.color(color)

a = Square(10)

a.random_color()

turtle.mainloop()