class square:
    def __init__ (self, lengthOfSide, color):
        self.lengthOfSide = lengthOfSide
        self.color = color

    def __repr__(self):
        s = (self.lengthOfSide)
        return s

    def getArea(self):
        area = int(self.lengthOfSide)*2
        return area

    def getPerimeter(self):
        perimeter = int(self.lengthOfSide)*4
        return perimeter

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color