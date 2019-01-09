
import turtle
from turtle import Turtle


class Ball(Turtle):
	"""docstring for Ball"""
	def __init__(self, x, y ,dx, dy,r, color,shape):
		Turtle.__init__(self)
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.r = r
		self.color("red")
		self.shape("circle")
		turtle.penup()
		turtle.goto(x, y)
		turtle.shapesize(r/10)
		
	def move(self,screen_width, screen_height):
			current_x = self.xcor()
			new_x = current_x + self.dx
			current_y = self.ycor()
			new_y = current_y + self.dy
			right_ball_side = new_x + self.r
			left_ball_side = new_x + self.r
			up_ball_side = new_y + self.r
			down_ball_side = new_y + self.r
			if screen_height == up_ball_side :
				dy = dy-5
			elif screen_height == down_ball_side*(-1):
				dy = dy-5
			elif screen_width == left_ball_side*(-1):
				dx = dx+5
			elif screen_width == right_ball_side:
				dx = dx+5
			else:
				pass
			


		