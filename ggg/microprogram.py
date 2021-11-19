import math

param = (0, 0, 70, 10, 25, 35, 25)


# param = (10, 0, 100, 0, 45, 50, 25)


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
    # print(f'x0 {x_start} y0 {y_start}')
    print(x_start, y_start)

    x_radius = i
    y_radius = j

    x_point = x_start
    y_point = y_start

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
    print(x_point, y_point)
    x_point, y_point = x_end, y_end
    x_radius = x_end - (x_start + i)
    y_radius = y_end - (y_start + j)
    print(f'x{x_radius} y{y_radius}')

    if x_radius == r:
        y_point -= y_radius

    elif y_radius == r:
        x_point -= x_radius

    else:
        distance_start, sin_angle, cos_angle = calc_angle(x_radius, y_radius, r)
        if cos_angle == 0 or sin_angle == 0:
            # print(f'x2 {x_end - distance_start * sin_angle} y2 {y_end + distance_start * cos_angle}')
            print(x_end - distance_start * sin_angle, y_end + distance_start * cos_angle)
        else:
            x_pont, y_point = distance_start * cos_angle, distance_start * sin_angle
            if i > 0 and j > 0:
                x_point -= abs(x_pont)
                y_point += abs(y_point)
            elif i < 0 and j > 0:
                x_point += abs(x_pont)
                y_point += abs(y_point)
            elif i > 0 and j < 0:
                x_point -= abs(x_pont)
                y_point -= abs(y_point)
            else:
                x_point += abs(x_pont)
                y_point -= abs(y_point)
    # print(f'x2 {x_pont} y2 {y_point}')
    print(x_point, y_point)
    # print(f'x_end {x_end} y_end {y_end}')
    print(x_end, y_end)


calc_points(param)
