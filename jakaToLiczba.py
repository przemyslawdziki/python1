# Zmodyfikuj program Jaka to liczba? tak, aby gracz dysponował ograniczoną
# liczbą prób odgadnięcia wybranej przez komputer liczby. Gdy graczowi nie uda
# się odgadnąć tej liczby w wyznaczonej liczbie prób, program powinien
# wyświetlić odpowiedni komunikat z reprymendą.


def jakaToLiczba():
    import random

    liczba_prob = 7
    rand = random.randint(0, 1000)

    print("Zgadnij jaką liczbę wylosowałem:")

    while liczba_prob > 0:
        choice = int(input("Podaj swoją liczbę: "))
        #print(rand)

        if(rand > choice):
            print("Twoja liczba jest za mała.")
        elif(rand < choice):
            print("Twoja liczba jest za duża.")
        elif(rand == choice):
            print("Gratulacje wygrałeś!!!")
            break
        liczba_prob -= 1


        if(liczba_prob == 0):
            print("Skończyły się Ci życia. \nPostaraj się bardziej następnym razem!!!")






jakaToLiczba()