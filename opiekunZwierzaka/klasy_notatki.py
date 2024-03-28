class Critter(object):
    """wirtualny pupil"""
    total = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Pusty łańcuch znaków nie może być immieniem zwierzątka.")
        else:
            self.__name = new_name
            print("Zmiana imienia się powiodła.")


    @staticmethod
    def status():
        print("Ogólna liczba zwierzaków wynosi ", Critter.total)

    def __init__(self, name, mood):
        print("urodzł się nowy zwierzak.")
        self.name = name
        self.__mood = mood
        Critter.total += 1

    def __str__(self):
        rep = "Obiekt klasy Critter\n"
        rep += "name: " + self.name + "\n"
        return rep
    def talk(self):
        print("Cześć jestem " + self.name)
        print("W tej chwili czuję się " +self.__mood)

crit = Critter("Ciapek", "chujowo")
crit2 = Critter("Pucek", "zajebiscie")

crit.talk()
crit2.talk()
print(crit2.total)


# for i in range(10):
#     res = "crit" + str(i)
#     res = Critter("c" + str(i))
#     res.talk()
#
# print(Critter.status())