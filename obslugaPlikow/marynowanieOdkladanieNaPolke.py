#marynowanie i odkłdanie na półkę

import pickle, shelve
#zapisywane do pliku

print("Marynowanie list")

varienty = ["łagodny", "pikantny", "kwaszony"]
shape = ["cały", "krojone wzdłuż", "w plasterkach"]
brand = ["Bawtona", "Klimex", "Vortumnus"]

f = open("pickle1.dat", "wb")

pickle.dump(varienty, f)
pickle.dump(shape, f)
pickle.dump(brand, f)

f.close()

#odkladaie pliku na półkę

print("Odkładanie pliku na półkę")
#najpierw tworzymy półkę

s = shelve.open("pickle2.dat")

s["odmiana"] = ["łagodny", "pikantny", "kwaszony"]
s["kształt"] = ["cały", "krojone wzdłuż", "w plasterkach"]
s["marka"] = ["Bawtona", "Klimex", "Vortumnus"]

s.sync() #upewnij się, że dane zostały zapisane

#poieranie listy z pliku półki

print("marka - ", s["marka"])
print("kształt - ", s["kształt"] )
print("odmiana - ", s["odmiana"])
s.close()

input("Klepnij Enter aby zakończyć!!!")

#odczytywanie z pliku
#load(plik)



