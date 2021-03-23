from graphics import circle, rect
from graphics.subgrapics.cuboid import *
from graphics.subgrapics import sphere as s

r = int(input("Enter the radius:"))
print("Area of the given circle=", circle.area(r))
print("Perimeter of the given circle=", circle.perimeter(r))


l = int(input("\nEnter length of the rectangle:"))
b = int(input("Enter the breadth of the rectangle:"))
print("Area of the given rectangle=", rect.area(l,b))
print("Perimeter of the given rectangle=", rect.perimeter(l,b))


l = int(input("\nEnter length of the cuboid:"))
b=int(input("Enter breadth of the cuboid:"))
h=int(input("Enter height of the cuboid:"))
print("Area of the given cuboid=", area(l, b, h))
print("Perimeter of the given cuboid=", perimeter(l, b, h))


r = int(input("\nEnter the radius of the sphere:"))
print("Area of the given sphere=", s.area(r))
print("Perimeter of the given circle=", s.perimeter(r))
