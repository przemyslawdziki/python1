class Rectangle():
    recs = []

    def __init__(self, w, l):
        self.length = l
        self.width = w
        self.recs.append((self.width, self.length))

    def print_size(self):
        print("""{} na {}
              """.format(self.width,
                           self.length))

r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)

print(Rectangle.recs)