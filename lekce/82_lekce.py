# with open("data.txt", "w") as data:
#     for cislo in range(1, 6):
#         data.write(str(cislo) + "\n")
#
# # with open("daa.txt", "r") as data:
# #     for line in data:
# #         print(line, end = "")
#
#
# def otevri(nazev_souboru):
#     try:
#         for one in open(nazev_souboru, "r"):
#             print(one, end = "")
#     except:
#         print("soubor nenalezen")
#
#
#
#
# otevri("data.txt")

class Zamestnanec:
    def __init__(self, jmeno, plat, specializace):
        self.jmeno = jmeno
        self.plat = plat
        self.specializace = specializace

    def vypis(self):
        print("zamesnanec " + self.jmeno + " ma plat " + str(self.plat) + " ma specializaci " + self.specializace)



class Databaze:
    def __init__(self):
        self.list_zamestnancu = []

    def pridej_zamestnance(self):
        jmeno = input("jake je jmeno zamestnance?: ")
        plat = int(input("jaky je plat zamestnance?: "))
        specializace = input("jaka je spicializace?: ")
        zamestnanec = Zamestnanec(jmeno, plat, specializace)
        self.list_zamestnancu.append(zamestnanec)


    def vypis_vsech_zamestnancu(self):
        for zamestnanec in self.list_zamestnancu:
            zamestnanec.vypis()

    def uloz(self):
        with open("data.txt", "w") as data:
            for zamestnanec in self.list_zamestnancu:
                data.write(zamestnanec.jmeno + ";" + str(zamestnanec.plat) + ";" + zamestnanec.specializace + "\n")

    def nahraj(self):
        with open("data.txt", "r") as data:
            for line in data:
                jmeno, plat, specializace = line.strip().split(";")
                zamestnanec = Zamestnanec(jmeno, int(plat), specializace)
                self.list_zamestnancu.append(zamestnanec)

    def vypocitej_prumnerny_plat(self):
        plat_dohromady = 0
        for zamestnanec in self.list_zamestnancu:
            plat_dohromady += zamestnanec.plat
        print("prumnerny plat zamestnancu je " + str(plat_dohromady // len(self.list_zamestnancu)))


    def vypocitej_median_platu(self):
        list_platu = []
        for zamestnanec in self.list_zamestnancu:
            list_platu.append(zamestnanec.plat)
        list_platu.sort()
        if len(list_platu) % 2 == 1:
            index = len(list_platu) // 2
            print("madian platu zamestnancu je " + str(list_platu[index]))
        else:
            index1 = len(list_platu) //2 - 1
            index2 = len(list_platu) // 2
            plat1 = list_platu[index1]
            plat2 = list_platu[index2]
            plat = (plat1 + plat2) //2
            print("madian platu zamestnancu je " + str(plat))


    # def vypis_vsechny_zamestnance_jejihz_plat_je_rovno_nebo_vetsi_nez(self, hranicni_plat):
    #     for zamestnanec in self.list_zamestnancu:
    #         if zamestnanec.plat >= hranicni_plat:
    #             zamestnanec.vypis()
    #
    #
    # def vipis_vsechny_zamestnance_jejihz_profese_je(self, profese):
    #     for zamestnanec in self.list_zamestnancu:
    #         if zamestnanec.specializace == profese:
    #             zamestnanec.vypis()


    def vypis_vyhovujici_zamestnance(self, parametr, funkce_podminka):
        for zamestnanec in self.list_zamestnancu:
            if funkce_podminka(zamestnanec, parametr):
                zamestnanec.vypis()



databaze = Databaze()
while True:
    volba = input("pridani zamestnance = 1; vypis vsech zamestnancu = 2; ulozeni = 3; nahrani = 5; prumnerny plat = 6; median platu = 7; vypis plat vyzsi nez = 8; vypis zamestnance z danou profesi = 9; ukonceni = x: ")
    if volba == "1":
        databaze.pridej_zamestnance()
    elif volba == "2":
        databaze.vypis_vsech_zamestnancu()
    elif volba == "3":
        databaze.uloz()
    elif volba == "x":
        break
    elif volba == "5":
        databaze.nahraj()
    elif volba == "6":
        databaze.vypocitej_prumnerny_plat()
    elif volba == "7":
        databaze.vypocitej_median_platu()
    elif volba == "8":
        hranicni_plat = int(input("zadej hranicni plat zamestnance: "))
        # databaze.vypis_vsechny_zamestnance_jejihz_plat_je_rovno_nebo_vetsi_nez(hranicni_plat)
        funkce_plat_vetsi_nez = lambda zamestnanec, hranicni_plat: zamestnanec.plat >= hranicni_plat
        databaze.vypis_vyhovujici_zamestnance(hranicni_plat, funkce_plat_vetsi_nez)

    elif volba == "9":
        profese = input("zadej danou profesi: ")
        # databaze.vipis_vsechny_zamestnance_jejihz_profese_je(profese)
        funkce_profese = lambda zamestnanec, profese: zamestnanec.specializace == profese
        databaze.vypis_vyhovujici_zamestnance(profese, funkce_profese)
    else:
        print("spatna volba")