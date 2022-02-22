from multiprocessing import Condition
from typing import Counter
import Gruppi_Cartelle
import Tabellone

class Regolamento:

    def __init__(self):
        self.vincite=0

    '''si '''
    def controllo_cartella_gruppo(self, gruppo, numero_estratto):
        k=0
        i=0
        #for j in range(3):
        exitcondition=False
        while exitcondition==False:
            '''in c sono salvati tutti gli indici che corrispondono alla posizione dell' numero estratto nel gruppo di cartelle'''
            c=gruppo.singola_cartella(i).cerca_numero(numero_estratto)
            if c[2] == True:
                k=i
                '''per convenzione si sostituisce al numero estratto il numero -1'''
                gruppo.singola_cartella(k).inserisci_numero(c[0],c[1],-1)
                exitcondition=True
                
            elif i >= len(gruppo.lista_cartelle)-1:
                exitcondition=True
            else:
                i+=1
        return k

    '''per ogni riga di una singola cartella si contano gli elementi == -1 e si prende come valore di una possibile vincita il valore massimo di questa lista di tre valori: counter_righe'''
    def verifica_vincite(self, cartella):
        counter_righe=[0,0,0]
        for i in range(3):
            c=cartella.conta_elementi_estratti_cartella(i)

            if   i == 0:
                counter_righe[0]=c
            elif i == 1:
                counter_righe[1]=c
            elif i == 2:
                counter_righe[2]=c
            else:
                pass

        m=0
        exitcondition = False
        vincita=max(counter_righe)

        '''per ogni riga di una cartella per cui sono presenti 5 valori si incremente di 1 il valore m, quando m sarà == 3 --> Tombola'''
        for i in counter_righe:
            if i == 5:
                m+=1

        if m==3:
            exitcondition = True

        return vincita, exitcondition

    











