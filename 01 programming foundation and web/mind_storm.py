import turtle

def draw_shapes():
	window = turtle.Screen()
	window.bgcolor('red')

	# draw a square
	def draw_sqare():
		brad = turtle.Turtle()
		brad.shape("circle")
		brad.color("blue")
		brad.fill(True)
		brad.speed(10)
		# repeat drawing square to form circle
		for i in range(1, 37):
			# draw four lines to make a square
			for j in range(1, 5):
				brad.forward(100)  # Move 100 step forward
				brad.right(90)  # turn right at 90 degree angle
			brad.left(10)  # tilt created square left by 10 degree
		brad.fill(False)

	# draw a circle with fill
	def draw_circle():
		angie = turtle.Turtle()
		angie.fill("True")
		angie.shape("arrow")
		angie.color("yellow")
		angie.speed(2)
		angie.circle(100)
		angie.fill("False")

	# draw a triangle with fill
	def draw_triangle():
		titi = turtle.Turtle()
		titi.shape("turtle")
		titi.color("green")
		titi.speed(20)
		# Repeat drawing triangle to make circle
		for i in range(1, 37):
			# repeat drawing line 3 times at angle 150 to create triangle
			for j in range(1, 4):
				titi.forward(150)  # Move forward 150 pixel
				titi.left(120)  # turn left at 120 degree angle
			titi.right(10)

	draw_sqare()
	#draw_circle()
	draw_triangle()
	window.exitonclick()

draw_shapes()