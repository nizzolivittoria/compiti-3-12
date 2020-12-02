l = int (input ("inserisci numero cifre binarie"))
totale= 0
for n in range (l):
    numero = int (input ("elenca partendo da destra le cifre"))
    valore = (numero*2**n)
    totale += valore

print (totale)
