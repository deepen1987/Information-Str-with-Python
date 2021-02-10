# CS521 - A2
# Deependrasingh Shekhawat
# Script for Area between co-ordinates

import math


def distance_between_city(x1, y1, x2, y2):
    earth_radius = 6371
    distance = earth_radius * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))
    return distance


# Calculating sides triangle
def side_of_triangle(side1, side2, side3):
    side = (side1 + side2 + side3) / 2
    return side


# Calculate area of triangle
def area_of_triangle(side, side1, side2, side3):
    triangle_area = math.sqrt(side * (side - side1) * (side - side2) * (side - side3))
    return triangle_area


# Co-ordinates for Atlanta
a1, a2 = -84.5545400, 33.7405800
a1 = math.radians(a1)
a2 = math.radians(a2)

# Co-ordinates for Orlando
o1, o2 = -81.5250400, 28.4115300
o1 = math.radians(o1)
o2 = math.radians(o2)

# Co-ordinates for Savannah
s1, s2 = -81.1998900, 32.1672300
s1 = math.radians(s1)
s2 = math.radians(s2)

# Co-ordinates for Charlotte
c1, c2 = -80.9567600, 35.2072400
c1 = math.radians(c1)
c2 = math.radians(c2)

# Calculate distance between cities
c_a_distance = distance_between_city(c1, c2, a1, a2)
c_s_distance = distance_between_city(c1, c2, s1, s2)
s_a_distance = distance_between_city(s1, s2, a1, a2)
o_a_distance = distance_between_city(o1, o2, a1, a2)
s_o_distance = distance_between_city(s1, s2, o1, o2)

area = area_of_triangle(side_of_triangle(c_a_distance, c_s_distance, s_a_distance),
                        c_a_distance, c_s_distance, s_a_distance) + \
       area_of_triangle(side_of_triangle(s_a_distance, s_o_distance, o_a_distance),
                        s_a_distance, s_o_distance, o_a_distance)

print(f"""Total area enclosed between Atlanta, Orlando, 
Savannah and Charlotte is {area}""")
