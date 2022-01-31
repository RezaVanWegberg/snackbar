from functools import total_ordering
from lib2to3.pygram import pattern_grammar


HoeveelPat = int(input("Hoeveel patat? :"))
HoeveelFri = int(input("Hoeveel frikandellen? :"))
HoeveelKro = int(input("Hoeveel kroketten? :"))

PrijsPat = HoeveelPat * 1.20
PrijsFri = HoeveelFri * 0.95
PrijsKro = HoeveelKro * 0.85
TotaleKosten = PrijsPat + PrijsFri + PrijsKro
BestelKosten = 1.35

def Bonnetje():
    if HoeveelPat > 0:
        print(f"Patat = €{PrijsPat:.2f}")
    if HoeveelFri > 0:
        print(f"Frikandel = €{PrijsFri:.2f}")
    if HoeveelKro > 0:
        print(f"Kroket = €{PrijsKro:.2f}")
    if TotaleKosten < 10:
        TotaleKosten + BestelKosten
        print(f"Bestelkosten = {BestelKosten}")
        print(f"Totaal = €{TotaleKosten}")
    elif TotaleKosten > 40:
        print(f"5% korting = {TotaleKosten * 0.05:.2f}")
        print(f"Totaal = €{TotaleKosten * 0.95:.2f}" )
    elif TotaleKosten >= 10 and TotaleKosten <= 40:
        print(f"Totaal = €{TotaleKosten}")

Bonnetje()