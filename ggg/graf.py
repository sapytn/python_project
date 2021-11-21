# импортируем модули
import pylab
import matplotlib.path
from microprogram import calc_points


def draw_arc(axes, arc_x, arc_y, arc_width, arc_theta1, arc_theta2):
    """
    Рисование дуги
    """
    # arc_x = 25
    # arc_y = 35
    arc_height = arc_width
    # arc_theta1 = 0
    # arc_theta2 = 180

    arc = matplotlib.patches.Arc((arc_x, arc_y),
                                 arc_width,
                                 arc_height,
                                 theta1=arc_theta1,
                                 theta2=arc_theta2
                                 )
    axes.add_patch(arc)


param = (0, 0, 50, 50, 25, 25, 25)
param1 = (50, 50, 100, 0, 25, -25, 25)
param2 = (100, 0, 50, -50, -25, -25, 25)
param3 = (-50, -50, 0, 0, -25, 25, 25)


axes = pylab.gca()
axes.set_aspect("equal")

# x, y, i, j, r, arc_theta1, arc_theta2 = calc_points(param)
# draw_arc(axes, i, j, r * 2, arc_theta2, arc_theta1)

x, y, i, j, r, arc_theta1, arc_theta2 = calc_points(param)
draw_arc(axes, i, j, r * 2, arc_theta2, arc_theta1)

pylab.plot(x, y)

# показываем график
pylab.show()
