from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.
def draw_square(x, y):
    square = canvas.create_rectangle(x, y, x+50, y+50, fill = "red")

draw_square(20, 60)
draw_square(10, 40)
draw_square(180, 210)

root.mainloop()
