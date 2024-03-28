import sys

def open_file(file_name, mode):
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Nie można otworzyć pliku", file_name ,"Program zostanie zakończony\n")
        input("\nAby zakończyć program wciśnij klawisz Enter.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Zwróć kolejny wiersz pliku quiz po sformatowaniu go"""
    line = the_file.readline()
    line = line.replace("/","\n")
    return line

def next_block(the_file):
    """Zwróc kolejny blok danych z pliku quiz"""
    category = next_line(the_file)
    question = next_line(the_file)

    answers = []
    for i in range(4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    point = next_line(the_file)

    explanation = next_line(the_file)

    return category, question, answers, correct, point, explanation

def welcome(title):
    print("\t\tWitaj w turnieju wiedzy.")
    print("\t\t", title,"\n")

def nalepsze_wyniki(score):
    import wczzywywanieWynikowGry

    _score = score
    scores = []
    choice = None

    while choice != "0":
        print(
            """
            Najlepsze wyniki:
            0 - zakończ
            1 - wyświetl wyniki
            2 - dodaj wynik
            """
        )

        choice = input("Wybierz co chcesz zrobic: ")

        if choice == "0":
            print("Do widzenia.")
        elif choice == "1":
            scores = wczzywywanieWynikowGry.odczytaj_plik("wynikiGry.dat")
            print("Najlepsze wyniki: ")
            print("GRACZ:\tWYNIK:")
            for entry in scores:
                name, score = entry
                print(name, "\t", score)
        elif choice == "2":
            name = input("Dodaj nazwę gracza: ")
            score = _score
            entry = (name, score)
            scores.append(entry)
            scores.sort(reverse=True)
            scores = scores[:5]
            marynowanie(scores)
        else:
            print("Niestety", choice, "nie jest prawidłowym wyborem.")
    return scores

#marynowanie

def marynowanie(scores):
    import pickle, shelve

    try:
        with open("wynikiGry.dat", "ab") as f:
            pickle.dump(scores, f)
    except IOError as e:
        print("Wystapił błąd podczas zapisywania wyników gry do pliku.")


def main():
    trivia_file = open_file("quiz.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0


    category, question, answers, correct, point, explanation = next_block(trivia_file)

    while category:
        print(category)
        print(question)

        for i in range(4):
            print("\t", i + 1, "-", answers[i], end="")

        answer = input("Jaka jest twoja odpowiedź: ")

        if answer == correct:
            print("Odpowiedź prawidłowa!", end=" ")
            score += int(point)

        else:
            print("Odpowiedź niepoprawna.", end=" ")
        print(explanation)
        print("Wynik: ", score, "\n\n")

        category, question, answers, correct, point, explanation = next_block(trivia_file)

    trivia_file.close()
    print("To było ostatnie pytanie.")
    print("Twój wynik końcowy wynosi: ", score)



    nalepsze_wyniki(score)
#    marynowanie(wynik)

    print("Zostało zamarynowane")

main()
input("Wciśnij ENTER aby zakończyć.")
