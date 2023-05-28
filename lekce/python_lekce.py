class Firma:
    def __init__(self, nazev):
        self.nazev = nazev
        self.zamestanci = []
        print("vznikla firma ktera se jmenuje " + self.nazev)

    def prijmi_zamestance(self, zamestanec):
        self.zamestanci.append(zamestanec)
        print("zamestanec " + zamestanec.jmeno + " byl pridan do firmy " + self.nazev)


    def vypis_vsechny_zamestance(self):
        print("   firma " + self.nazev + " ma tyto zamestance:")
        for clovek in self.zamestanci:
            clovek.vypis_zamestance()

    def spoj_firmy(self, druha_firma):
        for zamestanec in druha_firma.zamestanci:
            if zamestanec.profese == "reditel":
                druha_firma.zamestanci.remove(zamestanec)
                break
        nazev_nove_firmy = self.nazev + " " + druha_firma.nazev
        novy_list = self.zamestanci + druha_firma.zamestanci
        nova_firma = Firma(nazev_nove_firmy)
        nova_firma.zamestanci = novy_list
        return nova_firma

    def propust_polovinu_delniku(self):
        pocet_delniku = 0
        for clovek in self.zamestanci:
            if clovek.profese == "delnik":
                pocet_delniku += 1
        pocet_propustenych_delniku = pocet_delniku//2
        nebylo_propusteno_dostatek = True
        while nebylo_propusteno_dostatek:
            for clovek in self.zamestanci:
                if pocet_propustenych_delniku == 0:
                    nebylo_propusteno_dostatek = False
                elif clovek.profese == "delnik":
                    self.zamestanci.remove(clovek)
                    pocet_propustenych_delniku -= 1
                    break


    def propust(self, profese, pomer):
        pocet_zamestancu = 0
        for clovek in self.zamestanci:
            if clovek.profese == profese:
                pocet_zamestancu += 1
        pocet_propustenych_zamestancu = pocet_zamestancu// pomer
        nebylo_propusteno_dostatek = True
        while nebylo_propusteno_dostatek:
            for clovek in self.zamestanci:
                if pocet_propustenych_zamestancu == 0:
                    nebylo_propusteno_dostatek = False
                elif clovek.profese == profese:
                    self.zamestanci.remove(clovek)
                    pocet_propustenych_zamestancu -= 1
                    break


class Zamestanec:
    def __init__(self, jmeno, profese):
        self.jmeno = jmeno
        self.profese = profese
        print("vznikl zamestanec", end = " ")
        self.vypis_zamestance()

    def vypis_zamestance(self):
        print("zamestanec jmenem " + self.jmeno + " ma profesi " + self.profese)



firma1 = Firma("firma1")
zamestanec1 = Zamestanec("Jaromir", "delnik")
zamestanec2 = Zamestanec("Pepa", "reditel")
zamestanec7 = Zamestanec("Karel", "delnik")
zamestanec8 = Zamestanec("Petr", "delnik")
firma1.prijmi_zamestance(zamestanec2)
firma1.prijmi_zamestance(zamestanec1)
firma1.prijmi_zamestance(zamestanec7)
firma1.prijmi_zamestance(zamestanec8)

firma2 = Firma("firma2")
zamestanec3 = Zamestanec("Josef", "delnik")
zamestanec4 = Zamestanec("Pavel", "reditel")
zamestanec5 = Zamestanec("Kuba", "delnik")
zamestanec6 = Zamestanec("Davit", "delnik")
firma2.prijmi_zamestance(zamestanec3)
firma2.prijmi_zamestance(zamestanec4)
firma2.prijmi_zamestance(zamestanec5)
firma2.prijmi_zamestance(zamestanec6)

firma3 = firma2.spoj_firmy(firma1)
firma3.vypis_vsechny_zamestance()
firma3.propust("delnik", 2)
firma3.vypis_vsechny_zamestance()

