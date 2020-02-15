# two find distance between two co-ordinates
import math             # to use sqrt function it has been imported from math

x1 = int(input("enter X1 point"))
x2 = int(input("enter X2 point"))
y1 = int(input("enter Y1 point"))
y2 = int(input("enter Y2 point"))

dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("Distance between two points is ", dist, "units")
