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
		brad.speed(2)
		line_count = 0
		no_line = 4
		while line_count < no_line:
			brad.forward(100)  # Move 100 step forward
			brad.right(90)  # turn right at 90 degree angle
			line_count = line_count + 1
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
		titi.fill("True")
		titi.shape("triangle")
		titi.color("green")
		titi.speed(2)
		# repeat drawing 3 times
		for i in range(1, 4):
			titi.forward(150)  # Move forward 150 pixel
			titi.left(120)  # turn left at 120 degree angle
		titi.fill("False")

	draw_sqare()
	draw_circle()
	draw_triangle()
	window.exitonclick()

draw_shapes()