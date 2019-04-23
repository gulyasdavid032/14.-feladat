#Írj egy programot, ami a parancssori argumentumként kap bemenetként egy természetes
#számot és egy txt fájlba beírja az összes páratlan háromszög számot, ami kisebb, mint a
#megadott szám.
import sys
try:
    fout=open("output2.txt",'w')
    ls=[]
    sys.argv[1]=int(sys.argv[1])
    for i in range(1,sys.argv[1]):
        s=(i*(i+1))/2
        s=int(s)
        if s<sys.argv[1] and s%2!=0:
            ls.append(s)
            a=str(ls)
    fout.write(a)
    print("A számok az output2.txt -ben találhatóak")
except IndexError:
    print("Ellenőrizd az indexeket!")