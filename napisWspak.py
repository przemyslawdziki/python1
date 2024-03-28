# Utwórz program, który wczytuje komunikat użytkownika, a następnie wypisuje
# go w odwrotnej kolejności.

def odwrocNapis():
    napis = input("Podaj napis do odwrocenia: ")

    for i in range(len(napis) - 1, -1, -1):
        print(napis[i], end="")


odwrocNapis()