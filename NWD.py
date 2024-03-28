

def nwd():
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))

    if(a > b):
        m =  a
        w = b
    elif(b > a):
        w = b
        m = a
    r = w % m

    while r:
        w = m
        m = r
        r = w % m

    print("NWD liczb %i i %i i wynosi %i, a NWW wynosi %i" % (a, b, m, a*b/m))

nwd()