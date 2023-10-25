import etlapmodul
penznem="Ft"
etlap_hossz=60
szamlahossz=30
osszeg:int=0
desszertek=["Csokis fagyi ", "Macaron "]
dAr=[850, 650]
levesek = ["Húsleves ", "Gyümölcsleves "]
levesAr = [1999, 1500]
foetelek = ["Csirkepörkölt ", "Mátrai borzaska "]
foetelAr = [2980, 4500]
rendelt = []
rendeltAr = []
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
            rendeltAr.append(levesAr[0])
            rendelt.append(levesek[0])

        elif valasz1==2:
            rendeltAr.append(levesAr[1])
            rendelt.append(levesek[1])

        foetel(foetelAr,foetelek,nemkert)
    elif valasz1 =="n":
        nemkert = True
        foetel(foetelAr,foetelek,nemkert)

    return nemkert
def foetel(foetelAr,foetelek,nemkert):
    valasz = input("Kér főételt? (I/N): ").lower()
    if valasz == "i":
        print("Fő ételek:")
        print("1-Csirkepörkölt\n2-Mátrai borzaska")
        valasz = int(input("1 vagy 2? "))
        while (valasz!= 1) and (valasz != 2):
            valasz = int(input("1 vagy 2? "))
        if valasz == 1:
            rendeltAr.append(foetelAr[0])
            rendelt.append(foetelek[0])


        elif valasz==2:
            rendeltAr.append(foetelAr[1])
            rendelt.append(foetelek[1])

        desszert(nemkert)
    if valasz =="n":
        desszert(nemkert)
def desszert(nemkert):
    valasztas = input("Kér desszertet? (I/N): ").lower()
    if valasztas == "i":
        print("desszertek:")
        print("1-Csokis fagyi\n2-Macaron")

        valaszd = int(input("1 vagy 2? "))
        while (valaszd != 1) and (valaszd != 2):
            valaszd = int(input("1 vagy 2? "))
        if valaszd == 1:
            rendelt.append(desszertek[0])
            rendeltAr.append(dAr[0])
            kiiras(rendelt)
        elif valaszd == 2:
            rendelt.append(desszertek[1])
            rendeltAr.append(dAr[1])
            kiiras(rendelt)
    elif valasztas == "n" and nemkert==False:
        print("Ön nem kér semmit!")
        exit()
    elif valasztas == "n" and nemkert==True:
        print("Nem kér desszertet")
        kiiras(rendelt)

def kiiras(rendelt):
    etlapmodul.szamlaSor("*", szamlahossz)
    etlapmodul.szamlacim("*", "Számla", "*", szamlahossz)
    etlapmodul.szamlaSor("*", szamlahossz)
    etlapmodul.kertEtelekcim("*", "Kért ételek: ", "*")
    i=0
    while i <= len(rendelt)-1:
        etlapmodul.valasztottetel2("*", rendelt[i], rendeltAr[i], "Ft", "*")

        i+=1
    osszear=0
    i=0
    while i <= len(rendeltAr)-1:
        osszear+=rendeltAr[i]
        i+=1
    etlapmodul.szamlaSor("*", szamlahossz)
    etlapmodul.vegosszeg("*", "Fizetendő: ",osszear," Ft","*")
    etlapmodul.szamlaSor("*", szamlahossz)

