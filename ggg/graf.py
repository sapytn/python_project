# импортируем модули
import numpy as np
import matplotlib.pyplot as plt
import pylab
import matplotlib.path

# функция
# y = lambda x: np.sin(x)
# создаём рисунок с координатную плоскость
fig = plt.subplots()
# создаём область, в которой будет
# - отображаться график
# x = np.linspace(-3, 3,100)
# значения x, которые будут отображены
# количество элементов в созданном массиве
# - качество прорисовки графика
# рисуем график
x = [10, 37.21405430584632, 82.78594569415368, 110]
y = [10, 70.2859456941537, 70.2859456941537, 10]
#
# plt.plot(x,y)

plt.plot(x, y)


def drawArc(axes):
    """
    Рисование дуги
    """
    arc_x = 0
    arc_y = 0
    arc_width = 1
    arc_height = 1
    arc_theta1 = 270
    arc_theta2 = 360

    arc = matplotlib.patches.Arc((arc_x, arc_y),
                                 arc_width,
                                 arc_height,
                                 theta1=arc_theta1,
                                 theta2=arc_theta2)
    axes.add_patch(arc)
    pylab.text(0.6, -0.3, "Arc", horizontalalignment="center")

drawArc(50,50,25,25)


# показываем график
plt.show()
