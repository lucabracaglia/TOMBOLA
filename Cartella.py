import numpy as np
import random

class Cartella:

    '''Viene creata la classe Cartella: ogni cartella sarà rappresentata come una matrice di 3 righe e 9 colonne, inizialmente 
    con tutti valori 0, che poi verrà popolata seguendo i vincoli richiesti dal problema.'''

    def __init__(self,cartella=None,conta_colonne=None,conta_righe=None):
        '''Creo una matrice 3X9 di zeri'''
        self.cartella = np.zeros((3,9))
        self.conta_colonne = np.zeros(9) 
        self.conta_righe = np.zeros(3)

    '''Tale metodo permette di azzerare i contatori, nel caso si siano effettuate sulla cartella operazioni superflue'''
    def azzera_contatori(self):
        self.conta_colonne = np.zeros(9) 
        self.conta_righe = np.zeros(3)

    '''Tale metodo rende nuovamente la cartella una matrice di zeri e azzera i contatori'''
    def elimina_cartella(self):
        self.cartella = np.zeros((3,9))
        self.azzera_contatori()
        
    '''Tale metodo permette la visualizzazione di una cartella'''
    def visualizza(self):
        return self.cartella

    '''Specificati gli indici di posizione nella cartella in input viene restituito in output l'elemento situato in quella data posizione'''
    def visualizza_elemento(self,i,j):
        return self.cartella[i,j]
    
    '''Permette la visualizzazione in formato migliore della cartelle (Al posto degli zeri presenti nella cartella viene inserito un '--', se il numero presente nella cartella è -1(numero estratto)
    viene inserito :'*', altrimenti viene visualizzato il numero intero)'''
    def stampa(self):
        for r in range(3):
            print('[ ',end='')
            for c in range(9):
                if self.visualizza_elemento(r,c) == 0:
                    print('--',end=' ')
                elif self.visualizza_elemento(r,c) == -1:
                    print('*',end=' ')
                else:
                    print(int(self.visualizza_elemento(r,c)),end=' ')
            print(']')
        print('\n')
        pass
    
    '''Dato in input l'indice associato alla colonna della cartella, viene restituito in output il numero di elementi su tale colonna'''
    def conta_elementi_colonne(self, index_colonna):
        return self.conta_colonne[index_colonna]
    
    '''Dato in  input l'indice associato alla riga viene restituito in output il numero di elementi c estratti su tale riga'''
    def conta_elementi_estratti_cartella(self,i):
        c=0
        for j in range(9):
            if self.cartella[i][j]==-1:
                c+=1
            else:
                pass
        return c

    '''Noti in input gli indici di posizione della cartella, tale metodo permette di aggiornare il conteggio sulle righe e sulle colonne della matrice quando viene inserito un numero'''
    def aumenta_conteggio(self,index_riga, index_colonna): 
        self.conta_righe[index_riga] += 1
        self.conta_colonne[index_colonna] += 1
    
    '''Analogo discorso del metodo precedente, serve per decrementare il conteggio'''
    def riduci_conteggio(self,index_riga, index_colonna):
        self.conta_righe[index_riga] -= 1
        self.conta_colonne[index_colonna] -= 1

    '''Tale metodo permette di inserire un numero specificato negli indici di posizione prestabiliti della cartella'''    
    def inserisci_numero(self,index_riga,index_colonna,numero):
        self.cartella[index_riga,index_colonna] = numero
        self.aumenta_conteggio(index_riga, index_colonna)
    
    '''Metodo che permette di posizionare uno 0 negli indici di posizione desiderata'''  
    def elimina_numero(self,index_riga,index_colonna):
        self.cartella[index_riga,index_colonna] = 0
        self.riduci_conteggio(index_riga, index_colonna)
    
    '''Dato un numero n in input tale metodo restituisce gli indici di posizione di tale numero nel caso in cui sia presente nella cartella'''
    def cerca_numero(self,n):
        index_r=[]
        index_c=[]
        for i in range(3):
            for j in range(9):
                if self.cartella[i][j]==n:
                   index_r.append(i)
                   index_c.append(j)
                else:
                    pass
        if len(index_r)>0 and len(index_c)>0:
            return index_r, index_c, True
        
        else:
            return index_r, index_c, False
            

    '''se nella matrice è presente il numero 0 è considerate posizione libera, perciò se l' elemento corrispondente è diverso da zero --> True'''
    def posizione_occupata(self,index_riga,index_colonna):
        if self.cartella[index_riga,index_colonna] != 0:
            return True
        else:
            return False


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

    '''effettuo delle modifica casuali alle posizioni della cartella per permettere la generazione di Gruppi_Cartella'''
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

                        #elimino dal dizionario 'decine' i numeri già usati
                        for q in range(9):
                            for w in range(len(decine[q])):
                                if (decine[q][w-1]==n):
                                    del decine[q][w-1]


                        
        return self.cartella, decine
