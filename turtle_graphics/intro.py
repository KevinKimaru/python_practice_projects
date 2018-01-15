import random
import tkinter
import turtle as t


def square(length):
    for i in range(4):
        t.fd(length)
        t.left(90)


# print(dir(t))
# print(help(t.forward))

# t.fd(100)#forward()
# t.bk(200)#backward() back()

# t.shape("turtle")

# t.hideturtle()
# t.showturtle()

# t.seth(90)#setheading()
# t.rt(90)#right()
# t.lt(90)#left()

# penup()
# pendown()

# t.speed(1)
# t.seth(135)
# t.fd(100)
# t.seth(270)
# t.fd(100)
# t.seth(45)
# t.fd(100)

# t.setpos(100, -100)#setposition(100, -100), goto(100, -100)

# clears the drawing from the graphics window but it leaves the turtle in its current position with its current heading
'''t.clear()'''
# clears the drawing and also returns the turtle to its starting position in the center of the screen
'''t.reset()'''

# clockwise positive towards the right
'''t.circle(100)'''
# anticlockwise negative towards the left
'''t.circle(-60)'''

# range of 1-10,,increasing from 1 to 10,,however 0 is the fastest speed
'''t.speed(1)'''

# to remove all animation ie the drawing so the drawing will be immeadiately
'''t.tracer(0, 0)'''  # In this case you have to call t.update after setting up th drawing : as follows:
'''t.update()'''
# restore animation to the default settings
'''t.tracer(1, 10)'''

'''t.color("blue")'''
'''t.pensize()'''  # t.width()
'''t.bgcolor("white")'''

'''t.begin fill()'''
# draw stuff
'''t.end_fill()'''

# EXAMPLE1================
# t.fd(100)
# t.lt(90)
# t.fd(100)
# t.lt(90)
# t.fd(100)
# t.lt(90)
# t.fd(100)
#
# t.penup()
# t.setposition(100, -100)
# t.pendown()
# t.fd(130)

# EXAMPLE2=================
# def square(length):
#     for i in range(4):
#         t.fd(length)
#         t.left(90)
#
# square(60)
# square(100)
# square(200)

# EXAMPLE3============

# t.tracer(0, 0)
# t.circle(100)
# t.circle(-100)
# t.update()

# EXAKPLE 4========
# t.color("red")
# t.pensize(20)
# t.fd(100)
# t.bgcolor("light blue")

'''EXAMPLE 5====================='''
# colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
# t.tracer(0, 0)
# for angle in range(0, 360, 1):
#     t.color(random.choice(colors))
#     t.seth(angle)
#     t.circle(100)
# t.update()



'''EXAMPLE 6====================='''
# colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
# t.tracer(0,0)
# for i in range(45):
#     t.color(colors[i % 6])
#     t.pendown()
#     t.fd(2 + i * 5)
#     t.left(45)
#     t.width(i)
#     t.penup()
# t.update()

# EXAMPLE 7==========================
# t.color("green")
# t.begin_fill()
# square(200)
# t.end_fill()

# t.width(10)
# t.begin_fill()
# t.fd(150)
# t.seth(45)
# t.fd(150)
# t.seth(90)
# t.fd(150)
# t.color("blue")
# t.end_fill()

'''EXAMPLE 8 ================================FIBONACCI SEQUENCE'''
def drawfib(n, len_ang):
    t.fd(2 * len_ang)
    if n == 0:
        pass
    elif n == 1:
        pass
    else:
        t.left(len_ang)
        drawfib(n - 1, len_ang)
        t.right(2 * len_ang)
        drawfib(n - 2, len_ang)
        t.left(len_ang)
    t.bk(2 * len_ang)


start_points = [[-300, 250], [-150, 250],
                [-300, 110], [-80, 110],
                [-300, -150], [50, -150]]
# n = 0

# for start_point in start_points:
#     x, y = start_point
#     n = n + 1
#     t.penup()
#     t.setpos(x, y)
#     t.pendown()
#     drawfib(n, -30)



# t.tracer(0, 0)
# drawfib(15, 14)
# t.update()
# tkinter.mainloop()



