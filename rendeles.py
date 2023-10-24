import etlapmodul
penznem="Ft"
etlap_hossz=60
szamlahossz=30
osszeg:int=0
levesek = ["Húsleves ", "Gyümölcsleves "]
levesAr = [1999, 1500]
foetelek = ["Csirkepörkölt ", "Mátrai borzaska "]
foetelAr = [2980, 4500]
rendelt = []
rendeltAr = []
global LeValasztas
global FoValasztas
nemkert:bool=False
def leves(levesAr,foetelAr,nemkert,osszeg):


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

        foetel(foetelAr,valasz1,nemkert,osszeg)
    elif valasz1 =="n":
        nemkert = True
        foetel(foetelAr,valasz1,nemkert,osszeg)

    return  valasz1 ,nemkert, osszeg




def foetel(foetelAr,valasz1,nemkert,osszeg):
    valasz = input("Kér főételt? (I/N): ").lower()
    if valasz == "i":
        print("Fő ételek:")
        print("1-Csirkepörkölt\n2-Mátrai borzaska")

        valasz = int(input("1 vagy 2? "))
        while (valasz!= 1) and (valasz != 2):
            valasz = int(input("1 vagy 2? "))
        if valasz == 1:
                    osszeg += foetelAr[0]
                    FoValasztas=1
                    print("hmm")
                    etlapmodul.szamlacim("*", "Számla", "*", szamlahossz)
                    etlapmodul.szamlaSor("*", szamlahossz)
                    etlapmodul.kertEtelekcim("*", "Kért ételek: ", "*", szamlahossz)
                    if valasz1 == 1:
                        etlapmodul.valasztottetel("*", levesek[0], levesAr[0], "Ft", "*")
                    elif valasz1 == 2:
                        etlapmodul.valasztottetel2("*", levesek[1], levesAr[1], "Ft", "*")
                    etlapmodul.valasztottetel("*", foetelek[0], foetelAr[0], "Ft", "*")
                    etlapmodul.vegosszeg("*","Fizetendő összeg: ",osszeg,penznem,"*")
                    print("Köszönjük hogy nálunk rendelt!")
        elif valasz==2:
                    osszeg += foetelAr[1]
                    FoValasztas=2
                    print("ehe")
                    etlapmodul.szamlacim("*", "Számla", "*", szamlahossz)
                    etlapmodul.szamlaSor("*", szamlahossz)
                    etlapmodul.kertEtelekcim("*", "Kért ételek: ", "*", szamlahossz)
                    if valasz1 == 1:
                        etlapmodul.valasztottetel("*", levesek[0], levesAr[0], "Ft", "*")
                    elif valasz1 == 2:
                        etlapmodul.valasztottetel2("*", levesek[1], levesAr[1], "Ft", "*")
                    etlapmodul.valasztottetel("*", foetelek[1], foetelAr[1], "Ft", "*")
                    etlapmodul.vegosszeg("*","Fizetendő összeg: ",osszeg,penznem,"*")
                    print("Köszönjük hogy nálunk rendelt!")
    if valasz =="n" and nemkert==True:
        print("Ön nem kér semmit!")
        exit()

    if valasz =="n" and nemkert==False:
        etlapmodul.szamlacim("*", "Számla", "*", szamlahossz)
        etlapmodul.szamlaSor("*", szamlahossz)
        etlapmodul.kertEtelekcim("*", "Kért ételek: ", "*", szamlahossz)
        if valasz1 ==1:
            etlapmodul.valasztottetel("*", levesek[0], levesAr[0],"Ft", "*")
        elif valasz1==2:
            etlapmodul.valasztottetel2("*", levesek[1], levesAr[1],"Ft", "*")
        etlapmodul.szamlaSor("*", szamlahossz)
        etlapmodul.vegosszeg("*","Fizetendő összeg: ",osszeg,penznem,"*")
        print("Köszönjük hogy nálunk rendelt!")


def desszert():
    valasz = input("Kér desszertet? (I/N): ").lower()
    if valasz == "i":
        print("desszertek:")
        print("1-Csirkepörkölt\n2-Mátrai borzaska")

        valasz = int(input("1 vagy 2? "))
        while (valasz != 1) and (valasz != 2):
            valasz = int(input("1 vagy 2? "))
        if valasz == 1: