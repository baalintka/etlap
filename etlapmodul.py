def sor(jel,db):
    print(jel*db)

import rendeles
def cim (jel,szoveg,jel2,etlap_hossz):
    hossz=etlap_hossz-(len(jel)+len(jel2))
    print(f"{jel}{szoveg:^{hossz}}{jel2}")

def kaja(jel,levesek,levesAr,penznem,jel2,etlap_hossz):
    hossz:int = int(etlap_hossz/4)


    print(f"{jel:<8}{levesek:<20}{levesAr:>20}{penznem:<5}{jel2:>7}")

def kaja2(jel,foetelek,foetelAr,penznem,jel2,etlap_hossz):
    hossz:int = int(etlap_hossz/4)


    print(f"{jel}{foetelek}{foetelAr:>{hossz*2}}{penznem:<{hossz-2}}{jel2}")


def szamlaSor(jel,db):
    print(jel*db)
def szamlacim(jel,szoveg,jel2,szamlahossz):
    hossz=szamlahossz-(len(jel)+len(jel2))
    print(f"{jel}{szoveg:^{hossz}}{jel2}")
def kertEtelekcim(jel,szoveg,jel2,szamlahossz):
    print(f"{jel:<5}{szoveg}{jel2:>12}")
def valasztottetel(jel,szoveg,ar,penznem,jel2):
    print(f"{jel:<5}{szoveg }{ar}{penznem:<5}{jel2:>8}")
def valasztottetel2(jel,szoveg,ar,penznem,jel2):
    print(f"{jel:<5}{szoveg:<5}{ar:<5}{penznem:<5}{jel2:>2}")