# Napisz program, który symuluje ciasteczko z wróżbą. Program powinien
# wyświetlić jedną z pięciu niepowtarzalnych przepowiedni, dokonując losowego
# wyboru przy każdym uruchomieniu.

def ciasteczkaZWrozba():
    import random
    wrozby = ('Co masz zrobić dziś… zrób dziś.',
              'Dzisiaj jest twój dobry dzień.',
              'Nie ma rzeczy niemożliwych.',
              'Nie czekaj, działaj!',
              'UWAGA! Ktoś Cię obserwuje! :)',
              'Zawsze słuchaj swojego ciasteczka.',
              'Szczęście, którego szukasz, jest w drugim ciasteczku :)',
              'Oczekuj na miłą niespodziankę.',
              'Ktoś bardzo cię lubi…',
              'Czeka cię wielka przygoda!',
              'Co tanio wychodzi, drogo wraca.',
              'Nie dziś, nie jutro, może za rok',
              'Teraz pójdzie gładko.',
              'Zaraź kogoś radością.',
              'Miłość to zwycięstwo wyobraźni nad inteligencją.',
              'Kochaj siebie, jak nikt inny.',
              'Czekaj na znak. Lub weź się do dzieła!')

    choice = random.choice(wrozby)

    print(choice)

ciasteczkaZWrozba()





