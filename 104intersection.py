#!/usr/bin/python3

import sys
from math import *

def check_shape():
    if int(sys.argv[1]) < 1 or int(sys.argv[1]) > 3:
        print("Please read usage, invalid surface option")
        sys.exit(84)

def check_radius():
    if int(sys.argv[8]) < 0:
        print("Bro radius and angles are not negative please check yourself")
        sys.exit(84)

def check_vector():
    if int(sys.argv[5]) == 0 and int(sys.argv[6]) == 0 and int(sys.argv[7]) == 0:
        sys.exit(84)

def check_angle():
    if int(sys.argv[8]) > 90 and int(sys.argv[1]) == 3:
        sys.exit(84)

def check_inputs():
    argnum = 1
    if len(sys.argv) == 2 and sys.argv[1] == "-h":
        print_usage()
        sys.exit(0)
    if len(sys.argv) != 9:
        print("Invalid number of arguments", file = sys.stderr)
        sys.exit(84)
    while (argnum < 9):
        try:
            float(sys.argv[argnum])
        except ValueError:
            print('Please enter numerical values for the coordinates')
            sys.exit (84)
        argnum = argnum + 1
    check_shape()
    check_radius()
    check_vector()
    check_angle()
    

def print_usage():
    print("USAGE")
    print("\t./104intersection opt xp yp zp xv yv zv p")
    print("DESCRIPTION")
    print("\topt\t\tsurface option: 1 for a sphere, 2 for a cylinder, 3 for a cone")
    print("\t(xp, yp, zp)\tcoordinates of a point by which the light ray passes through")
    print("\t(xv, yv, zv)\tcoordinates of a vector parallel to the light ray")
    print("\tp\t\tparameter: radius of the sphere, radius of the cylinder, or\n\t\t\tangle formed by the cone and the Z-axis")

def indentify_shape(argument):
    switcher = {
        1: "Sphere",
        2: "Cylinder",
        3: "Cone"        
    }
    return (switcher.get(argument))

def header_display(shape, point, vector):
    if (sys.argv[1] == "3"):
        print(shape, "with a", sys.argv[8], "degree angle")
        print("Line passing through the point",tuple(point),"and parallel to the vector",tuple(vector))
    if (sys.argv[1] == "1" or sys.argv[1] == "2"):
        print(shape, "of radius", sys.argv[8])
        print("Line passing through the point",tuple(point),"and parallel to the vector",tuple(vector))

def get_points(solutions, vector, point):
    for root in solutions:
        x = point[0] + root * vector[0]
        y = point[1] + root * vector[1]
        z = point[2] + root * vector[2]
        print("({:.3f}, {:.3f}, {:.3f})".format(x, y, z))

def cone_intersection(point, vector, angle):
    angle = angle * pi / 180
    a = vector[0] ** 2 + vector[1] ** 2 - vector[2] ** 2 * tan(angle) ** 2
    b = (point[0] * vector[0] * 2) + (point[1] * vector[1] * 2) - (2 * point[2] * vector[2]) * tan(angle) ** 2
    c = point[0] ** 2 + point[1] ** 2 - point[2] ** 2 * tan(angle) ** 2

    delta = b ** 2 - 4 * a * c

    if vector[0] == 0 and vector[1] == 0:
        print("There is an infinite number of intersection points.")
    elif delta > 0:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        print("2 intersection points:")
        get_points([x1, x2], vector, point)
    elif delta == 0:
        x1 = -b / (2 * a)
        print("1 intersection point:")
        get_points([x1], vector, point)
    else:
        print("No intersection point.")

def cylinder_intersection(point, vector, radius):
    a = vector[0] ** 2 + vector[1] ** 2
    b = (point[0] * vector[0]) * 2 + (point[1] * vector[1]) * 2
    c = point[0] ** 2 + point[1] ** 2 - radius ** 2

    delta = b ** 2 - 4 * a * c

    if vector[0] == 0 and vector[1] == 0 and point[0] ** 2 + point[1] ** 2 == radius ** 2:
        print("There is an infinite number of intersection points.")
    elif delta > 0:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        print("2 intersection points:")
        get_points([x1, x2], vector, point)
    elif delta == 0:
        x1 = -b / (2 * a)
        print("1 intersection point:")
        get_points([x1], vector, point)
    else:
        print("No intersection point.")
    
def sphere_intersections(point, vector, radius):
    a = vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2
    b = 2 * (vector[0] * point[0] + vector[1] * point[1] + vector[2] * point[2])
    c = point[0] ** 2 + point[1] ** 2 + point[2] ** 2 - radius ** 2

    delta = b ** 2 - 4 * a * c

    if delta > 0:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
        print("2 intersection points:")
        get_points([x1, x2], vector, point)
    elif delta == 0:
        x1 = -b / (2 * a)
        print("1 intersection point:")
        get_points([x1], vector, point)
    else:
        print("No intersection point.")

def main():
    check_inputs()
    shape = indentify_shape(int(sys.argv[1]))
    point = [int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])]
    vector = [int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7])]

    header_display(shape, point, vector)
    if (sys.argv[1] == "1"):
        sphere_intersections(point, vector, int(sys.argv[8]))
    if (sys.argv[1] == "2"):
        cylinder_intersection(point, vector, int(sys.argv[8]))
    if (sys.argv[1] == "3"):
        cone_intersection(point, vector, int(sys.argv[8]))

if __name__ == "__main__":
    main()