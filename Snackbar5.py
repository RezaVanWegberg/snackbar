from ast import While
from lib2to3.pygram import pattern_grammar
from msilib.schema import Patch
import random
from tracemalloc import stop
from typing import List

PrijsPatat = 2.40

PrijsGewone = 0.95
PrijsVega = 1.23
PrijsXXL = 2.10

PrijsKroket = 0.85
PrijsKroketBrood = 1.28
PrijsKetchup = 0.23
PrijsMayo = 0.19

BittergarnituurPrijs = 0.60

Ketchup = ["K", "k", "Ketchup", "ketchup", "KETCHUP"]
Mayo = ["M", "m", "Mayo", "mayo", "MAYO"]
ListXXL = ["X", "x", "XXL", "Xxl"]
ListVega = ["V", "v", "Vega", "VEGA", "vega"]
ListGewone = ["G", "g", "Gewone", "GEWONE", "gewone"]
ListMet = ["M", "m", "Met", "MET", "met"]
ListZonder = ["Z", "z", "Zonder", "zonder", "ZONDER"]
ListY = ["Y", "y", "Yes", "YES", "yes"]
ListN = ["N", "n", "No", "NO", "no"]

PatCounter = 0

KetchupCounter = 0
MayoCounter = 0

gewone = 0
vega = 0
Xxl = 0

kroketbrood = 0
kroket = 0

bitterbal = 0
minifrikandel = 0
kipnuggets = 0
bamibal = 0
minikaas = 0


ListBitter = ["Bitterbal", "mini Frikandel", "Kipnuggets", "Bamibal", "Mini Kaassoufflé"]
ListBitterGekregen = []

Bittergarnituur = 0

ListAlles = {"Patat": 0, "Gewone": 0, "Vega": 0, "XXL": 0, "Kroketbrood": 0, "Kroket": 0, "Bitterbal": 0, "MiniFrikandel": 0, "Kipnuggets": 0, "Bamibal": 0, "MiniKaassouffle": 0, "Ketchup": 0, "Mayo":0}

# def VraagSaus():
#     global KetchupCounter
#     global MayoCounter
#     while True:
#         InputSaus = input("Welke saus wil je? [Ketchup] of [Mayo] of [geen] :")
#         if InputSaus in Ketchup:
#             KetchupCounter += 1
#             print()
#             break
#         elif InputSaus in Mayo:
#             MayoCounter += 1
#             print()
#             break
#         elif InputSaus == "geen":
#             print()
#             break       

# def BerekenBTW():
#     btw = TotaleKosten * 0.06
#     print(f"de btw is {btw}")

# a = True
# b = True

# while a == True:
#     b = True
#     VraagSurprise = input("Wilt u een bittergarnituur surprise? [Y] of [N] :")
#     if VraagSurprise in ListY:
#         VraagGrote = input("Welke grootte: [mini], [normal] of [big] :")
#         if VraagGrote == "mini":
#             for x in range(3):
#                 Bittergarnituur += 1
#                 random.shuffle(ListBitter)
#                 ListBitterGekregen.append(ListBitter[1])
#         elif VraagGrote == "normal":
#             for x in range(5):
#                 Bittergarnituur += 1
#                 random.shuffle(ListBitter)
#                 ListBitterGekregen.append(ListBitter[1])
#         elif VraagGrote == "big":
#             for x in range(7):
#                 Bittergarnituur += 1
#                 random.shuffle(ListBitter)
#                 ListBitterGekregen.append(ListBitter[1])

#     HoeveelPat = int(input("Hoeveel patat? :"))
#     patat += PatCounter
#     if HoeveelPat > 0:
#         for p in range(HoeveelPat):
#             VraagSaus()


#     HoeveelFri = int(input("Hoeveel frikandellen? :"))
#     if HoeveelFri > 0:
#         for y in range(HoeveelFri):
#             WelkeSoortFri = input("welke soort frikandel: [gewone], [vega] of [XXL]? :")
#             if WelkeSoortFri in ListGewone:
#                 gewone += 1
#                 VraagSaus()
#             elif WelkeSoortFri in ListVega:
#                 vega += 1
#                 VraagSaus()
#             elif WelkeSoortFri in ListXXL:
#                 Xxl += 1
#                 VraagSaus
#             else:
#                 print()


#     HoeveelKro = int(input("Hoeveel kroketten? :"))
#     if HoeveelKro > 0:
#         for z in range(HoeveelKro):
#             MetBroodje = input("met of zonder broodje? [met] of [zonder] :")
#             if MetBroodje in ListMet:
#                 kroketbrood += 1
#                 VraagSaus()
#             elif MetBroodje in ListZonder:
#                 kroket += 1
#                 VraagSaus()
#             else:
#                 print()
    
#     while b == True:
#         Herhaling = input("nog meer bestellen? [Y] of [N]:")
#         if Herhaling in ListY:
#             a = True
#             b = False
#         elif Herhaling in ListN:
#             a = False
#             b = False



while True:
    VraagBestellen = input(f"wat wilt u bestellen? Kies uit \n {ListAlles} \n of stop :")
    if VraagBestellen == "Patat":
        Aantal = int(input("Hoeveel wilt u hebben van deze item? :"))
        ListAlles["Patat"] += Aantal
        PatCounter += Aantal
        Aantal = 0

    if VraagBestellen == "Gewone":
        Aantal = int(input("Hoeveel wilt u hebben van deze item? :"))
        ListAlles["Gewone"] += Aantal
        gewone += Aantal
        Aantal = 0

    if VraagBestellen == "Vega":
        Aantal = int(input("Hoeveel wilt u hebben van deze item? :"))
        ListAlles["Vega"] += Aantal
        vega += Aantal
        Aantal = 0

    if VraagBestellen == "XXL":
        Aantal = int(input("Hoeveel wilt u hebben van deze item? :"))
        ListAlles["XXL"] += Aantal
        Xxl += Aantal
        Aantal = 0

    if VraagBestellen == "Kroketbrood":
        Aantal = int(input("Hoeveel wilt u hebben van deze item? :"))
        ListAlles["Kroketbrood"] += Aantal
        kroketbrood += Aantal
        Aantal = 0

    if VraagBestellen == "Kroket":
        Aantal = int(input("Hoeveel wilt u hebben van deze item? :"))
        ListAlles["Kroket"] += Aantal
        kroket += Aantal
        Aantal = 0

    if VraagBestellen == "Bitterbal":
        Aantal = int(input("Hoeveel wilt u hebben van deze item? :"))
        ListAlles["Bitterbal"] += Aantal
        bitterbal += Aantal
        Aantal = 0

    if VraagBestellen == "MiniFrikandel":
        Aantal = int(input("Hoeveel wilt u hebben van deze item? :"))
        ListAlles["MiniFrikandel"] += Aantal
        minifrikandel += Aantal
        Aantal = 0

    if VraagBestellen == "Kipnuggets":
        Aantal = int(input("Hoeveel wilt u hebben van deze item? :"))
        ListAlles["Kipnuggets"] += Aantal
        kipnuggets += Aantal
        Aantal = 0

    if VraagBestellen == "Bamibal":
        Aantal = int(input("Hoeveel wilt u hebben van deze item? :"))
        ListAlles["Bamibal"] += Aantal
        bamibal += Aantal
        Aantal = 0

    if VraagBestellen == "MiniKaassouffle":
        Aantal = int(input("Hoeveel wilt u hebben van deze item? :"))
        ListAlles["MiniKaassouffle"] += Aantal
        minikaas += Aantal
        Aantal = 0

    if VraagBestellen == "Ketchup":
        Aantal = int(input("Hoeveel wilt u hebben van deze item? :"))
        ListAlles["Ketchup"] += Aantal
        KetchupCounter += Aantal
        Aantal = 0

    if VraagBestellen == "Mayo":
        Aantal = int(input("Hoeveel wilt u hebben van deze item? :"))
        ListAlles["Mayo"] += Aantal
        MayoCounter += Aantal
        Aantal = 0

    
    elif VraagBestellen == "stop":
        break
    else:
        print()

    
TotaalBittergarnituur = Bittergarnituur * BittergarnituurPrijs
        

TotaalKet = KetchupCounter * PrijsKetchup
TotaalMay = MayoCounter * PrijsMayo
TotaalPat = PatCounter * PrijsPatat

TotaalGew = gewone * PrijsGewone
TotaalVeg = vega * PrijsVega
TotaalXXL = Xxl * PrijsXXL

TotaalKro = kroket * PrijsKroket
TotaalKroBro = kroketbrood * PrijsKroketBrood

TotaleKosten = TotaalPat + TotaalGew + TotaalVeg + TotaalXXL + TotaalKro + TotaalKet + TotaalMay 
BestelKosten = 1.35

def Bonnetje():
    print()
    if PatCounter > 0:
        print(f"Patat = {PatCounter} x {PrijsPatat} = €{TotaalPat:.2f}")


    if gewone > 0:
        print(f"Gewone Frikandel = {gewone} x {PrijsGewone} = €{TotaalGew:.2f}")
    if vega > 0:
        print(f"Vega Frikandel = {vega} x {PrijsVega} = €{TotaalVeg:.2f}")
    if Xxl > 0:
        print(f"XXL Frikandel = {Xxl} x {PrijsXXL} = {TotaalXXL:.2f}")


    if kroket > 0:
        print(f"Kroket = {kroket} x {PrijsKroket} = €{TotaalKro:.2f}")
    if kroketbrood > 0:
        print(f"Kroket Brood = {kroketbrood} x {PrijsKroketBrood:.2f} = €{TotaalKroBro:.2f}")

    if Bittergarnituur > 0:
        print(f"Bittergarnituur = {Bittergarnituur} x {BittergarnituurPrijs:.2f} = €{TotaalBittergarnituur:.2f}")
        print(f"Dit zijn de items: {ListBitterGekregen}")

    if KetchupCounter > 0:
        print(f"Ketchup = {KetchupCounter} x 0.23 = €{TotaalKet:.2f}")
    if MayoCounter > 0:
        print(f"Mayo = {MayoCounter} x 0.19 = €{TotaalMay:.2f}")


    if TotaleKosten < 10:
        TotaleKosten + BestelKosten
        print(f"Bestelkosten = {BestelKosten}")
        print(f"Totaal = €{TotaleKosten + BestelKosten:.2f}")
    elif TotaleKosten > 40 and TotaleKosten <= 100:
        print(f"5% korting = {TotaleKosten * 0.05:.2f}")
        print(f"Totaal = €{TotaleKosten * 0.95:.2f}" )
    elif TotaleKosten >= 10 and TotaleKosten <= 40:
        print(f"Totaal = €{TotaleKosten:.2f}")
    elif TotaleKosten > 100:
        print(f"7% korting = {TotaleKosten * 0.075:.2f}")
        print(f"Totaal = €{TotaleKosten * 0.925:.2f}")


Bonnetje()

