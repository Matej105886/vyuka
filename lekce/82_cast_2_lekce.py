def secti_cisla(cislo1, cislo2):
    return cislo1 + cislo2

print(secti_cisla(4, 3))

secti_cisla_2 = lambda cislo1, cislo2: cislo1 + cislo2
print(secti_cisla_2(5, 4))

je_vetasi_nez_10 = lambda cislo: cislo > 10
print(je_vetasi_nez_10(15))

vynasob_10 = lambda cislo: cislo * 10
print(vynasob_10("ahoj"))
