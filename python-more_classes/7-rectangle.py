class Rectangle:
    # Public class attributes
    number_of_instances = 0
    print_symbol = "#"

    # Initialization of instance
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    # Getter for width
    @property
    def width(self):
        return self.__width

    # Setter for width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # Getter for height
    @property
    def height(self):
        return self.__height

    # Setter for height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    # Method to calculate area of the rectangle
    def area(self):
        return self.__width * self.__height

    # Method to calculate perimeter of the rectangle
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    # String representation of the rectangle using the print_symbol
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_str = []
        for _ in range(self.__height):
            rect_str.append(str(self.print_symbol) * self.__width)
        return "\n".join(rect_str)

    # repr() method to return a string that can recreate the object
    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    # Destructor to handle instance deletion
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
