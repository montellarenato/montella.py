class ssc_napoli:

    # Attributi di Classe
    rosa = 27

    #Metodo costruttore
    def __init__(self,nome, cognome, anno, numero_maglia, stipendio):

        # Attributi di Istanza
        self.nome = nome
        self.cognome = cognome
        self.anno = anno
        self.numero_maglia = numero_maglia
        self.stipendio = stipendio
        
    #Metodo di tipo Get
    def scheda(self):
        return f'\nScheda "{self.nome}"\n Cognome: {self.cognome}\n Anno: {self.anno}\n Numero_maglia: {self.numero_maglia}\n Stipendio: {self.stipendio}' 
    
giocatore1 = ssc_napoli("Lorenzo","Insigne",1991, 24, 4.5)

giocatore2 = ssc_napoli("Victor","Osimhen",1998, 9, 4.5)

giocatore3 = ssc_napoli("Kalidou","koulibaly",1991, 26, 6)

print("Il tipo di variabile costruita è:")
print(giocatore1)
print(giocatore2)
print(giocatore3)

print("\nLa singola scheda è:")
print (giocatore1.scheda())
print (giocatore2.scheda())
print (giocatore3.scheda())

