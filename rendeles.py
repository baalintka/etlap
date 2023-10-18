
def leves(levesAr,foetelAr):

    valasztas=0
    valasz = input("Kér levest? (I/N): ").lower()
    if valasz == "i":
        print("Levesek:")
        print("1-Húsleves\n""2-Gyümölcsleves\n")
        valasz = int(input("1 vagy 2?"))
        if valasz == 1:

            valasztas=0;
            print(valasztas)
        else:
            levesosszeg = levesAr[1];
            print("valami")
    else:
        foetel(foetelAr)

    foetel(foetelAr)



def foetel(foetelAr):
    valasz = input("Kér főételt? (I/N): ").lower()
    if valasz == "i":
        print("Fő ételek:")
        print("1-Csirkepörkölt\n2-Mátrai borzaska")

        valasz = int(input("1 vagy 2? "))
        if valasz == 1:
            print("hmm")
        else:
            print("ehe")


def szamlaSor(jel,db):
    print(jel*db)

def szamlacim(jel,szoveg,jel2,szamlahossz):
    hossz=szamlahossz-(len(jel)+len(jel2))
    print(f"{jel}{szoveg:^{hossz}}{jel2}")
def kertEtelekcim(jel,szoveg,jel2,szamlahossz):
    print(f"{jel:<5}{szoveg}{jel2:>12}")
def valasztottEtel(jel,szoveg,ar,jel2):
    if valasztas==0:
        print(f"{jel:<5}{szoveg }{ar}{jel2:>12}")