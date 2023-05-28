# while True:
#     try:
#         cislo = int(input("zadej cislo: "))
#         print(cislo)
#         break
#
#     except ValueError:
#         print("toto nebylo cislo")
#
# print("tady program pokracuje")

# while True:
#     try:
#         cislo1 = int(input("zadej 1. cislo: "))
#         while True:
#             try:
#                 cislo2 = int(input("zadej2. cislo: "))
#                 cislo3 = cislo1 // cislo2
#                 break
#             except ZeroDivisionError:
#                 print("zadej znovu 2. cislo")
#         print("vysledek deleni je "+ str(cislo3))
#         break
#
#     except ValueError:
#         print("zadal jsi alespon 1 cislo spatne " )

#
# while True:
#     try:
#         cislo1 = int(input("zadej 1. cislo: "))
#         break
#
#     except ValueError:
#         print("1. cislo nebylpo cislo")
#
# while True:
#     try:
#         cislo2 = int(input("zadej 2. cislo: "))
#         cislo3 = cislo1 // cislo2
#         print("vysledek deleni je "+ str(cislo3))
#
#         break
#
#     except ValueError:
#         print("2. cislo nebylpo cislo")
#
#     except ZeroDivisionError:
#         print("0 nelze delit")

# while True:
#     try:
#         cislo1 = int(input("zadej 1. cislo: "))
#         break
#
#     except ValueError:
#         print("1. cislo nebylpo cislo")
#
# while True:
#     try:
#         cislo2 = int(input("zadej 2. cislo: "))
#         if cislo2 == 0:
#             raise Exception("0 nepujde delit")
#         break
#
#     except ValueError:
#         print("2. cislo nebylpo cislo")
#
#     except Exception as exception:
#         print(repr(exception))
#
#
#
# try:
#     cislo3 = cislo1 // cislo2
#     print("vysledek deleni je " + str(cislo3))
#
# except ZeroDivisionError:
#     print("0 nelze delit")


class Ovoce:
    def __init__(self, cena, druh):
        if cena <= 0:
            raise Exception("cena nesmi byt zaporna")
        if len(druh) == 0:
            raise Exception("druh musi mit alespon 1 pismenko")
        self.cena = cena
        self.druh = druh
while True:
    try:
        cena = int(input("zadej cenu: "))
        druh = input("zadej druh: ")
        ovoce1 = Ovoce(cena, druh)
        break


    except Exception as exception:
        print(repr(exception))

try:
    print(ovoce1.cena)
    print(ovoce1.druh)

except NameError as nameerror:
    print(repr(nameerror))
