
from packages.Shape import Point, Line, Triangle, Square

def main():
    # Create points
    p1 = Point(0, 0)
    p2 = Point(3, 0)
    p3 = Point(3, 4)

    # Create lines
    line1 = Line(p1, p2)
    line2 = Line(p2, p3)
    line3 = Line(p3, p1)

    # Create a triangle
    triangle = Triangle(is_regular=False, vertices=[p1, p2, p3], edges=[line1, line2, line3])

    # Print the triangle's properties
    print("Vertices:", triangle.get_vertices())
    print("Edges:", triangle.get_edges())
    print("Area:", triangle.compute_area())
    print("Perimeter:", triangle.compute_perimeter())
    print("Inner Angles:", triangle.compute_inner_angles())

    square = Square(vertices=[Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)])
    print("\nSquare Properties:")
    print("Vertices:", square.get_vertices())
    print("Edges:", square.get_edges())
    print("Area:", square.compute_area())
    print("Perimeter:", square.compute_perimeter())
    print("Inner Angles:", square.compute_inner_angles())

main()
