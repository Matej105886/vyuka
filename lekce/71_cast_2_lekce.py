class Kniha:
    def __init__(self, autor, nazev, pocet_stran):
        self.autor = autor
        self.nazev = nazev
        self.pocet_stran = pocet_stran

    def vypis_knizky(self):
        print("Kniha se jmenuje " + self.nazev + " ma autora "  + self.autor + " a ma " + str(self.pocet_stran) + " pocet stran")


class Knihovna:
    def __init__(self):
        self.knihy = []

    def pridej_knihu(self, autor, nazev, pocet_stran):
        kniha = Kniha(autor, nazev, pocet_stran)
        self.knihy.append(kniha)
        print("kniha byla pridana")
        kniha.vypis_knizky()

    def vypis_knihovny(self):
        if len(self.knihy) >= 1:
            print("v knihovne je " + str(len(self.knihy)) + " knih:")
            for kniha in self.knihy:
                kniha.vypis_knizky()
        else:
            print("v knihovne nejsou knihy")


knihovna = Knihovna()
# knihovna.pridej_knihu("Alois", "stare povesti ceske", 220)
# knihovna.pridej_knihu("Alios", "lucerna", 136)
knihovna.vypis_knihovny()