import etlapmodul
import rendeles
import szamla
etlap_hossz=60
szamlahossz=30
i = 0


valasztasMasik=1
levesek = ["1-Húsleves", "2-Gyümölcsleves"]
levesAr = [1999, 1500]
foetelek = ["1-Csirkepörkölt", "2-Mátrai borzaska"]
foetelAr = [2980, 4500]
rendelt = []
rendeltAr = []
#while i < len(rendelt):

etlapmodul.sor("*",etlap_hossz)
etlapmodul.cim("*","Étlap","*",etlap_hossz)
etlapmodul.sor("*",etlap_hossz)
etlapmodul.cim("*","# Levesek #","*",etlap_hossz)
etlapmodul.kaja("*",levesek[0],levesAr[0],"Ft","*",etlap_hossz)
etlapmodul.kaja("*",levesek[1],levesAr[1],"Ft","*",etlap_hossz)
etlapmodul.cim("*","# Főételek #","*",etlap_hossz)
etlapmodul.kaja("*",foetelek[0],foetelAr[0],"Ft","*",etlap_hossz)
etlapmodul.kaja("*",foetelek[1],foetelAr[1],"Ft","*",etlap_hossz)
etlapmodul.sor("*",etlap_hossz)
etlapmodul.cim("*","Jó Étvágyat!","*",etlap_hossz)
etlapmodul.sor("*",etlap_hossz)

rendeles.leves(levesAr,foetelAr)
rendeles.szamlaSor("*",szamlahossz)

rendeles.szamlacim("*","Számla","*",szamlahossz)
rendeles.szamlaSor("*",szamlahossz)
rendeles.kertEtelekcim("*","Kért ételek: ","*",szamlahossz)
rendeles.valasztottEtel("*",levesek[0],levesAr[0],"*")