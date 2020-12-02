binario = []
num = int (input ("inserisci numero naturale: "))
while True:

    rapporto= int (num/2)
    resto = num % 2
    if resto == 1:
        binario.append (1)
    else:
        binario.append (0)
    num = rapporto

    if rapporto == 0:
        break

binario.reverse ()
print (binario)
