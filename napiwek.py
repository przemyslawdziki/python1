
def pobierzDane():
    wartoscRachunku = float(input("Wprowadz wartość rachunku klienta: "))

    return wartoscRachunku

def obliczNapiwek():
    napiwek_temp = pobierzDane()

    napiwek15 = napiwek_temp * 0.15
    napiwek20 = napiwek_temp * 0.20


    print(f"Napiwek 15 % wynosi {napiwek15} złotych,\na napiwek 20 % wynosi {napiwek20} złotych")





obliczNapiwek()