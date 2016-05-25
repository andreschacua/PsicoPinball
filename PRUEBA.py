from tkinter import *

import math

c = Canvas(width=200, height=200)
c.pack()

# una figura , recordar solo se pueden cosas como poligonos y lineas
xy = [(50, 50), (50, 80), (150, 150),(180,150)]

polygon_item = c.create_polygon(xy)

center = 50, 50 # lugar inicial para parametro

def getangle(event):
    dx = c.canvasx(event.x) - center[0]
    dy = c.canvasy(event.y) - center[1]
    try:
        return complex(dx, dy) / abs(complex(dx, dy))
    except ZeroDivisionError:
        return 0.0 # cannot determine angle

def press(event):
    # calculate angle at start point
    global start
    start = getangle(event)

def motion(event):
    # calculate current angle relative to initial angle
    global start
    angle = getangle(event) / start
    offset = complex(center[0], center[1])
    newxy = []
    for x, y in xy:
        v = angle * (complex(x, y) - offset) + offset
        newxy.append(v.real)
        newxy.append(v.imag)
    c.coords(polygon_item, *newxy)

c.bind("<Button-1>", press)
c.bind("<B1-Motion>", motion)

mainloop()
