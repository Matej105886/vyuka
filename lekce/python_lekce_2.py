class Zoo:
    def __init__(self):
        self.zvirata = []

    def pirdej_zvire(self, zvire):
        if type(zvire) == Tygr:
            return
        self.zvirata.append(zvire)


    def vypis_vsechny_zvirata(self):
        for zvire in self.zvirata:
            print(type(zvire))

    def vrat_hmotnost_potravy_vsech_zvirat(self):
        soucet = 0
        for zvire in self.zvirata:
            soucet += zvire.potrava
        return soucet



class Zvire:
    def __init__(self, hmotnost_potrava):
        self.potrava = hmotnost_potrava


class Slon(Zvire):
    def __init__(self):
        Zvire.__init__(self,100)


class Zirafa(Zvire):
    def __init__(self):
        Zvire.__init__(self,80)


class Tygr(Zvire):
    def __init__(self):
        Zvire.__init__(self,20)


slon1 = Slon()
slon2 = Slon()
zirafa1 = Zirafa()
tygr1 = Tygr()
zoo = Zoo()
zoo.pirdej_zvire(slon1)
zoo.pirdej_zvire(slon2)
zoo.pirdej_zvire(zirafa1)
zoo.pirdej_zvire(tygr1)
zoo.vypis_vsechny_zvirata()
slon1.potrava = 150
print(zoo.vrat_hmotnost_potravy_vsech_zvirat())