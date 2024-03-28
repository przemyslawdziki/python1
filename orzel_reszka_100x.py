# Napisz program, który „rzuca” 100 razy monetą, a następnie podaje
# użytkownikowi liczbę orzełków i reszek.


def rzuty():
    import random
    orzel = 0
    reszka = 0

    for _ in range(0, 100):
        choice = random.randint(0, 1)
        if(choice == 0):
            reszka += 1
        elif(choice == 1):
            orzel += 1

    print("Orzeł wypadł %s razy\nRszka wypadła %s razy\n" %(orzel, reszka))


rzuty()



