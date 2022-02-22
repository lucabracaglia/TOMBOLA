import Cartella
import Gruppi_Cartelle
import random

class Giocatori:
    def __init__(self,n):
        self.numero_cartelle=n
        self.lista_cartelle=[]

    def cartelle_assegnate(self):
        return self.lista_cartelle

    '''permette di selezionare una determinata cartella associata al giocatore'''
    def visualizza_cartella(self,i):
        return self.lista_cartelle[i]


    def crea_cartella(self):
        cartella=Cartella.Cartella()
        for i in range(self.numero_giocatori):
            print('----')
            self.lista_cartelle.append(cartella)
            return self.lista_cartelle

    '''ad ogni giocatore vengono assegnate n = self.numero_cartelle cartelle dal gruppo di cartelle generato casualemnte 
        da gruppo.assegna_numeri'''
    def assegnazione(self):
        gruppo=Gruppi_Cartelle.Gruppi()
        gruppo.assegna_numeri()
        for i in range(self.numero_cartelle):
            self.lista_cartelle.append(gruppo.singola_cartella(i))

        return self.lista_cartelle

    