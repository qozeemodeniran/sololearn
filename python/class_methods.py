class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    # class method: Class methods are different - they are called by a class, which is passed to the cls parameter of the method.A common use of these are factory methods, which instantiate an instance of a class, using different parameters than those usually passed to the class constructor.
    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)

square = Rectangle.new_square(5)

print(square.calculate_area())