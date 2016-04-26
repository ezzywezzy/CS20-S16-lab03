import turtle
import math



frank = turtle.Turtle()
frank.penup()
frank.goto(-75, 0)


# w=width h=height s=space between lettters
def drawE(bill, w, h, s):
    bill.pendown()
    bill.left(90)
    bill.forward(h)
    #makes backbone of "E"
    bill.right(90)
    bill.forward(w)
    bill.right(90)
    bill.penup()
    bill.forward(h/2)
    bill.pendown()
    bill.right(90)
    bill.forward(w)
    bill.left(90)
    bill.forward(h/2)
    bill.right(90*3)
    bill.forward(w)
    #makes lines of "E"
    bill.penup()
    bill.forward(s)
    #spacing for the next letter
    
def drawK(bill, w, h, s):
    bill.pendown()
    bill.left(90)
    bill.forward(h)
    bill.right(90)
    bill.penup()
    bill.forward(w)
    bill.right(180)
    bill.pendown()
    x = math.atan((.5*h)/w)
    bill.left(math.degrees(x))
    z = math.sqrt((h/2)**2 + w**2)
    bill.forward(z)
    bill.left(90-math.degrees(x))
    bill.left(math.degrees(math.atan(w/(.5*h))))
    bill.forward(z)
    
frank.speed(400)


#drawE(frank, 50, 100, 50)
#drawK(frank, 50, 100, 50)


def drawInitial(bill, w, h, s):
    drawE(bill, w, h, s)
    drawK(bill, w, h, s)

drawInitial(frank, 50, 100, 50)










turtle.done()

