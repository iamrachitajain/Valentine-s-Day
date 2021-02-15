import turtle

turtle.bgcolor("black")
pen = turtle.Turtle()
pen.pencolor("red")

def curve():
	for i in range(200):
		pen.right(1)
		pen.forward(1)

def heart():
	pen.fillcolor("red")
	pen.begin_fill()
	pen.left(140)
	pen.forward(113)
	curve()
	pen.left(120)
	curve()
	pen.forward(112)
	pen.end_fill()

def txt():
	pen.up()
	pen.setpos(-58, 95)
	pen.down()
	pen.color("black")
	pen.write("I Love Baby", font=("Verdana", 15, "bold"))

heart()
while(1):
	txt()
	pen.ht()