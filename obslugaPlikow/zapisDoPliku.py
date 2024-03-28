#odczyt

print("Odczyt i zamkniecie pliku.")
text_file = open("odczyt.txt", "r")
text_file.close()

print("Odczyt znaków z pliku.")
text_file = open("odczyt.txt", "r")
print(text_file.read(1))
print(text_file.read(7))
text_file.close()

print("Odczyt całego pliku za jednym razem.")
text_file = open("odczyt.txt", "r")
whole_thiing = text_file.read()
print(whole_thiing)
text_file.close()

print("Odczytywanie po jednym wierszu na raz.")
text_file = open("odczyt.txt", "r")
print(text_file.read())
print(text_file.read())
print(text_file.read())
text_file.close()


print("wczzytywanie pliku do listy.")
text_file = open("odczyt.txt", "r")
lines = text_file.readlines()
print(lines)
for line in lines:
    print(line)
text_file.close()

print("ponieranie zawartosci pliku wiersz po wierszu.")
text_file = open("odczyt.txtx", "r")
for line in text_file:
    print(line)
text_file.close()

#zapis do pliku

print("utworzenie pliku textowego")
text_file = open("zapis.txt", "w")
text_file.write("Wiersz 1\n")
text_file.write("To jest wiersz 2\n")
text_file.write("Ten tekst tworzy wiersz 3\n")
text_file.close()



