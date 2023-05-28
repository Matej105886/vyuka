# slovo = "slovo"
# pocet = 0
# for pismeno in slovo:
#     if pismeno == "s":
#         pocet += 1
# print(pocet)

# slovo = "slovo"
# slovnik = {}
# for pismeno in slovo:
#     if pismeno in slovnik.keys():
#         pocet = slovnik[pismeno]
#         pocet += 1
#         slovnik[pismeno] = pocet
#     else:
#         slovnik[pismeno] = 1
# print(slovnik)

#
#
# cisla = []
# cisla.append(1)
# cisla.append(2)
# cisla.append(1)
# print(cisla)
#
# cisla_set = set()
# cisla_set.add(1)
# cisla_set.add(2)
# cisla_set.add(1)
# print(cisla_set)


class Predmet:
    def __init__(self, nazev, ucitel):
        self.nazev = nazev
        self.ucitel = ucitel

    def vypis(self):
        print("predmet " + self.nazev + " uci ucitel " + self.ucitel.jmeno)

def vytvor_predmet(jmeno, ucitel):
    predmet = Predmet(jmeno, ucitel)
    ucitel.predmety.add(predmet)
    return predmet

class Ucitel:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.predmety = set()

    def vypis(self):
        print("ucitel " + self.jmeno + " uci tyto predmety:" ,end=" ")
        for predmet in self.predmety:
            print(predmet.nazev, end=", ")
        print()

ucitele = set()
list_predmetu2 = []
list_predmetu = []
ucitel1 = Ucitel("Pavel")
ucitel2 = Ucitel("Jan")
ucitel3 = Ucitel("Jiri")
list_predmetu.append(vytvor_predmet("fyzika", ucitel1))
matematika = vytvor_predmet("matematika", ucitel1)
list_predmetu.append(matematika)
# matematika = vytvor_predmet("matematika", ucitel3)
ucitel3.predmety.add(matematika)
list_predmetu.append(matematika)
list_predmetu.append(vytvor_predmet("cestina", ucitel2))
list_predmetu.append(vytvor_predmet("dejepis", ucitel2))
for predmet in list_predmetu:
    ucitele.add(predmet.ucitel)
for ucitel in ucitele:
    print(ucitel.jmeno)
    for predmet in ucitel.predmety:
        list_predmetu2.append(predmet)

for predmet in list_predmetu2:
    print(predmet.nazev)
