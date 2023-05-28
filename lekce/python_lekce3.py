import random

class Zelenina:

    def __init__(self, nazev, hmotnost):
        self.nazev = nazev
        self.hmotnost = hmotnost

    def vypis_informace(self):
        print("zelenina " + self.nazev + " ma hmotnost:" + str(self.hmotnost))


class Ovoce:

    def __init__(self, nazev, hmotnost):
        self.nazev = nazev
        self.hmotnost = hmotnost

    def vypis_informace(self):
        print("ovoce " + self.nazev + " ma hmotnost:" + str(self.hmotnost))


class Generator:

    def vygeneruj_ovoce_nebo_zeleninu(self):
        volba_zelenina_nebo_ovoce = random.randint(1, 2)
        list_ovoce = [("jablko", 15), ("mandarinka", 10), ("broskev", 20)]
        list_zelenina = [("mrkev", 13), ("okurka", 22), ("paprika", 19), ("salat", 21)]
        if volba_zelenina_nebo_ovoce == 1:
            volba_jidla = random.choice(list_ovoce)
            ovoce = Ovoce(volba_jidla[0], volba_jidla[1])
            return ovoce
        else:
            volba_jidla = random.choice(list_zelenina)
            zelenina = Zelenina(volba_jidla[0], volba_jidla[1])
            return zelenina

    def vygeneruj_nekolik_ovoci_nebo_zelenin(self, pocet):
        list_jidel = []
        for i in range(pocet):
            jidlo = self.vygeneruj_ovoce_nebo_zeleninu()
            list_jidel.append(jidlo)
        return list_jidel



generator = Generator()



list_jidel = generator.vygeneruj_nekolik_ovoci_nebo_zelenin(9)


for i in range(len(list_jidel)):
        print(i + 1, end= ": ")
        list_jidel[i].vypis_informace()

celkova_hmotnost_zeleniny = 0
celkova_hmotnost_ovoce = 0
for jidlo in list_jidel:
    if type(jidlo) == Ovoce:
        celkova_hmotnost_ovoce += jidlo.hmotnost
    else:
        celkova_hmotnost_zeleniny += jidlo.hmotnost

pocet_ovoce = 0
pocet_zeleniny = 0
for jidlo in list_jidel:
    if type(jidlo) == Ovoce:
        pocet_ovoce += 1
    else:
        pocet_zeleniny += 1
if pocet_ovoce > pocet_zeleniny:
    ovoce_ke_smazani = pocet_ovoce - pocet_zeleniny
    print("bude mazano "+ str(ovoce_ke_smazani) + " ovoci")
    for i in range(ovoce_ke_smazani):
        if ovoce_ke_smazani > 0:
            if type(list_jidel[i]) == Ovoce:
                list_jidel.remove(list_jidel[i])
                ovoce_ke_smazani -= 1
elif pocet_ovoce < pocet_zeleniny:
    zelenina_ke_smazani = pocet_zeleniny - pocet_ovoce
    print("bude mazano " + str(zelenina_ke_smazani) + " zelenin")
    for i in range(zelenina_ke_smazani):
        if zelenina_ke_smazani > 0:
            if type(list_jidel[i]) == Zelenina:
                list_jidel.remove(list_jidel[i])
                zelenina_ke_smazani -= 1
print("jidla po mazani:")
for i in range(len(list_jidel)):
        print(i + 1, end= ": ")
        list_jidel[i].vypis_informace()

print(celkova_hmotnost_zeleniny)
print(celkova_hmotnost_ovoce)


