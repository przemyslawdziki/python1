def najlepszewynikiLista():
    scores = []
    choice = None

    while choice != "0":
        print(
            """Najlepsze wyniki:
            0 - zakończ
            1 - pokaz wyniki
            2 - dodaj wynik
            3 - usuń wynik
            4 - posortuj wyniki
            """
        )

        choice = input("Wybierz : ")
        print()

        if choice == "0":
            print("Do widzenia")
            break
        elif choice == "1":
            print("Najlepsze wyniki: ")
            for score in scores:
                print(score)
        elif choice == "2":
            score = int(input("Jaki wynik uzyskałeś: "))
            scores.append(score)
        elif choice == "3":
            score = int(input("Który wynik usunąć?: "))
            if score in scores:
                scores.remove(score)
            else:
                print(score, "nie ma na liście wyników!")
        elif choice == "4":
            scores.sort(reverse=True)
        else:
            print("Niestety,", choice, "nie jest prawidłowym wyborem.")

    input("Aby zakończyć wciśnij Enter")

def nalepszewynikiKrotki():

   scores = []

   choice = None

   while choice != "0":
       print(
           """
           Najlepsze wyniki krotki
           0 - zakończ
           1 - wyświetl wyniki
           2 - dodaj wynik
           """)

       choice = input("Wybierz: ")

       if choice == "0":
           print("Do widzenia")
           break
       elif choice == "1":
           print("Najlepsze wyniki:")
           print("GRACZ\tWYNIK")
           for entry in scores:
               name, score = entry
               print(name, "\t", score)
       elif choice == "2":
           name = input("Podaj nazwę graacza: ")
           score = input("Jaki wynik uzyskał gracz: ")
           entry = (name, score)
           scores.append(entry)
           scores.sort(reverse=True)
           scores= scores[:5]
       else:
           print("Niestety",choice,"nie jest prawidłowym wyborem.")





#input("Aby zakończyć wciśnij Enter")



nalepszewynikiKrotki()