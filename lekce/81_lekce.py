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


databaze = Databaze()
while True:
    volba = input("pridani zamestnance = 1; vypis vsech zamestnancu = 2; ulozeni = 3; nahrani = 5; prumnerny plat = 6; ukonceni = x: ")
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
    else:
        print("spatna volba")