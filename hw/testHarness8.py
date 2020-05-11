from hw8 import square

def printSquare(k):
    k.getSquare

def main():
    square1 = square("8", "blue")
    print("The side length of the square is:", square1)

    square1.getArea()
    print("The area of square is:", square1.getArea())

    square1.getPerimeter()
    print("The perimeter of square is:", square1.getPerimeter())

    square1.setColor("red")
    print("The new color of square is:", square1.getColor())

    print("I am a", square1.getColor(), "square with a side length of", square1)




if __name__ == "__main__":
    main()