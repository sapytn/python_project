import math


# param = (10, 10, 110, 10, 45, 50, 25)


def calc_angle(x_radius, y_radius, r):
    distance_radius = math.sqrt(x_radius ** 2 + y_radius ** 2)
    distance_point = math.sqrt(distance_radius ** 2 - r ** 2)
    cos_radius = abs(x_radius / distance_radius)
    sin_radius = abs(y_radius / distance_radius)
    cos_start = abs(distance_point / distance_radius)
    sin_start = abs(r / distance_radius)
    sin_angle = sin_radius * cos_start + cos_radius * sin_start
    cos_angle = cos_radius * cos_start - sin_radius * sin_start
    x_point = distance_point * cos_angle
    y_point = distance_point * sin_angle
    return x_point, y_point


def calc_point(x_radius, y_radius, x_point, y_point, r):
    print('i', x_radius, 'j', y_radius)
    if abs(x_radius) == r:
        y_point += y_radius

    elif abs(y_radius) == r:
        x_point += x_radius

    else:
        x_dist, y_dist = calc_angle(x_radius, y_radius, r)

        if x_radius > 0:
            x_point += x_dist
        else:
            x_point -= x_dist
        if y_radius > 0:
            y_point += y_dist
        else:
            y_point -= y_dist

    return x_point, y_point


def calc_points(param):
    x_start, y_start, x_end, y_end, i, j, r = param
    x = []
    y = []
    x_point = x_start
    y_point = y_start
    x.append(x_point)
    y.append(y_point)

    x_radius, y_radius = i, j

    x_point, y_point = calc_point(x_radius, y_radius, x_point, y_point, r)
    x.append(x_point)
    y.append(y_point)
    # FIRST POINT IS FIND

    x_point = x_end
    y_point = y_end
    x_radius = (x_start + i) - x_end
    y_radius = (y_start + j) - y_end

    x_point, y_point = calc_point(x_radius, y_radius, x_point, y_point, r)
    x.append(x_point)
    y.append(y_point)

    x.append(x_end)
    y.append(y_end)
    return x, y, i + x_start, j + y_start, r


if __name__ == '__main__':
    param = (0, 0, 100, 50, 25, 25, 25)
    x, y, i, j, r = calc_points(param)
    print("x", x, "y", y)
    print(i, j, r)
