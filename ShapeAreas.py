def areaCircle(aDiameter):
    Pi = 3.142
    area1 = Pi * (aDiameter/2) **2
    return area1
def areaRect(width, length):
    area = width * length
    return area
def areaTriangleHeron(side1, side2,side3):
    area2 = (side1 + side2 + side3) / 2
    area3 = (area2 * (area2 - side1) * (area2 - side2) * (area2 - side3)) ** 0.5
    return area3
