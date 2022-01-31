from functools import total_ordering
from lib2to3.pygram import pattern_grammar
from operator import truediv
from xml.dom import HIERARCHY_REQUEST_ERR

PrijsPatat = 2.40

PrijsGewone = 0.95
PrijsVega = 1.23
PrijsXXL = 2.10

PrijsKroket = 0.85
PrijsKroketBrood = 1.28
PrijsKetchup = 0.23
PrijsMayo = 0.19


Ketchup = ["K", "k", "Ketchup", "ketchup", "KETCHUP"]
Mayo = ["M", "m", "Mayo", "mayo", "MAYO"]
ListXXL = ["X", "x", "XXL", "Xxl"]
ListVega = ["V", "v", "Vega", "VEGA", "vega"]
ListGewone = ["G", "g", "Gewone", "GEWONE", "gewone"]
ListMet = ["M", "m", "Met", "MET", "met"]
ListZonder = ["Z", "z", "Zonder", "zonder", "ZONDER"]
ListY = ["Y", "y", "Yes", "YES", "yes"]
ListN = ["N", "n", "No", "NO", "no"]

patat = 0

KetchupCounter = 0
MayoCounter = 0

gewone = 0
vega = 0
Xxl = 0

kroketbrood = 0
kroket = 0

a = True
b = True

while a == True:
    b = True
    HoeveelPat = int(input("Hoeveel patat? :"))
    patat += HoeveelPat
    if HoeveelPat > 0:
        for x in range(HoeveelPat):
            WelkeSaus = input("Wat voor saus wil je? [Ketchup] of [Mayo] of [Geen] :")
            if WelkeSaus in Ketchup:
                KetchupCounter += 1
            elif WelkeSaus in Mayo:
                MayoCounter += 1
            else:
                print()


    HoeveelFri = int(input("Hoeveel frikandellen? :"))
    if HoeveelFri > 0:
        for y in range(HoeveelFri):
            WelkeSoortFri = input("welke soort frikandel: [gewone], [vega] of [XXL]? :")
            if WelkeSoortFri in ListGewone:
                gewone += 1
            elif WelkeSoortFri in ListVega:
                vega += 1
            elif WelkeSoortFri in ListXXL:
                Xxl += 1
            else:
                print()


    HoeveelKro = int(input("Hoeveel kroketten? :"))
    if HoeveelKro > 0:
        for z in range(HoeveelKro):
            MetBroodje = input("met of zonder broodje? [met] of [zonder] :")
            if MetBroodje in ListMet:
                kroketbrood += 1
            elif MetBroodje in ListZonder:
                kroket += 1
            else:
                print()
    
    while b == True:
        Herhaling = input("nog meer bestellen? [Y] of [N]:")
        if Herhaling in ListY:
            a = True
            b = False
        elif Herhaling in ListN:
            a = False
            b = False
    

        

TotaalKet = KetchupCounter * PrijsKetchup
TotaalMay = MayoCounter * PrijsMayo
TotaalPat = HoeveelPat * PrijsPatat

TotaalGew = gewone * PrijsGewone
TotaalVeg = vega * PrijsVega
TotaalXXL = Xxl * PrijsXXL

TotaalKro = kroket * PrijsKroket
TotaalKroBro = kroketbrood * PrijsKroketBrood

TotaleKosten = TotaalPat + TotaalGew + TotaalVeg + TotaalXXL + TotaalKro + TotaalKet + TotaalMay 
BestelKosten = 1.35

def Bonnetje():
    print()
    if patat > 0:
        print(f"Patat = {patat} x {PrijsPatat} = €{TotaalPat:.2f}")


    if gewone > 0:
        print(f"Gewone Frikandel = {gewone} x {PrijsGewone} = €{TotaalGew:.2f}")
    if vega > 0:
        print(f"Vega Frikandel = {vega} x {PrijsVega} = €{TotaalVeg:.2f}")
    if Xxl > 0:
        print(f"XXL Frikandel = {Xxl} x {PrijsXXL} = {TotaalXXL:.2f}")


    if kroket > 0:
        print(f"Kroket = {kroket} x {PrijsKroket} = €{TotaalKro:.2f}")
    if kroketbrood > 0:
        print(f"Kroket Brood = {kroketbrood} x {PrijsKroketBrood:.2f} = €")


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

