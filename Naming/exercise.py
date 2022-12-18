class Point:
    def __init__(self, coordX, coordY):
        self.coordX = coordX
        self.coordY = coordY


class Rectangle:
    def __init__(self, starting_point, width, high):
        self.starting_point = starting_point
        self.width = width
        self.high = high

    def area(self):
        return self.width * self.high

    def print_vertices(self):
        top_right_vertix = self.starting_point.coordX + self.width
        bottom_left_vertix = self.starting_point.coordY + self.high
        print('Starting Point (X)): ' + str(self.starting_point.coordX))
        print('Starting Point (Y)): ' + str(self.starting_point.coordY))
        print('End Point X-Axis (Top Right): ' + str(top_right_vertix))
        print('End Point Y-Axis (Bottom Left): ' + str(bottom_left_vertix))


def build():
    main_point = Point(50, 100)
    rectangle = Rectangle(main_point, 90, 10)

    return rectangle


first_rectangle = build()

print(first_rectangle.area())
first_rectangle.print_vertices()