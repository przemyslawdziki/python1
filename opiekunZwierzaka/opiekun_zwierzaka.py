class Critter(object):
    """Wirtualny pupil"""

    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom
        self.rep = ""

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unheppines = self.hunger + self.boredom

        if unheppines < 5:
            m = "szczęśliwy"
        elif unheppines <= 10:
            m = "zadowolony"
        elif unheppines <= 15:
            m = "podenerwowany"
        else:
            m = "wściekły"
        return m

    def talk(self):
        print("Nazywam się", self.name, "i jestem", self.mood, "teraz.\n")
        self.__pass_time()

    def eat(self, food = 4):
        print("mniam, mniam. Dziękuję.")
        self.hunger -= food

        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("Hura.")
        self.boredom -= fun

        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    def __str__(self):
        rep = ""
        self.rep += "Moje imię to " + self.name + "\n"
        self.rep += "Poziom znudzenia to " + str(self.boredom) + "\n"
        self.rep += "Poziom głodu to " + str(self.hunger) + "\n"
        self.rep += "Obecnie jestem " + self.mood + "\n"
        return self.rep

def main():
    crit_name = input("Jak chcesz nazwać swojego zwierzaka?: ")
    crit = Critter(crit_name)

    choice = None

    while choice != "0":
        print("""
        Opiekun zwierzaka
        0 - zakończ 
        1 - słucchaj swojego zwierzaka
        2 - nakarm swojego zwierzaka
        3 - pobaw się ze swoi zwierzakiem
        """)

        choice = input("Wybierz: ")

        if choice == "0":
            print("Do widzenia.")
            break
        elif choice == "1":
            crit.talk()
        elif choice == "2":
            food = int(input("Ile jedzenia chcesz podać zwierzakowi: "))
            crit.eat(food)
        elif choice == "3":
            fun = int(input("jak długo cchcesz się bawić ze zwierzakiem: "))
            crit.play(fun)
        elif choice == "4":
            print(crit)

        else:
            print("Niestety, ", choice, "nie jest prawidłowym wyborem.")

main()

input("Wciśnij ENTER aby zakończyć")
