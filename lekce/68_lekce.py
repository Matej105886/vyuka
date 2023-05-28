import random

class Generator:
    def vygeneruj_list(self, delka_listu, min_cislo, max_cislo):
        list_cisel = []
        for i in range(delka_listu):
            cislo = random.randint(min_cislo, max_cislo)
            list_cisel.append(cislo)
        return list_cisel

    def vygeneruj_list_serazeny_vzestupne(self, delka_listu):
        list_cisel = []
        predchozi_cislo = 0
        for i in range(delka_listu):
            cislo = predchozi_cislo + random.randint(1, 3)
            list_cisel.append(cislo)
            predchozi_cislo = cislo
        return list_cisel



generator = Generator()

list_cisel1 = generator.vygeneruj_list(9, 1, 3)
print(list_cisel1)

list_cisel2 = generator.vygeneruj_list(9, 1, 3)
print(list_cisel2)

list_cisel7 = generator.vygeneruj_list(9, 1, 3)
print(list_cisel7)

list_cisel8 = []
for i in range(len(list_cisel1)):
    if list_cisel1[i] > list_cisel2[i] and list_cisel1[i] >list_cisel7[i]:
        list_cisel8.append(list_cisel1[i])
    elif list_cisel2[i] > list_cisel1[i] and list_cisel2[i] >list_cisel7[i]:
        list_cisel8.append(list_cisel2[i])
    elif list_cisel7[i] > list_cisel1[i] and list_cisel7[i] >list_cisel2[i]:
        list_cisel8.append(list_cisel7[i])
    elif  list_cisel1[i] > list_cisel2[i]:
        list_cisel8.append(list_cisel1[i])
    elif list_cisel2[i] > list_cisel7[i]:
        list_cisel8.append(list_cisel2[i])
    elif list_cisel7[i] > list_cisel1[i]:
        list_cisel8.append(list_cisel7[i])
    else:
        list_cisel8.append(list_cisel1[i])

print(list_cisel8)


# list_cisel4 = generator.vygeneruj_list_serazeny_vzestupne(10)
# print(list_cisel4)
#
# list_cisel5 = generator.vygeneruj_list_serazeny_vzestupne(10)
# print(list_cisel5)
#
#
# list_cisel6 = []
# soucet_delky_listu = len(list_cisel4) + len(list_cisel5)
# j = 0
# k = 0
# for i in range(soucet_delky_listu):
#     if j >= len(list_cisel4):
#         list_cisel6.append(list_cisel5[k])
#         k += 1
#     elif k >= len(list_cisel5):
#         list_cisel6.append(list_cisel4[j])
#         j += 1
#     elif list_cisel4[j] < list_cisel5[k]:
#         list_cisel6.append(list_cisel4[j])
#         j += 1
#     elif list_cisel4[j] > list_cisel5[k]:
#         list_cisel6.append(list_cisel5[k])
#         k += 1
#     else:
#         list_cisel6.append((list_cisel4[j]))
#         j += 1

# print(list_cisel6)

# list_cisel3 = []
# for i in range(len(list_cisel1)):
#     if list_cisel1[i] > list_cisel2[i]:
#         list_cisel3.append(list_cisel1[i])
#     elif list_cisel1[i] < list_cisel2[i]:
#         list_cisel3.append(list_cisel2[i])
#     else:
#         list_cisel3.append(list_cisel1[i])
# print(list_cisel3)

# soucet_cisel = 0
# for cislo in cislo1:
#     soucet_cisel += cislo
# chybi_do_100 = 100 - soucet_cisel
# cislo1.append(chybi_do_100)
# print(cislo1)
