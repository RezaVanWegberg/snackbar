from lib2to3.pygram import pattern_grammar


HoeveelPat = int(input("Hoeveel patat? :"))
HoeveelFri = int(input("Hoeveel frikandellen? :"))
HoeveelKro = int(input("Hoeveel kroketten? :"))

PrijsPat = HoeveelPat * 1.20
PrijsFri = HoeveelFri * 0.95
PrijsKro = HoeveelKro * 0.85

def Bonnetje():
    if HoeveelPat > 0:
        print(f"Patat = €{PrijsPat}")
    if HoeveelFri > 0:
        print(f"Frikandel = €{PrijsFri}")
    if HoeveelKro > 0:
        print(f"Kroket = €{PrijsKro}")
    
Bonnetje()