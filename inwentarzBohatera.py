#inwenatarz bohatera

#tworzenie krotki
inventory = ()

if not inventory:
    print("Nie posiadarz niczego")

input("\nAby kontynuować naciśnij Enter")

inventory = ("miecz",
             "zbroja",
             "tacza",
             "napój uzdrawiający")

print("Wykaz inwentarza:")
print(inventory)


print("\nElementy inwentarza: ")
for item in inventory:
    print(item)

#indeksowanie krotek
indeks = int(input("Wprowadz numer indeksu inwentarza: "))
print("Pod indeksem", indeks, "znajduje się", inventory[indeks])

#wycinanie krotek

start = int(input("Wprowdź indeks wyznaczający początek wycinka: "))
finish = int(input("Wprowdż indesk wyznaczający koniec wycinka: "))
print("inventory[",start,":",finish,"] to", end=" ")
print(inventory[start:finish])

#konkatenacja krotek
chest = ("złoto", "dolary")
print("znajduujesz skrzynię, która zawiera: ")
print("Tajemnica wiary!!!")
print(chest)
print("Dodajesz zawartośc skrzyni do swojego inwenatarza.")
inventory += chest
print("Twój aktualny inwentaarz to: ")
print(inventory)

