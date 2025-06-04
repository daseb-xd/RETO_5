# RETO_5
Ejercicio de crear un paquete con la clase shape

Primero se crea una carpeta general Files, aqui tendremos nuestreo archivo principal y nuestro módulo del cual importamos las clases de ```Point```, ```Line``` y 2 de las figuras que heredan de la clase ```Shape```

### Ejemplo del código

```python
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
```
El output es el siguiente:
```Python
Vertices: [Point(0, 0), Point(3, 0), Point(3, 4)]
Edges: [Line(Point(0, 0), Point(3, 0)), Line(Point(3, 0), Point(3, 4)), Line(Point(3, 4), Point(0, 0))]
Area: 6.0
Perimeter: 12.0
Inner Angles: [36.87, 53.13, 90.0]

Square Properties:
Vertices: [Point(0, 0), Point(1, 0), Point(1, 1), Point(0, 1)]
Edges: [Line(Point(0, 0), Point(1, 0)), Line(Point(1, 0), Point(1, 1)), Line(Point(1, 1), Point(0, 1)), Line(Point(0, 1), Point(0, 0))]
Area: 1.0
Perimeter: 4.0
Inner Angles: [90, 90, 90, 90]
```

Así, es posible usar todo el código de ```Shape.py``` sin necesidad de ponerlo todo en ```main.py```
