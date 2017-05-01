import math
from operator import attrgetter

def calculate_area(radius, height):
    pi = math.pi
    return ((radius * radius * pi) + calculate_border_area(radius, height))

def calculate_border_area(radius, height):
    return (2 * math.pi * radius * height)

class Pankake:

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        self.area = calculate_area(radius, height)
        self.borderArea = calculate_border_area(radius, height)
    
    def __repr__(self):
        return repr((self.radius, self.height, self.area, self.borderArea))

test_case = int(input())

for i in range(1, test_case + 1):
    total_pancakes, stack_size = [int(s) for s in input().split()]
    pankakes = []
    pankakes_clone = []
    max_area = 0

    for j in range(total_pancakes):
        rad, hei = [int(s) for s in input().split()]
        pank = Pankake(rad, hei)
        pankakes.append(pank)

    #print(pankakes)
    
    if (stack_size == 1):
        pankakes = sorted(pankakes, key=attrgetter('area'), reverse=True)
        max_area = pankakes[0].area
    else:
        max_area = 0
        pankakes = sorted(pankakes, key=attrgetter('borderArea'), reverse=True)
        for p in range(total_pancakes):
            pankakes_clone = pankakes.copy()
            area = pankakes_clone[p].area
            pankakes_clone.pop(p)
            for j in range(1, stack_size):
                area += pankakes_clone[0].borderArea
                pankakes_clone.pop(0)
            max_area = max(max_area, area)

    print('Case #' + str(i) + ': ' + str(max_area))



    
