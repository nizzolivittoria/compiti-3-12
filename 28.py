print ("scrivi 0 per interrompere")
nomi = []
escursioni = []
contatore = 0

while True:
    città = input ("nome città: ")
    maxgradi = int (input ("temperatura max prefissata: "))
    mingradi = int (input ("temperatura min prefissata: "))
    escursione = (maxgradi - mingradi)
    nomi.append (città)
    escursioni.append (escursione)
    
    if città == "0" or maxgradi == 0 or mingradi == 0:
        for i in nomi:
            indice = nomi.index (i)
            maxgradi2 = int (input ("temperatura max oggi: "))
            mingradi2 = int (input ("temperatura min oggi: "))
            escursione2 = (maxgradi2 - mingradi2)

            if escursione2 > escursioni [indice]:
                contatore += 1
        break
print ("le città con un'escursione termica maggiore rispetto a quella prefissata sono", contatore)
