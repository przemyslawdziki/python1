#współdziałanie obiektów

class Player(object):
    def blast(self, enemy):
        print("Gracz razi wroga")
        enemy.die()

class Alien(object):
    def die(self):
        print("obcy umiera")


hero = Player()
invader = Alien()
hero.blast(invader)