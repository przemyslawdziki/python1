# Napisz program, który liczy za użytkownika. Umożliw użytkownikowi
# wprowadzenie liczby początkowej, liczby końcowej i wielkości odstępu między
# kolejnymi liczbami.


def pobierzDane(m = None ):
    massage = m
    digit = int(input(f'{massage}'))
    return digit

def dodawanie(a, b, c):
    _min = a
    _max = b
    _ods = c
    _sum = 0

    for i in range(_min, _max + 1, _ods):
        _sum += i
    return _sum

def odejmowanie(a, b, c):
    _min = a
    _max = b
    _ods = c
    _sum = 0

    for i in range(_min, _max + 1, _ods):
        _sum -= i
    return _sum

def mnozenie(a, b, c):
    _min = a
    _max = b
    _ods = c
    total = 1

    for i in range(_min, _max + 1, _ods):
        total *= i
    return total

def programLiczacy():
    min = pobierzDane("Podaj dolną grance: ")
    max = pobierzDane("Podaj gorna granice: ")
    odstep = pobierzDane("Podaj odstep między liczzbami: ")

    while True:
        print("Jakie działanie chcesz wykonać: ")
        print("1 - dpdawanie")
        print("2 - odejmowanie")
        print("3 - mnozenie")
        print("9 - wyjscie")

        your_choice = input("wybierz jedno z powyższych: ")
        if(your_choice == '1'):
            dod = dodawanie(min, max, odstep)
            print(dod)
        elif(your_choice == '2'):
            odejm = odejmowanie(min, max, odstep)
            print(odejm)
        elif(your_choice == '3'):
            mno = mnozenie(min, max, odstep)
            print(mno)
        elif(your_choice == '9'):
            break
        else:
            print("Dokonano złego wyboru. Wybiez 1, 2, 3 lub 9.")


programLiczacy()
