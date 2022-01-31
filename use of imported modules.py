import ShapeAreas

result = ShapeAreas.areaRect(4, 8) - ShapeAreas.areaRect(2, 3) - ShapeAreas.areaCircle(1.75)
print("The area of the room =", result, "\n")
print ("or\n\n")
result = ShapeAreas.areaRect(4, 5) + ShapeAreas.areaRect(2, 3) - ShapeAreas.areaCircle(1.75)
print("The area of the room =", result, "\n")
