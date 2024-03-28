# Tym razem trudniejsze wyzwanie. Napisz pseudokod do programu, w którym
# gracz i komputer zamienią się rolami w grze z odgadywaniem liczby. To znaczy
# gracz wybiera losowo liczbę z przedziału od 1 do 100, a komputer ma ją
# odgadnąć. Zanim rozpoczniesz tworzenie algorytmu, pomyśl, w jaki sposób
# sam byś zgadywał. Jeśli wszystko się uda, spróbuj napisać kod gry.


def kompZgadujeLiczbe():
    dolna_granica = 1
    gorna_granica = 100
    proba = 0

    while True:
        proba += 1
        kompChoice = (gorna_granica + dolna_granica) // 2
        print("Moja liczba to %i" % kompChoice)
        guess = input("Czy to twoja liczba? (t/mniejsza/wieksza): ")

        if guess == 't':
            print("Hura, wygrałem w %d próbach!!!" % proba)
            break
        elif guess == 'mniejsza':
            gorna_granica = kompChoice - 1
        elif guess == 'wieksza':
            dolna_granica = kompChoice + 1
        else:
            print("Niepoprawna odpowiedź. Podaj 't' jeśli zgadłem lub 'mniejsza'/'wieksza' jeśli nie.")
            continue


kompZgadujeLiczbe()
