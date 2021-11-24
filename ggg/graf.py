# импортируем модули
import pylab
import matplotlib.path
from microprogram import calc_points
import matplotlib.pyplot as plt
from matplotlib.ticker import  MultipleLocator
import numpy as np


# plt.style.use(['dark_background', 'presentation'])


def draw_arc(axes, arc_x, arc_y, arc_width, angle_start, angle_end):
    """
    Рисование дуги
    """
    arc_height = arc_width
    arc = matplotlib.patches.Arc((arc_x, arc_y),
                                 arc_width,
                                 arc_height,
                                 theta1=angle_start,
                                 theta2=angle_end,
                                 color="g",
                                 linewidth=1.0
                                 )
    axes.add_patch(arc)


def draw_line(axes, x, y):
    """
    Рисование линии
    """
    line = pylab.Line2D([x[0], x[1]], [y[0], y[1]], color="g", linewidth=1.0)
    line1 = pylab.Line2D([x[2], x[3]], [y[2], y[3]], color="g", linewidth=1.0)
    axes.add_line(line)
    axes.add_line(line1)


param = (0, 0, 100, 0, 50, 50, 25)
param4 = (0, 0, 100, 0, 50, -50, 25)
param1 = (75, 50, 100, 0, 0, -25, 25)
param2 = (100, 0, 50, -50, -25, -25, 25)
param3 = (-50, -50, 0, 0, -25, 25, 25)


f, ax = plt.subplots()
plt.axis([-30, 130, -80, 80])
# plt.grid()
f.set_facecolor('#eee')


x, y, i, j, r, angle_start, angle_end = calc_points(param)
draw_arc(ax, i, j, r * 2, angle_start, angle_end)
draw_line(ax, x, y)

x, y, i, j, r, angle_start, angle_end = calc_points(param4)
draw_arc(ax, i, j, r * 2, angle_start, angle_end)
draw_line(ax, x, y)

# показываем график
pylab.show()
