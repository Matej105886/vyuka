# import math
# cislo1 = 0
# epsilon = 0.0001
# for i in range(3):
#     cislo1 += 0.2
#
# rovna_se = abs(0.3 - cislo1)  < epsilon
# print(rovna_se)
# print(cislo1)
# print(math.pi)

class Zvire:
    def __init__(self, jmeno, davka_jidla):
        self.jmeno = jmeno
        self.davka_jidla = davka_jidla

    def vypis_inf_o_zvireti(self):
        print(self.jmeno + " sni " + str(self.davka_jidla) + "kg jidla")



class Slon(Zvire):
    def __init__(self, jmeno):
        super().__init__(davka_jidla=100, jmeno=jmeno)

    def vypis_inf_o_zvireti(self):
        print("-----------------")
        print("toto zvire je slon")
        super().vypis_inf_o_zvireti()

class Zirafa(Zvire):
    def __init__(self, jmeno):
        super().__init__(davka_jidla=80, jmeno=jmeno)

    def vypis_inf_o_zvireti(self):
        print("-----------------")
        print("toto zvire je zirafa")
        super().vypis_inf_o_zvireti()

class Lev(Zvire):
    def __init__(self, jmeno):
        super().__init__(davka_jidla=40, jmeno=jmeno)

    def vypis_inf_o_zvireti(self):
        print("-----------------")
        print("toto zvire je lev")
        super().vypis_inf_o_zvireti()


class Zoo:
    def __init__(self, penize, max_pocet_zvirat):
        self.penize = penize
        self.max_pocet_zvirat = max_pocet_zvirat
        self.list_zvirat = []

    def nakup_zvire(self, list_zvirat):
        if self.max_pocet_zvirat == len(self.list_zvirat):
            print("vase kapacita zvirat je plna")
            return
        for informace in list_zvirat:
            informace[0].vypis_inf_o_zvireti()
            print("Toto zvire stoji: " + str(informace[1]) + " Kc")
        volba = input("Zadej jmeno zvire, ktere chses koupit: ")
        for zvire in list_zvirat:
            if volba == zvire[0].jmeno:
                if self.penize >= zvire[1]:
                    self.list_zvirat.append(zvire[0])
                    list_zvirat.remove(zvire)
                    self.penize -= zvire[1]
                    print("zvire " + zvire[0].jmeno + " je vase.")
                    return
                else:
                    print("nemate dost penez na toto zvire")
                    return
        print("toto zvire v prodeji neni")


class Obchod_se_zviraty:
    def __init__(self):
        slon1 = Slon("Bimbo")
        zirafa1 = Zirafa("Eva")
        lev1 = Lev("Ferdo")
        self.list_zvirat_na_prodej = [(slon1, 1000000), (zirafa1, 800000), (lev1, 500000)]





obchod_se_zviraty = Obchod_se_zviraty()
zoo = Zoo(3000000, 2)

zoo.nakup_zvire(obchod_se_zviraty.list_zvirat_na_prodej)
print(zoo.list_zvirat[0].jmeno)

