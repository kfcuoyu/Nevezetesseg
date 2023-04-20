#Beolvasás fájlból
f=open("lista.txt","r",encoding="utf-8")
kislista=[]
nagylista=[]
for sor in f:
    kislista=sor[:-1].split(";")
    nagylista.append(kislista)
f.close()

#Menürendszer
def menü():
    print("1 Nevezetességek listája")
    print("2 Választás a második személyek közül")
    print("3 Választás az órabérek közül")
    valasztott=input("Válaszd ki a sorszámot: ")
    return valasztott

#Nevezetességek listája
def feladat1():
    for i in range(0, len(nagylista)):
        print(nagylista[i][0])

#Személyek közötti választás
def feladat2():
    for i in range(0, len(nagylista)):
        print(i,nagylista[i][1])
    választás=int(input("Válassz országot: "))
    print("Hírességek az országban: ",nagylista[választás][0])

#Város választás
def feladat3():
    for i in range(0, len(nagylista)):
        print(i,nagylista[i][2])
    választás=int(input("Válassz országot: "))
    print("Hírességek a városban: ",nagylista[választás][0])
    print("Az országa: ",nagylista[választás][1])
        
#A választott menüpont sorszámát adjuk meg:    
sorszam=menü()
if sorszam=='1':
    feladat1()
elif sorszam=="2":
    feladat2()
elif sorszam=="3":
    feladat3()
else:
    print("Nem választottál menüpontot. Viszontlátásra")
    

