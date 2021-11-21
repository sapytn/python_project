import math


def calc_angle():
    pass


def calc_point():
    x = 0
    y = 0
    i = 25
    j = 50
    r = 25
    hyp_radius = math.sqrt(i ** 2 + j ** 2)
    distance_point = math.sqrt(hyp_radius ** 2 - r ** 2)
    cosa = abs(i / hyp_radius)
    cosb = abs(distance_point / hyp_radius)
    sina = abs(j / hyp_radius)
    sinb = abs(r / hyp_radius)

    sin_angle = sina * cosb + cosa * sinb
    cos_angle = cosa * cosb - sina * sinb

    x_point = cos_angle * distance_point
    y_point = sin_angle * distance_point




calc_point()
