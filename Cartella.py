from operator import index
from tkinter.tix import Tree
import numpy as np
import random

class Cartella:

    def __init__(self,cartella=None,conta_colonne=None,conta_righe=None):
        '''creo una matrice 3X9 di zeri'''
        self.cartella = np.zeros((3,9))
        self.conta_colonne = np.zeros(9) 
        self.conta_righe = np.zeros(3)

    '''azzera i contatori, nel caso si siano effettuate sulla cartella operazioni superflue'''
    def azzera_contatori(self):
        self.conta_colonne = np.zeros(9) 
        self.conta_righe = np.zeros(3)

    '''rende nuovamente la cartella una matrice di zeri e azzera i contatori'''
    def elimina_cartella(self):
        self.cartella = np.zeros((3,9))
        self.azzera_contatori()
        
    '''permette la visualizzazione di una cartella'''
    def visualizza(self):
        return self.cartella

    '''specificati gli indici permette di visualizzare l'elemtìnto corrispondente nella cartella'''
    def visualizza_elemento(self,i,j):
        return self.cartella[i,j]
    
    '''restituisce il numero di elementi sulla colonna specificata dall'indice'''
    def conta_elementi_colonne(self, index_colonna):
        return self.conta_colonne[index_colonna]

    '''restituisce il numero di elementi sulla riga specificata dall'indice'''
    def conta_elementi_rige(self, index_riga):
        return self.conta_righe[index_riga]

    '''serve per aumentare i contatori riga colonna quando verrà aggiunto un numero'''
    def aumenta_conteggio(self,index_riga, index_colonna): 
        self.conta_righe[index_riga] += 1
        self.conta_colonne[index_colonna] += 1
    
    '''serve per ridurre i contatori riga colonna quando verrà sottratto un numero'''
    def riduci_conteggio(self,index_riga, index_colonna):
        self.conta_righe[index_riga] -= 1
        self.conta_colonne[index_colonna] -= 1

    '''permette di inserire un numero specificati gli indici di dove si vuole inserire'''    
    def inserisci_numero(self,index_riga,index_colonna,numero):
        self.cartella[index_riga,index_colonna] = numero
        self.aumenta_conteggio(index_riga, index_colonna)
    
    '''permette di eliminare un numero specificati gli indici di dove si vuole eliminare'''  
    def elimina_numero(self,index_riga,index_colonna):
        self.cartella[index_riga,index_colonna] = 0
        self.riduci_conteggio(index_riga, index_colonna)

    '''se nella matrice è presente il numero 0 è considerate posizione libera, perciò se l' elemento corrispondente è diverso da zero --> True'''
    def posizione_occupata(self,index_riga,index_colonna):
        if self.cartella[index_riga,index_colonna] != 0:
            return True
        else:
            return False

    '''restituisce in due liste di indici delle posizioni libere per riga e collonna.'''
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

    '''restituisce due liste di indici delle posizioni occupate nella matrice'''
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

    '''se su una riga della cartella ci sono 5 numeri ---> True'''
    def vincolo_righe(self,index_riga):
        if self.conta_righe[index_riga] == 5:
            return True
        else:
            return False

    '''se è presente almeno un elemento sulla colonna ---> True'''
    def vincolo_colonne(self,index_colonna):
        if self.conta_colonne[index_colonna] >= 1:
            return True
        else:
            return False
    
    '''verifica che nella cartella siano rispettati per ogni righa i vincoli riga (esattamente 5 elementi per riga)'''
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
    
    '''verifica che nella cartella siano rispettati per ogni righa i vincoli riga (alemeno 1 elemento per colonna)'''
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

    '''verifica contemporaneamente che una cartella rispetti i vincoli riga e colonna'''    
    def vincoli(self):
        if (self.vincoli_colonne()) and (self.vincoli_righe()):
            return True
        else:
            return False

    def altera_posizione_righa(self,index_riga):
        '''non viene alterata la posizione dell ultima colonna per garantire che la posizione del 90 resti invariata'''
        eliminare=random.randint(1,7)
        inserire=random.randint(1,7)
        numero=0

        if self.posizione_occupata(index_riga,eliminare): #verifico che la posizione da eliminare sia effettivamente occupate
            if self.posizione_occupata(index_riga,inserire): #verifico che la posizione che voglio occupare non sia già occupata
                pass
            else:
                numero=self.visualizza_elemento(index_riga,eliminare)
                self.elimina_numero(index_riga,eliminare)
                self.inserisci_numero(index_riga,inserire,1)
        else:
            pass
        
        if self.vincoli(): #verifico che la nuova configurazione rispetti i vincoli
             return self.cartella
        else:   #altrimenti ripristino la situazione precedente
            self.elimina_numero(index_riga,inserire)
            self.inserisci_numero(index_riga,eliminare,numero)
            pass

    '''inserisce in posizioni casuali il numero 1, forzando che su ogni riga ce ne siano 5'''
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

    '''verifica che siano rispettati i vincoli richiesti (in particolare forzando che siano 5 elementi per riga 
        va verificato che sia rispettato i vincoli colonna)'''
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
    
    '''genera posizioni cartelle in cui l'ultima posizione non è occupata (ci deve andare il 90 una sola volta)'''
    def verifica_pos_90(self):
        self.elimina_cartella()
        self.genera_posizioni_cartella()
        exitcond=False
        exitcond=self.posizione_occupata(2,8)

        while exitcond==True:
            self.elimina_cartella()
            self.genera_posizioni_cartella()
            exitcond=self.posizione_occupata(2,8)
        
        return self.cartella
    
    '''genera posizioni cartelle in cui l'ultima posizione è occupata (ci deve andare il 90 una sola volta)'''
    def genera90(self):
        self.elimina_cartella()
        self.genera_posizioni_cartella()
        exitcond=True
        exitcond=self.posizione_occupata(2,8)

        while exitcond==False:
            self.elimina_cartella()
            self.genera_posizioni_cartella()
            exitcond=self.posizione_occupata(2,8)
        
        return self.cartella



    '''date le posizioni si assegano dei numeri casuali alla cartella, prestando attenzione al fatto che:
    sulla prima colonna ci siano i numeri da 1 a 9
    sulla seconda da 10 a 19
    sulla terza da 20 a 29
    sulla quarta 30 39 
    sulla quinta 40 49
    sulla sesta 50 59
    sulla settima 60 69
    sulla ottava 70 79 
    sulla nona 80 89 (90 escluso che viene trattato separatamente)'''

    
    
    '''funzione a cui si passa il dizionario 'decine' a cui verranno tolti i numeri già utilizzati, evitando cosi ripetizioni'''
    def assegna_numeri_cartella(self, decine):

        l=[]
        exitcond=False
        for i in range(3):
            for j in range(9):
                if self.posizione_occupata(i,j):
                    if i==2 and j==8: # assicuriamo che l'ultima posizione si occupata dal 90
                        n=90
                        self.inserisci_numero(i,j,n)
                        l.append(n)
                        del decine[8][-1]
                    else:
                        k=random.randint(0,len(decine[j])-1)
                        n=decine[j][k]
                        
                        while exitcond==False:
                            if n in l:
                                k=random.randint(0,len(decine[j])-1)
                                n=decine[j][k]
                                
                            else:
                                exitcond=True
        
                        exitcond=False
                        self.inserisci_numero(i,j,n)
                        l.append(n)

                        #elimino dal dizionario 'decine' i numeri estratti
                        for q in range(9):
                            for w in range(len(decine[q])):
                                if (decine[q][w-1]==n):
                                    del decine[q][w-1]


                        
        return self.cartella, decine
