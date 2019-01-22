
import turtle
from turtle import Turtle


class Ball(Turtle):
	"""docstring for Ball"""
	def __init__(self, x, y ,dx, dy,r, color):
		Turtle.__init__(self)
		self.penup()
		self.goto(x, y)
		self.x = x
		self.y = y
		self.dx = dx
		self.dy = dy
		self.r = r
		self.color(color)
		self.shape("circle")
		self.shapesize(r/10)
		self.showturtle()
	def move(self,screen_width, screen_height):
			current_x = self.xcor()
			new_x = current_x + self.dx
			current_y = self.ycor()
			new_y = current_y + self.dy
			right_ball_side = new_x + self.r
			left_ball_side = new_x - self.r
			up_ball_side = new_y + self.r
			down_ball_side = new_y - self.r
			self.goto(new_x,new_y)
			if screen_height <= up_ball_side :
				self.dy = -self.dy
			elif -screen_height >= down_ball_side:
				self.dy = -self.dy
			elif -screen_width >= left_ball_side:
				self.dx = -self.dx
			elif screen_width <= right_ball_side:
				self.dx = -self.dx

			

'''my_ball = Ball(0,0,2,2,50,"red")
while True:
	my_ball.move(200,200)
turtle.mainloop()'''
		