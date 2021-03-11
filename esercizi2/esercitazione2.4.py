from random import randint

f = open("dati.txt", 'w')

dati=""

for riga in range(100):

    dati = dati + str(randint(1,100)) + "\n"

print(dati)

f.write(dati)

f.close()
