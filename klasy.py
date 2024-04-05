class Shape():
    def what_am_i(self):
        print("jestem figurą.")

class Rectangle(Shape):
    def __init__(self, height, length):
        self.height = height
        self.length = length

    def calculate_perimeter(self):
        return 2 * self.height + 2 * self.length

class Square(Shape):

    square_list = []
    def __init__(self, bok):
        self.bok = bok
        self.square_list.append(self)
    def calculate_perimeter(self):
        return 4 * self.bok

    def change_size(self, zwiekszenie):
        self.bok += zwiekszenie

    def what_am_i(self):
        super().what_am_i()
        print("jestem kwadratem")

    def __repr__(self):
        print("{} na {} na {} na {}".format(self.bok, self.bok, self.bok,self.bok,self.bok))


rectangle = Rectangle(10, 20)
print("Obwód prostokąta", rectangle.calculate_perimeter())

square = Square(10)
print("obwód kwadratu", square.calculate_perimeter())

square.change_size(90)
print("obwód kwadratu po zwiekszeniu", square.calculate_perimeter())

rectangle.what_am_i()
square.what_am_i()

a = Square(29)
# print(a)

def funkcja(obj1, obj2):
    result = obj1 is obj2
    return result

print(funkcja("a", "a"))




#
# class Horse():
#     def __init__(self, name):
#         self.name = name
#
#
# class Rider():
#     def __init__(self, name, horse):
#         self.name = name
#         self.horse = horse
#
# horse = Horse("Harry")
# rider = Rider("Stanley", horse)
#
# print(rider.horse.name)


