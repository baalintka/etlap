import rendeles
import etlapmodul
etlap_hossz=60
szamlahossz=30
i = 0
osszeg=0
valasztas=1
valaszd=0

valasztasMasik=1
levesek = ["1-Húsleves", "2-Gyümölcsleves"]
levesAr = [1999, 1500]
desszertek=["1-Csokis fagyi ", "2-Macaron "]
dAr=[850, 650]
foetelek = ["1-Csirkepörkölt", "2-Mátrai borzaska"]
foetelAr = [2980, 4500]
rendelt = []
rendeltAr = []


etlapmodul.sor("*",etlap_hossz)
etlapmodul.cim("*","Étlap","*",etlap_hossz)
etlapmodul.sor("*",etlap_hossz)
etlapmodul.cim("*","# Levesek #","*",etlap_hossz)
for i in range(len(levesek)):
    etlapmodul.kaja("*",levesek[i],levesAr[i],"Ft","*")

etlapmodul.cim("*","# Főételek #","*",etlap_hossz)
for i in range(len(foetelek)):
    etlapmodul.kaja("*",foetelek[i],foetelAr[i],"Ft","*")

etlapmodul.cim("*","# Desszertek #","*",etlap_hossz)
for i in range(len(desszertek)):
    etlapmodul.kaja("*",desszertek[i],dAr[i],"Ft","*")

etlapmodul.sor("*",etlap_hossz)
etlapmodul.cim("*","Jó Étvágyat!","*",etlap_hossz)
etlapmodul.sor("*",etlap_hossz)

rendeles.rendelles(levesek,"Kér levest? (I/N):",levesAr,"levest")
rendeles.rendelles(foetelek,"Kér főételt? (I/N):",foetelAr,"főételt")
rendeles.rendelles(desszertek,"Kér desszertet? (I/N):",dAr,"desszertet")
rendeles.kiiras(rendelt,rendeltAr)



