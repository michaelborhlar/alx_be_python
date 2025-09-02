# oop/polymorphism_demo.py

import math

class Shape:
    """Base class for all shapes"""

    def area(self):
        """Placeholder method to be overridden by subclasses"""
        raise NotImplementedError("Subclasses must implement this method")


class Rectangle(Shape):
    """Rectangle shape, inherits from Shape"""

    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """Return the area of the rectangle"""
        return self.length * self.width


class Circle(Shape):
    """Circle shape, inherits from Shape"""

    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """Return the area of the circle"""
        return math.pi * (self.radius ** 2)
