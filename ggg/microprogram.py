import math



def angle_check(angle_start, angle_end):
    if angle_start > angle_end:
        angle_start, angle_end = angle_end, angle_start
    return angle_start, angle_end


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
    if abs(x_radius) == r and abs(y_radius) != r:
        y_point += y_radius

    elif abs(y_radius) == r and abs(x_radius) != r:
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


def find_angle_arc(dis_radx, y_dis, x_point, r):
    angle_cos = abs((dis_radx - x_point) / r)
    angle = math.degrees(math.acos(angle_cos))
    x_dis = x_point - dis_radx

    if x_dis < 0 and y_dis > 0 and not 90 > angle > 180:
        angle = 180 - angle
    elif x_dis < 0 and y_dis < 0 and not 180 > angle > 270:
        angle = 180 + angle
    elif x_dis > 0 and y_dis < 0 and not 270 > angle > 360:
        angle = 360 - angle
    print("angle", angle, 'x', x_dis, 'y', y_dis)
    return angle


def calc_points(param):
    x_start, y_start, x_end, y_end, i, j, r = param
    dis_radx = x_start + i
    dis_rady = y_start + j
    x = []
    y = []
    x_point = x_start
    y_point = y_start
    x.append(x_point)
    y.append(y_point)

    x_radius, y_radius = i, j

    x_point, y_point = calc_point(x_radius, y_radius, x_point, y_point, r)
    y_dis = y_point - dis_rady
    angle_start = find_angle_arc(dis_radx, y_dis, x_point, r)
    x.append(x_point)
    y.append(y_point)
    # FIRST POINT IS FIND

    x_point = x_end
    y_point = y_end
    x_radius = (x_start + i) - x_end
    y_radius = (y_start + j) - y_end

    x_point, y_point = calc_point(x_radius, y_radius, x_point, y_point, r)
    y_dis = y_point - dis_rady
    angle_end = find_angle_arc(dis_radx, y_dis, x_point, r)
    x.append(x_point)
    y.append(y_point)

    x.append(x_end)
    y.append(y_end)
    angle_start, angle_end = angle_check(angle_start, angle_end)
    return x, y, i + x_start, j + y_start, r, angle_start, angle_end


if __name__ == '__main__':
    param = (0, 0, 100, 0, 50, 50, 25)
    x, y, i, j, r, angle = calc_points(param)
    print("x", x, "y", y)
    print(i, j, r)
