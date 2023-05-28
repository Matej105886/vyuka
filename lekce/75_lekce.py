# vysky = {}
# vysky["Pepa"] = 180
# vysky["Jirka"] = 175
# print(vysky["Jirka"])
# # vysky.pop("Pepa")
# print(vysky.values())
# print(vysky.keys())
# print(vysky.items())

class Databaze_vysek:
    def __init__(self):
        self.vysky = {}

    def pridej_vysku(self, jmeno, vyska):
        if jmeno in self.vysky.keys():
            raise Exception("Toto jmeno uz existuje")
        self.vysky[jmeno] = vyska

    def vrat_vysku(self, jmeno):
        try:
            return self.vysky[jmeno]
        except KeyError:
            return 0

    def vrat_prumernou_vysku_vsech(self):
        vysky_dohromady = 0
        for vyska in self.vysky.values():
            vysky_dohromady += vyska
        return vysky_dohromady / len(self.vysky.values())

    def odstran(self, jmeno):
        self.vysky.pop(jmeno)

    def zmen_vysku(self, jmeno, nova_vyska):
        self.odstran(jmeno)
        self.pridej_vysku(jmeno, nova_vyska)

    def vypis_databazi(self):
        for item in self.vysky.items():
            print(item[0] + " ma vysku " + str(item[1]) + " cm")

    def restartuj_databazi(self):
        self.vysky.clear()

    def zvys_vysku(self, o_kolik):
        vysky_key = self.vysky.keys()
        vysky_key_list = []
        for key in vysky_key:
            vysky_key_list.append(key)
        for clovek in vysky_key_list:
            nova_vyska = self.vrat_vysku(clovek) + o_kolik
            self.zmen_vysku(clovek, nova_vyska)



databaze = Databaze_vysek()
databaze.pridej_vysku("Pavel", 185)
databaze.pridej_vysku("Pepa", 65)
databaze.zmen_vysku("Pavel", 175)
print(databaze.vrat_vysku("Pavel"))
# print(databaze.vrat_prumernou_vysku_vsech())
databaze.zvys_vysku(20)
print(databaze.vrat_vysku("Pavel"))
databaze.vypis_databazi()
databaze.restartuj_databazi()