from tkinter.tix import Tree
import numpy as np
import random

class Cartella:

    def __init__(self,cartella=None,conta_colonne=None,conta_righe=None):
        '''creo una matrice 3X9 di zeri'''
        self.cartella = np.zeros((3,9))
        self.conta_colonne = np.zeros(9) 
        self.conta_righe = np.zeros(3)
    
    def elimina_cartella(self):
        self.cartella = np.zeros((3,9))
        self.conta_colonne = np.zeros(9) 
        self.conta_righe = np.zeros(3)
        
    def visualizza(self):
        '''restituisce la cartella e il numero di elementi su righe e colonne'''
        return self.cartella

    def visualizza_elemento(self,i,j):
        '''restituisce la cartella e il numero di elementi su righe e colonne'''
        return self.cartella[i,j]

    def aggiorna_conteggio(self,index_riga, index_colonna): 
        self.conta_righe[index_riga] += 1
        self.conta_colonne[index_colonna] += 1
        
    def inserisci_numero(self,index_riga,index_colonna,numero):
        self.cartella[index_riga,index_colonna] = numero
        self.aggiorna_conteggio(index_riga, index_colonna)
    
    def posizione_occupata(self,index_riga,index_colonna):
        if self.cartella[index_riga,index_colonna] != 0:
            return True
        else:
            return False

    '''restituisce in una lista gli indici delle posizioni libere per riga.'''
    def posizione_libera(self):
        index_riga=[]
        index_colonna=[]
        for i in range(3):
            for j in range(9):
                if self.cartella[i][j]==0:
                    index_riga.append(i)
                    index_colonna.append(j)
                else: 
                    pass
        return index_riga, index_colonna

    def posiszioni_occupate(self):
        index_riga=[]
        index_colonna=[]
        for i in range(3):
            for j in range(9):
                if self.cartella[i][j]!=0:
                    index_riga.append(i)
                    index_colonna.append(j)
                else: 
                    pass
        return index_riga, index_colonna
    
    '''restituisce in una lista gli indici delle posizioni libere per riga.'''
    def posizione_libera_colonna(self,i):
        index_colonna=[]
        for j in range(9):
            if self.cartella[i][j]==0:
                index_colonna.append(j)
            else: 
                pass
        return index_colonna


    def vincolo_righe(self,index_riga):
        if self.conta_righe[index_riga] == 5:
            return True
        else:
            return False
    
    def vincolo_colonne(self,index_colonna):
        if self.conta_colonne[index_colonna] >= 1:
            return True
        else:
            return False

    def vincoli_righe(self):
        c=0
        for i in range(3):
            if self.vincolo_righe(i):
                pass
            else:
                c+=1
        if c==0:
            return True
        else: 
            return False
    
    def vincoli_colonne(self):
        c=0
        for i in range(9):
            if self.vincolo_colonne(i):
                pass
            else:
                c+=1
        if c==0:
            return True
        else: 
            return False
        
    def vincoli(self):
        if (self.vincoli_colonne) and (self.vincoli_righe):
            return True
        else:
            return False 


    def genera_posizioni(self):
        self.elimina_cartella()
        for i in range(5):
            l=self.posizione_libera_colonna(0)
            c=random.choice(l)
            self.inserisci_numero(0,c,1)
        
        for i in range(5):
            l=self.posizione_libera_colonna(1)
            c=random.choice(l)
            self.inserisci_numero(1,c,1)

        for i in range(5):
            l=self.posizione_libera_colonna(2)
            c=random.choice(l)
            self.inserisci_numero(2,c,1)
                   
        return self.cartella

    def genera_posizioni_cartella(self):
        self.elimina_cartella()
        self.genera_posizioni()
        exitcond=False
        exitcond=self.vincoli_colonne()

        while exitcond==False:
            self.elimina_cartella()
            self.genera_posizioni()
            exitcond=self.vincoli_colonne()
        
        return self.cartella

    
    def assegna_numeri(self):
        
        decine={0:(1,2,3,4,5,6,7,8,9),
                1:(10,11,12,13,14,15,16,17,18,19),
                2:(20,21,22,23,24,25,26,27,28,29),
                3:(30,31,32,33,34,35,36,37,38,39),
                4:(40,41,42,43,44,45,46,47,48,49),
                5:(50,51,52,53,54,55,56,57,58,59),
                6:(60,61,62,63,64,65,66,67,68,69),
                7:(70,71,72,73,74,75,76,77,78,79),
                8:(80,81,82,83,84,85,86,87,88,89,90)}
        
        self.elimina_cartella()
        self.genera_posizioni_cartella()
        index=self.posiszioni_occupate()[1]
        l=[]
        exitcond=False
        for i in range(3):
            for j in range(9):
                if self.posizione_occupata(i,j):
                    k=random.randint(0,len(decine[j])-1)
                    n=decine[j][k]
                    
                    while exitcond==False:
                        if n in l:
                            k=random.randint(0,len(decine[j])-1)
                            n=decine[j][k]
                            
                        else:
                            exitcond=True
      
                    exitcond=False
                    l.append(n)
                    self.inserisci_numero(i,j,n)
                    

        return self.cartella


    '''
    
    '''