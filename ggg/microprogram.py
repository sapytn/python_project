import math


# param = (10, 10, 110, 10, 45, 50, 25)


def calc_angle(x_radius, y_radius, r):
    distance_radius = math.sqrt(x_radius ** 2 + y_radius ** 2)
    distance_start = math.sqrt(distance_radius ** 2 - r ** 2)
    cos_radius = abs(x_radius / distance_radius)
    sin_radius = abs(y_radius / distance_radius)
    cos_start = abs(distance_start / distance_radius)
    sin_start = abs(r / distance_radius)
    sin_angle = sin_radius * cos_start + cos_radius * sin_start
    cos_angle = cos_radius * cos_start - sin_radius * sin_start
    return distance_start, sin_angle, cos_angle


def calc_points(param):
    x_start, y_start, x_end, y_end, i, j, r = param
    x = []
    y = []

    x_radius = i
    y_radius = j

    x_point = x_start
    y_point = y_start
    x.append(x_point)
    y.append(y_point)

    if i == r:
        y_point += y_radius
    elif j == r:
        x_point += x_radius
    else:
        distance_start, sin_angle, cos_angle = calc_angle(x_radius, y_radius, r)
        x_distance, y_distance = distance_start * cos_angle, distance_start * sin_angle
        if i > 0 and j > 0:
            x_point += abs(x_distance)
            y_point += abs(y_distance)
        elif i < 0 and j > 0:
            x_point -= x_start - abs(x_distance)
            y_point = y_start + abs(y_distance)
        elif i > 0 and j < 0:
            x_point = x_start + abs(x_distance)
            y_point = y_start - abs(y_distance)
        else:
            x_point = x_start - abs(x_distance)
            y_point = y_start - abs(y_distance)
    # print(f'x1 {x_pont} y1 {y_point}')
    # print(x_point, y_point)
    x.append(x_point)
    y.append(y_point)
    first_angle = math.degrees(math.acos((x_point - (x_start + x_radius)) / r))
    # FIRST POINT IS FIND

    x_point, y_point = x_end, y_end
    x_radius = x_end - (x_start + i)
    y_radius = y_end - (y_start + j)

    if x_radius == r and y_radius == y_end:
        y_point -= y_radius

    elif x_radius == r:
        x_point -= x_radius

    elif y_radius == r and x_radius == x_end:
        x_point -= x_radius

    elif y_radius == r:
        y_point -= y_radius

    else:
        distance_start, sin_angle, cos_angle = calc_angle(x_radius, y_radius, r)
        # if x_end - x_radius == r:
        #     x_point = x_end - x_radius
        # if y_end - y_radius == r:
        #     y_point = y_end - y_radius

        # print(f'x2 {x_end - distance_start * sin_angle} y2 {y_end + distance_start * cos_angle}')
        # print(x_end - distance_start * sin_angle, y_end + distance_start * cos_angle)

        x_point, y_point = distance_start * cos_angle, distance_start * sin_angle
        if i > 0 and j > 0:
            x_point = x_end - abs(x_point)
            y_point = y_end + abs(y_point)
        elif i < 0 and j > 0:
            x_point += abs(x_point)
            y_point += abs(y_point)
        elif i > 0 and j < 0:
            x_point -= abs(x_point)
            y_point -= abs(y_point)
        else:
            x_point += abs(x_point)
            y_point -= abs(y_point)

    # print(f'x2 {x_pont} y2 {y_point}')
    # print(x_point, y_point)
    x.append(x_point)
    y.append(y_point)
    second_angle = math.degrees(math.acos((x_point - (x_end - x_radius)) / r))
    # print(f'x_end {x_end} y_end {y_end}')
    # print(x_end, y_end)
    x.append(x_end)
    y.append(y_end)
    return x, y, i + x_start, j + y_start, r, first_angle, second_angle


if __name__ == '__main__':
    param = (0, 0, 50, 50, 25, 25, 25)
    x, y, i, j, r, arc_theta1, arc_theta2 = calc_points(param)
    print("x", x, "y", y)
    print(i, j, r)
