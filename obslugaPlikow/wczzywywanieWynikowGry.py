import pickle

def odczytaj_plik(nazwa_pliku):
    try:
        with open(nazwa_pliku, "rb") as plik:
            dane = pickle.load(plik)
            return dane
    except IOError as e:
        print("Wystąpił błąd podczas wczytywania pliku.", e)
        return None

nazwa_pliku = "wynikiGry.dat"
wyniki = odczytaj_plik(nazwa_pliku)

if wyniki:
    print("Odczytane dane z pliku:", wyniki)
else:
    print("Nie udało się odczytać daanych z pliku.")


