class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return 'Rectangle(width={w}, height={h})'.format(w = self.width, h = self.height)

    def set_width(self, width):
        if type(width) is int or float:
            self.width = width

    def set_height(self, height):
        if type(height) is int or float:
            self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)

    def get_picture(self):
        cadena = ''

        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'

        for i in range(self.height):
            cadena += '{:*<{w}}\n'.format('', w = self.width)
        
        return cadena

    def get_amount_inside(self, shape):
        if type(shape) is Rectangle or Square:
            if (self.width >= shape.width) and (self.height >= shape.height):
                nWidth = self.width // shape.width
                nHeight = self.height // shape.height
                return nWidth * nHeight
            else:
                return 0
        else:
            return 0



class Square(Rectangle):

    def __init__(self, side):
        Rectangle.__init__(self, side, side)
        self.side = side

    def __str__(self):
        return 'Square(side={s})'.format(s = self.side)

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

