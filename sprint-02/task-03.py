import re, math

def string_parsing(string):
    return {key: (int(x), int(y)) for match in re.finditer(r'([A-Z]{2})(\d):(\d)', string) for key, x, y in [match.groups()]}


def distance_between_neighbor_points(side1, side2):
    x1, y1 = side1
    x2, y2 = side2

    return math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1,2))


def figure_perimetr(string):

    perimeter = 0
    
    quadrilateral_points = string_parsing(string)

    neighbor_points = ('LB','RB'), ('LT','RT'), ('LB', 'LT'), ('RB', 'RT')

    for point in neighbor_points:
        perimeter += distance_between_neighbor_points(quadrilateral_points[point[0]], quadrilateral_points[point[1]])

    
    return round(perimeter, 14)


# test1 = "#LB1:1#RB4:1#LT1:3#RT4:3"
# print(figure_perimetr(test1))

test2 = "#LB0:1#RB5:1#LT4:5#RT8:3"
print(figure_perimetr(test2))
