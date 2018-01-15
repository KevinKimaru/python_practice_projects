from turtle import *
import tkinter

colors = {
    'red': '#f73400',
    'green': '#fffff0',
    'blue': '#45ff45'
}

screen = Screen()
screen.setup(800, 800)
screen.bgcolor(colors['green'])

pendown()
# penup()
goto(0, 100)
color(colors['red'])
style = ('Arial', 40, 'bold')
write('HELLO', font=style, align='center')

right(90)
forward(60)
color(colors['blue'])
write('WORLD', font=style, align='center')

goto(200, 200)
circle(50)
hideturtle()

right(120)
forward(120)
dot(100)

tkinter.mainloop()