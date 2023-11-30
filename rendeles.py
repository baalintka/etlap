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
    valasz:int=0
    if valasz1 == "i":
        for i in range(2):
            etlapmodul.kaja("*",lista[i],lista2[i],penznem,"*")
        valasz = int(input(f"Melyik {aktual} kéri? 1/2"))
        while not(valasz>=1 and valasz<=len(lista)):
            valasz = int(input(f"Melyik {aktual} kéri? 1/2..."))
        rendeltAr.append(lista[valasz-1])
        rendelt.append(lista2[valasz-1])

    elif valasz1 =="n":
        print(f"Nem kért {aktual}")

    return valasz

valasztott1=rendelles(levesek,"Kér levest? (I/N):",levesAr,"levest")
valasztott2=rendelles(foetelek,"Kér főételt? (I/N):",foetelAr,"főételt")
valasztott3=rendelles(desszertek,"Kér desszertet? (I/N):",dAr,"desszertet")
def kiiras(rendelt,rendeltAr):
    etlapmodul.szamlaSor("*", szamlahossz)
    etlapmodul.szamlacim("*", "Számla", "*", szamlahossz)
    etlapmodul.szamlaSor("*", szamlahossz)
    etlapmodul.kertEtelekcim("*", "Kért ételek: ", "*")

    etlapmodul.valasztottetel2("*", rendelt[valasztott1], rendeltAr[valasztott1], "Ft", "*")
    etlapmodul.valasztottetel2("*", rendelt[valasztott2], rendeltAr[valasztott2], "Ft", "*")
    etlapmodul.valasztottetel2("*", rendelt[valasztott3], rendeltAr[valasztott3], "Ft", "*")
    i=0
    osszear=0
    while i <= len(rendeltAr)-1:
        osszear+=rendeltAr[i]
        i+=1
    etlapmodul.szamlaSor("*", szamlahossz)
    etlapmodul.vegosszeg("*", "Fizetendő: ",osszear," Ft","*")
    etlapmodul.szamlaSor("*", szamlahossz)

