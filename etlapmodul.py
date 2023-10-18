def sor(jel,db):
    print(jel*db)


def cim (jel,szoveg,jel2,etlap_hossz):
    hossz=etlap_hossz-(len(jel)+len(jel2))
    print(f"{jel}{szoveg:^{hossz}}{jel2}")

def kaja(jel,levesek,levesAr,penznem,jel2,etlap_hossz):
    hossz:int = int(etlap_hossz/4)


    print(f"{jel:<8}{levesek:<20}{levesAr:>20}{penznem:<5}{jel2:>7}")

def kaja2(jel,foetelek,foetelAr,penznem,jel2,etlap_hossz):
    hossz:int = int(etlap_hossz/4)


    print(f"{jel}{foetelek}{foetelAr:>{hossz*2}}{penznem:<{hossz-2}}{jel2}")


