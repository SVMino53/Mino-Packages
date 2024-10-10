from typing import Type, Any, Literal
import math

import __error_handler as erh


class Point:

    def __init__(self, x : float, y : float) -> None:
        self.x = x
        self.y = y

    @property
    def x(self) -> float:
        return self.__x
    
    @property
    def y(self) -> float:
        return self.__y
    
    @x.setter
    def x(self, x : float) -> None:
        if isinstance(x, (float, int)):
            self.__x = float(x)
        else:
            erh.__type_error_msg('x', type(x), float)

    @y.setter
    def y(self, y : float) -> None:
        if isinstance(y, (float, int)):
            self.__y = float(y)
        else:
            raise TypeError(f"'y' is of type '{type(y).__name__}'; must be 'float'")
        

    def __add__(self, other : "Point") -> "Point":
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise TypeError(f"incompatible types for operation; '{type(self).__name__}' + '{type(other).__name__}'")

    def __sub__(self, other : "Point") -> "Point":
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        else:
            raise TypeError(f"incompatible types for operation; '{type(self).__name__}' - '{type(other).__name__}'")
    
    def __mul__(self, other : float) -> "Point":
        if isinstance(other, (float, int)):
            return Point(self.x*other, self.y*other)
        else:
            raise TypeError(f"incompatible types for operation; '{type(self).__name__}' * '{type(other).__name__}'")
    
    def __rmul__(self, other : float) -> "Point":
        if isinstance(other, (float, int)):
            return Point(self.x*other, self.y*other)
        else:
            raise TypeError(f"incompatible types for operation; '{type(other).__name__}' * '{type(self).__name__}'")


    def get_coords(self) -> tuple:
        return (self.x, self.y)
    
    def set_coords(self, coords : tuple[float, float]) -> None:
        self.x = coords[0]
        self.y = coords[1]
    
    def distance(self, other : Type["Point"] | None = None) -> float:
        if other is None:
            return math.sqrt(self.x**2 + self.y**2)
        
        else:
            return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
        
    def translate(self, x : float, y : float) -> None:
        pass

    def translate(self, vec : tuple[float, float]) -> None:
        pass


class Line:
    
    def __init__(self, start : Point, end : Point) -> None:
        self.start = start
        self.end = end

    @property
    def start(self) -> Point:
        return self.__start
    
    @property
    def end(self) -> Point:
        return self.__end
    
    @start.setter
    def start(self, start : Point) -> None:
        if not isinstance(start, Point):
            raise TypeError(f"'start' is of type")


class FreeShape:
    pass


class Polygon(FreeShape):
    pass


class Rectangle(FreeShape):
    pass


class Square(Rectangle):
    pass


class Ellipse(FreeShape):
    pass


class Circle(Ellipse):
    pass