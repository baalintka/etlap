import fomenu
penznem="Ft"
etlap_hossz=60
szamlahossz=30
osszeg:int=0
levesek = ["Húsleves", "Gyümölcsleves"]
levesAr = [1999, 1500]
foetelek = ["Csirkepörkölt", "Mátrai borzaska"]
foetelAr = [2980, 4500]
rendelt = []
rendeltAr = []
global LeValasztas
global FoValasztas
nemkert:bool=False
def leves(levesAr,foetelAr,nemkert):


    valasz1 = input("Kér levest? (I/N): ").lower()
    if valasz1 == "i":
        print("Levesek:")
        print("1-Húsleves\n""2-Gyümölcsleves\n")
        valasz1 = int(input("1 vagy 2?"))
        while (valasz1 != 1) and (valasz1 != 2):
            valasz1 = int(input("1 vagy 2?"))
            if valasz1 == 1:

                LeValasztas=1
                osszeg=levesAr[0]
                print(LeValasztas,osszeg)
            elif valasz1==2:
                LeValasztas=2
                osszeg = levesAr[1]

        foetel(foetelAr,valasz1,nemkert)
    elif valasz1 =="n":
        nemkert = True
        foetel(foetelAr,valasz1,nemkert)

    return  valasz1 ,nemkert




def foetel(foetelAr,valasz1,nemkert):
    valasz = input("Kér főételt? (I/N): ").lower()
    if valasz == "i":
        print("Fő ételek:")
        print("1-Csirkepörkölt\n2-Mátrai borzaska")

        valasz = int(input("1 vagy 2? "))
        while (valasz!= 1) and (valasz != 2):
            valasz = int(input("1 vagy 2? "))
            if valasz == 1:
                    FoValasztas=1
                    print("hmm")
            elif valasz==2:
                    FoValasztas=2
                    print("ehe")
    if valasz =="n" and nemkert==True:
        print("Ön nem kér semmit!")
        exit()

    if valasz =="n" and nemkert==False:
        print("Ön kért levest de nem kért főételt")
        szamlacim("*", "Számla", "*", szamlahossz)
        szamlaSor("*", szamlahossz)
        kertEtelekcim("*", "Kért ételek: ", "*", szamlahossz)
        if valasz1 ==1:
            valasztottetel("*", levesek[0], levesAr[0],"Ft", "*")
        elif valasz1==2:
            valasztottetel2("*", levesek[1], levesAr[1],"Ft", "*")
        szamlaSor("*", szamlahossz)
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

