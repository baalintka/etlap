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




def rendelles(lista,kerdes,lista2,aktual):
    valasz1 = input(kerdes).lower()
    if valasz1 == "i":
        for i in range(2):
            etlapmodul.kaja("*",lista[i],lista2[i],penznem,"*")
        valasz1 = int(input(f"Melyik {aktual} kéri? 1/2"))
        while not(valasz1>=1 and valasz1<=len(lista)-1):
            valasz1 = int(input(f"Melyik {aktual} kéri? 1/2..."))
        rendeltAr.append(lista[valasz1-1])
        rendelt.append(lista2[valasz1-1])

    elif valasz1 =="n":
        print(f"Nem kért {aktual}")



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

