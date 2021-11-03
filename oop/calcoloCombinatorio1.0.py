class calcComb():

    def __init__(self, stringa):

        self.__N = len(stringa)
        self.__stringa = stringa
        self.__listStringa = list(stringa)

    def get_stringa(self):
        return self.__stringa

    def get_listStringa(self):
        return self.__listStringa

    def setStringa(self,str):
        self.__N = len(stringa)
        self.__stringa = str
        self.__listStringa = list(stringa)

    def charRipetuti(self):

        word = list(parola) 
        caratteriripetuti={}
        nCaratteri = 0
        count = 0

        for i in word:
            if (i in caratteriripetuti): 
                caratteriripetuti[str(i)] += 1
        else:
            caratteriripetuti[str(i)] = 1 
        for i in caratteriripetuti:
            if caratteriripetuti[i]>1:
                count+=1
                nCaratteri += caratteriripetuti[i] 
                
    def combUtil(self,):
        f = open("C:/Users/Renato/OneDrive/Desktop/coding/oop/words.italian.txt", 'r')
        for riga in f:

           p=f.readline()

           if self.__stringa in p:
               print("è una parola italiana")
           #else:
               #print("non è una parola italiana")

    def fattoriale(n):
        '''
        implementare una qualunque versione della funzione fattoriale
        '''

    def coeffBinom(n, k):
        ''' 
        implementare la formula del coefficiente binomiale a partire dal fattoriale
        '''
        pass

parola= charRipetuti(str(input("inserisci una stringa")))
parola.charRipetuti()

