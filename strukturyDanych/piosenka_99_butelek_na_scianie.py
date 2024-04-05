def bootles_of_beer(bob):
    """ Wyświetla słowa piosenki
        99 butelek piwa na ścianie.
        :param bob: Musi być liczbą
        dodatnią.
    """
    if bob < 1:
        print("""Nie ma już butelek
                 piwa na ścianie
                 Nie ma już butelek piwa""")
        return
    tmp = bob
    bob -= 1
    print("""{} butele piwa na ścianie.
             {} butele piwa. Jedną weź
             i przekaż w koło. {} butek
             piwa na ścianie.
          """.format(tmp, tmp, bob))
    bootles_of_beer(bob)

bootles_of_beer(99)