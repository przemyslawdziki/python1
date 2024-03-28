# Napisz program Kreator postaci do gry z podziałem na role. Gracz powinien
# otrzymać pulę 30 punktów, którą może spożytkować na cztery atrybuty: siła,
# zdrowie, mądrość i zręczność. Gracz powinien mieć możliwość przeznaczania
# punktów z puli na dowolny atrybut, jak również możliwość odbierania
# punktów przypisanych do atrybutu i przekazywania ich z powrotem do puli.

class Hero():

    def __init__(self):
        self.punktyDoPodzialu = 30
        self.sila = 0
        self.zdrowie = 0
        self.madrosc = 0
        self.zrecznosc = 0

    def dodajPunkty(self, atrybut = 'sila', ilosc = 0):

        if(self.punktyDoPodzialu >= ilosc):
            if(atrybut == 'sila'):
                self.sila += ilosc
            elif(atrybut == 'zdrowie'):
                self.zdrowie += ilosc
            elif(atrybut == 'madrosc'):
                self.madrosc += ilosc
            elif(atrybut == 'zrecznosc'):
                self.zrecznosc += ilosc
            self.punktyDoPodzialu -= ilosc
        else:
            print("Nie masz wystarczającej ilości puktów.")

    def odejmijPunkty(self, atrybut, ilosc):
        if(atrybut == 'sila'):
            if(self.sila >= ilosc):
                self.sila -= ilosc
                self.punktyDoPodzialu += ilosc
            else:
                print("Nie masz wystarczajcej ilosc punktów w tym atrybucie.")

        elif(atrybut == 'zdrowie'):
            if(self.zdrowie >= ilosc):
                self.zdrowie -= ilosc
                self.punktyDoPodzialu += ilosc
            else:
                print("Nie masz wystaczającej ilości punktów w tym atrybucie.")

        elif(atrybut == 'zrecznosc'):
            if(self.zrecznosc >= ilosc):
                self.zrecznosc -= ilosc
                self.punktyDoPodzialu += ilosc
            else:
                print("nie masz wystarczającej ilosci punktów w tym atrybucie.")

        # elif(atrybut == 'dupa'):
        #     self.sila += ilosc
        #     self.zdrowie += ilosc
        #     self.zrecznosc += ilosc
        #     self.madrosc += ilosc

    def info(self):
        print(f"Siła: {self.sila}")
        print(f"Zdrowie: {self.zdrowie}")
        print(f"Mądrość: {self.madrosc}")
        print(f"Zręczność: {self.zrecznosc}")
        print(f"Punkty do podziału: {self.punktyDoPodzialu}")

    def nameOfValue(self):
        response = input("Jaki atrybut chcesz zwiększyć: ")
        return response

    def valueOfQuantity(self):
        resource = int(input("O jaką wartośc chesz zwiększyć atrybut: "))
        return resource
    def tworzeniepostaci(self):

        choice = None
        while choice != "0":
            print(
                """
                Co chcesz uczynić:
                0 - wyjscie
                1 - dodaj punkty
                2 - odejmij punkty
                3 - info
            """
            )

            choice = input("Wybierz: ")

            if (choice == "0"):
                print("Do widzenia")
                break
            elif (choice == "1"):
                atrybut = self.nameOfValue()
                ilosc = self.valueOfQuantity()
                self.dodajPunkty(atrybut, ilosc)
            elif (choice == "2"):
                atrybut = self.nameOfValue()
                ilosc = self.valueOfQuantity()
                self.odejmijPunkty(atrybut, ilosc)
            elif (choice == "3"):
                self.info()




for i in range(10):

    i = Hero()
    i.tworzeniepostaci()
