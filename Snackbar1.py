from functools import total_ordering
from lib2to3.pygram import pattern_grammar

Ketchup = ["K", "k", "Ketchup", "ketchup", "KETCHUP"]
Mayo = ["M", "m", "Mayo", "mayo", "MAYO"]
KetchupCounter = 0
MayoCounter = 0

HoeveelPat = int(input("Hoeveel patat? :"))
if HoeveelPat > 0:
    for x in range(HoeveelPat):
        WelkeSaus = input("Wat voor saus wil je? [Ketchup] of [Mayo] of [Geen]:")
        if WelkeSaus in Ketchup:
            KetchupCounter += 1
        elif WelkeSaus in Mayo:
            MayoCounter += 1
        else:
            print()


HoeveelFri = int(input("Hoeveel frikandellen? :"))
HoeveelKro = int(input("Hoeveel kroketten? :"))

PrijsKet = KetchupCounter * 0.23
PrijsMay = MayoCounter * 0.19

PrijsPat = HoeveelPat * 1.20
PrijsFri = HoeveelFri * 0.95
PrijsKro = HoeveelKro * 0.85
TotaleKosten = PrijsPat + PrijsFri + PrijsKro + PrijsKet + PrijsMay 
BestelKosten = 1.35

def Bonnetje():
    if HoeveelPat > 0:
        print(f"Patat = {HoeveelPat} x 1.20 = €{PrijsPat:.2f}")
    if HoeveelFri > 0:
        print(f"Frikandel {HoeveelFri} x 0.95 = €{PrijsFri:.2f}")
    if HoeveelKro > 0:
        print(f"Kroket = {HoeveelKro} x 0.85 = €{PrijsKro:.2f}")

    if KetchupCounter > 0:
        print(f"Ketchup = {KetchupCounter} x 0.23 = €{PrijsKet:.2f}")
    if MayoCounter > 0:
        print(f"Mayo = {MayoCounter} x 0.19 = €{PrijsMay:.2f}")
    
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

