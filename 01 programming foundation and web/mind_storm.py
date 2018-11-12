import turtle

def draw_square():
	window = turtle.Screen()
	window.bgcolor('red')

	brad = turtle.Turtle()
	brad.shape("circle")
	brad.color("blue")
	brad.fill(True)
	brad.shapesize(2,2)

	brad.speed(2)
	brad.forward(100)  # Move 100 step forward
	brad.right(90)  # turn right at 90 degree angle
	brad.forward(100)  # Move 100 step forward
	brad.right(90)  # turn right at 90 degree angle
	brad.forward(100)  # Move 100 step forward
	brad.right(90)  # turn right at 90 degree angle
	brad.forward(100)  # Move 100 step forward
	brad.right(90)  # turn right at 90 degree angle
	brad.fill(False)

	window.exitonclick()

draw_square()