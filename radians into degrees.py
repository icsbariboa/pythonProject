import math


def radians_to_degree(radian):
    degree = (int(radian) * (180 / math.pi))
    return degree


radian_input = int(input())
print(f"radian: {radian_input}")
degree_output = radians_to_degree(radian_input)
print(f"degree: {degree_output}")
