import random
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
        self.mnozstvi_krmeni = 100

    def nakup_zvire(self, obchod):
        list_zvirat = obchod.list_zvirat_na_prodej
        if self.max_pocet_zvirat == len(self.list_zvirat):
            print("vase kapacita zvirat je plna")
            return
        obchod.vypis_informace_o_zviratech_na_prodej()
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

    def nakup_krmeni(self, mnozstvi):
        mnozstvi_cena_1ks = 100
        mnozstvi_cena = mnozstvi*mnozstvi_cena_1ks
        if self.penize > mnozstvi_cena:
            self.mnozstvi_krmeni += mnozstvi
            self.penize -= mnozstvi_cena
            print("koupili jste " + str(mnozstvi) + " kg krmiva")
        else:
            print("Nemate dostatek penez")

    def vypis_informace_o_zoo(self):
        print("zoo ma " + str(self.mnozstvi_krmeni) + " kg krmiva a " + self.penize + "kc")
        print("maximalni pocet zvirat je " + str(self.max_pocet_zvirat) + " a zoo ma " + str(len(self.list_zvirat)) + " zvirat, a vlastni zvirata:")
        for zvire in self.list_zvirat:
            zvire.vypis_inf_o_zvireti()

    def vygeneruj_pocet_penez_zoo(self):
        pocet_penez = random.randint(0, 500000)
        self.penize += pocet_penez
        print("zoo si vydelala " + str(pocet_penez) + "kc a ma dohromady " + str(self.penize) + "kc")

    def nakrm_vsechna_zvirata(self):
        dohromady_sni = 0
        for zvire in self.list_zvirat:
            dohromady_sni += zvire.davka_jidla
        if self.mnozstvi_krmeni >= dohromady_sni:
            self.mnozstvi_krmeni -= dohromady_sni
            print("zvirata snedli " + str(dohromady_sni) + "kg krmeni a zbylo zoo " + str(self.mnozstvi_krmeni) + "kg krmeni")
            return True
        else:
            print("nemate dostatek jidla")
            return False

    def zvets_maximalni_pocet_zvirat(self, o_pocet_zvirat):

        cena_1ks = 1000000
        cena = o_pocet_zvirat*cena_1ks
        if self.penize >= cena:
            self.penize -= cena
            self.max_pocet_zvirat += o_pocet_zvirat
            print("max pocet zvirat je " + str(self.max_pocet_zvirat) + " a zoo ma " + str(self.penize) + "kc")
        else:
            print("nemate dostatek penez pro zvetseni")

class Obchod_se_zviraty:
    def __init__(self):
        slon1 = Slon("Bimbo")
        zirafa1 = Zirafa("Eva")
        lev1 = Lev("Ferdo")
        self.list_zvirat_na_prodej = [(slon1, 1000000), (zirafa1, 800000), (lev1, 500000)]

    def vygeneruj_nahodne_zvire(self):
        cislo_u_jmena =random.randint(1000, 10000)
        generator_ceny = random.randint(500000, 1200000)
        zvire_generator = random.randint(1,4)
        if zvire_generator == 1:
            zvire = Slon("slon" + str(cislo_u_jmena))
            self.list_zvirat_na_prodej.append((zvire, generator_ceny))
        elif zvire_generator == 2:
            zvire = Zirafa("zirafa" + str(cislo_u_jmena))
            self.list_zvirat_na_prodej.append((zvire, generator_ceny))
        else:
            zvire = Lev("lev" + str(cislo_u_jmena))
            self.list_zvirat_na_prodej.append((zvire, generator_ceny))

    def vypis_informace_o_zviratech_na_prodej(self):
        for informace in self.list_zvirat_na_prodej:
            informace[0].vypis_inf_o_zvireti()
            print("Toto zvire stoji: " + str(informace[1]) + " Kc")





obchod_se_zviraty = Obchod_se_zviraty()
zoo = Zoo(3000000, 2)

obchod_se_zviraty.vypis_informace_o_zviratech_na_prodej()
obchod_se_zviraty.vygeneruj_nahodne_zvire()
print("-----------------------------------------")
obchod_se_zviraty.vypis_informace_o_zviratech_na_prodej()
