import turtle

turtle.register_shape("pet-plastic-bottle-40x40.gif")
turtle.shape("pet-plastic-bottle-40x40.gif")
x=0
turtle.speed(100000000000000000000)
for i in range(2000):
	turtle.right(x)
	turtle.forward(300)
	turtle.right(55)
	turtle.forward(120)
	turtle.right(90)
	turtle.forward(40)
	turtle.pensize(2)
	turtle.forward(70)
	turtle.pensize(1)
	turtle.forward(20)
	turtle.home()
	x=x+1


