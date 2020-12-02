nomi = []
massima = []
minima = []
escursione = []
x = True
città = 0
maxtemperatura= 0
mintemperatura = 0
escursionetemperatura = 0
print("qual è il valore dell'escursione da prefissare?")
v = int(input())

while x == True:
    città += 1
    maxtemperatura += 1
    mintemperatura += 1
    escursionetemperatura += 0
    print("nome città", città,"? ")
    nomi2 = input()
    nomi.append(nomi2)
    print("temperatura massima di oggi a", nomi2,": ")
    temp1 = int(input())
    massima.append(temp1)
    print("temperatura minima di oggi a", nomi2,": ")
    temp2 = int(input())
    minima.append(temp2)
    escursionetermica = temp1 - temp2
    if escursionetermica > v:
         escursione.append(escursionetermica)
    else:
         pass
    abbandonare = int(input("se hai terminato premi 0 "))
    if abbandonare == 0:
        x = False
    else:
        pass
    


escursione.reverse()
print("il valore dell'escursione maggiore cambia rispetto a quello prefissato di :", escursione[:])
