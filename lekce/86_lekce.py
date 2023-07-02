class Uzivatel:
    def __init__(self, jmeno, heslo, role):
        self.jmeno = jmeno
        self.heslo = heslo
        self.role = role

    def vypis(self):
        print("uzvatel: " + self.jmeno + ", heslo: " + self.heslo)


class Program:
    def __init__(self):
        self.uzivatele = []
        self.prihlaseny_uzivatel = None

    def registrace(self):
        uzivatelske_jmeno = input("zadej uzivatelske jmeno: ")
        heslo = input("zadej heslo: ")
        role = input("zadej roli: ")
        uzivatel = Uzivatel(uzivatelske_jmeno, heslo, role)
        self.uzivatele.append(uzivatel)
        with open ("uzivatele.txt", "a") as uzivatele:
            uzivatele.write(uzivatel.jmeno + ";" + uzivatel.heslo + ";" + uzivatel.role + "\n")

    def prihlaseni(self):
        nasli = False
        prihlaseny_uzivatel = None
        zadane_uzivatelske_jmeno = input("zadej uzivatelske jmeno: ")

        with open("uzivatele.txt", "r") as uzivatele:
            for jeden_uzivatel in uzivatele:
                uzivatelske_jmeno, heslo, role = jeden_uzivatel.strip().split(";")
                uzivatel = Uzivatel(uzivatelske_jmeno, heslo, role)
                self.uzivatele.append(uzivatel)
                if zadane_uzivatelske_jmeno == uzivatelske_jmeno:
                    nasli = True
                    heslo_z_databaze = heslo
                    prihlaseny_uzivatel = uzivatel
        if nasli == True:
            print("uzivatel byl nalezen")
        else:
            nasli = False
            while not nasli:
                zadane_uzivatelske_jmeno = input("zadej uzivatelske jmeno: ")
                for jeden_uzivatel in self.uzivatele:
                    if zadane_uzivatelske_jmeno == jeden_uzivatel.jmeno:
                        nasli = True
                        heslo_z_databaze = jeden_uzivatel.heslo
                        prihlaseny_uzivatel = jeden_uzivatel
                        print("uzivatel byl nlezen")
                        break
        pokus = 0
        while True:
            if pokus >= 3:
                print("3 spatne pokusy ukonci program")
                return
            zadane_heslo = input("zadej heslo: ")
            if zadane_heslo == heslo_z_databaze:
                print("uzivatel byl prihlasen")
                break
            pokus += 1
        return prihlaseny_uzivatel

    def vypis_vsechny_uzivatele(self):
        for uzivatel in self.uzivatele:
            uzivatel.vypis()

    def vypis_data(self):
        print("vypisuji data")

    def zapis_do_databaze(self):
        radek = input("zadej data: ")
        with open("data_databaze.txt", "a") as data:
            data.write(self.prihlaseny_uzivatel.jmeno + ": " + radek + "\n")


    def vypis_z_databaze(self):
        i = 0
        with open("data_databaze.txt", "r") as data:
            for radek in data:
                print(str(i) + radek, end= "")
                i += 1

    def vymaz_data(self):
        radky = []
        self.vypis_z_databaze()
        index_radku = int(input("zadej index radku, ktery chces smazat: "))
        with open ("data_databaze.txt", "r") as data:
            for radek in data:
                radky.append(radek)
        uzivatel_jmeno, data = radek.split(":")
        if self.prihlaseny_uzivatel.jmeno != uzivatel_jmeno and self.prihlaseny_uzivatel.role != "admin":
            print("nemate opravneni k mazani radku")
            return
        radky.pop(index_radku)

        with open ("data_databaze.txt", "w") as data:
            for radek in radky:
                data.write(radek)




    def spust(self):
        while True:
            volba = input("registrovat = 1, prihlasit = 2: ")
            if volba == "1":
                self.registrace()
            elif volba == "2":
                self.prihlaseny_uzivatel = self.prihlaseni()
                break
            else:
                print("spatne uzivatelske jmeno nebo heslo")
        while True:
            volba = input("vypis vsechny uzivatele = 1, vypis data = 2, zapis = 3, vymaz data = 4: ")
            if volba == "1":
                if self.prihlaseny_uzivatel.role != "admin":
                    print("nemate opravneni prohlizet uzivatele")
                    return
                self.vypis_vsechny_uzivatele()
            elif volba == "2":
                self.vypis_z_databaze()
            elif volba == "3":
                self.zapis_do_databaze()
            elif volba == "4":
                self.vymaz_data()



program = Program()
program.spust()