

#tworzenie listy
inventory = ["miecz", "zbroja", "tarcza", "napój uzdrawiający"]

for item in inventory:
    print(item)

#długość listy
print("Twój dobytek zawiera ",len(inventory), "elementy(ów).")

#sprawdzanie czy element jest na liscie
if "napój uzdrawiający" in inventory:
    print("Dożyjesz dnia, w którym stoczysz walkę")


#wyświetlanie elementu wskazanego przez indeks
index = int(input("Wprowadź indeks elementu inwentarza: "))
print("Pod indeksem", index, "znajduje się", inventory[index])

#wyccinki list
start = int(input("Wprowdź indeks wyznaczający początek wycinka: "))
finish = int(input("Wprowadź indeks wyznaczający koniec wycinka: "))
print("inventory[",start,":",finish,"] to", end=" ")
print(inventory[start:finish])

#konkatenacja list
chest = ["złoto", "dolary"]
print("Znajduujesz skrzynie, która zawiera")
print(chest)
print("pakujesz zawartość do inwentaarza.")
inventory += chest
print("Twój aktualny inwentarz to: ")
print(inventory)

#mutowalność lisy czyli zmienność
#przypisanie przez indeks
print("wymiana miecza na kuszę")
inventory[0] = "kusza"
print("Twój aktualny inwentarz to: ")
print(inventory)

#dodawanie nowej wartosci do listy
print("wydajesz złoto i dolary na rozkosze cielesne.")
inventory[4:6] = ["kula do wróżenia"]
print("twój inwentarz to:")
print(inventory)

#usuwanie element
print("W bitwie twoja tarcza zostaje zniszczona.")
del inventory[2]
print("Twój inwentarz to :")
print(inventory)

#usuwaie wycnka z listy
print("Twoja kusza i zbbroa zostały skradzione")
del inventory[:2]
print("Twój inwentadrz to: ")
print(inventory)


input("Wciśnij Enter aby zakończyć.")