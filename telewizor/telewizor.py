# Napisz program, który symuluje telewizor, tworząc go jako obiekt. Użytkownik
# powinien mieć możliwość wprowadzenia numeru kanału oraz zwiększenia
# bądź zmniejszenia głośności. Zastosuj mechanizm zapewniający utrzymywanie
# numeru kanału i poziomu głośności we właściwych zakresach

class Telewizor(object):

    @property
    def nrKanal(self):
        return self.__nrKanal

    def set_nrKanal(self, new_nrKanal):
        if 0 <= new_nrKanal <= 100:
            self.__nrKanal = new_nrKanal
        else:
            print("Nieprawidłowy wybór kanału.")

    @property
    def glosnosc(self):
        return self.__glosnosc

    def __init__(self, nrKanal = 0, glosnosc = 0):
        self.set_nrKanal(nrKanal)
        self.__glosnosc = max(0, glosnosc) #nie może być ujemna

    def zwiekszGloscnosc(self, poziom = 1):
        self.__glosnosc += poziom

    def zmniejszGloscnosc(self, poziom = 1):
        self.__glosnosc -= poziom

    def displayparameter(self):
        print("Kanał = ", self.nrKanal)
        print("Poziom głośności = ", self.glosnosc)


def main():
    tv = Telewizor()

    choice = None

    while choice != "0":
        print("""
            Obsluga telewizora
            0 - wyłącz 
            1 - zmień kanał
            2 - zwiększ głośność
            3 - zmniejsz głosność
            4 - sprawdź parametry
            """)

        choice = input("Wybierz: ")

        if choice == "0":
            print("GOODBYE.")
            break
        elif choice == "1":
            nr = int(input("Podaj numer kanału z zakresu od 0 - 100: "))
            tv.set_nrKanal(nr)
        elif choice == "2":
            level = int(input("O ile chcesz zwiększyć głośność: "))
            tv.zwiekszGloscnosc(level)
        elif choice == "3":
            level = int(input("O ile chcesz zmniejszyć głośność: "))
            tv.zmniejszGloscnosc(level)
        elif choice == "4":
            tv.displayparameter()
        else:
            print("Niestety, ", choice, "nie jest prawidłowym wyborem.")


main()

input("Wciśnij ENTER aby zakończyć")
