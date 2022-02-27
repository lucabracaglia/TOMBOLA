import random
import Cartella

class Gruppi:

    '''
    Si deve generare un gruppo di sei cartelle diverse, senza ripetizioni di numeri.
    
    L'idea che caratterizza le prossime funzioni è la seguente:
    poichè è necessario che la somma degli elementi sulle colonne di un gruppo sia sulla prima colonna pari a 9 (sulla prima colonna ci vanno i numeri da 1 a 9 e perciò è necessario che la somma degli elementi sia pari a 9).
    La somma degli elementi dell' ultima colonna invece è 11 (80 a 90 inclusi) 
    Va generato un gruppo che rispetta la condizione sulla prima e sull'ultima colonna, successivamente si effettua un controllo sul gruppo creato e si verifica se per ogni altra colonna la somma sia pari a 10.
    se non è così si alternao casualmente le cartelle finchè tali vincoli non sono rispettati.
    '''

    def __init__(self,numero_max_cartelle=7):
        '''si inizzializza una lista vuota che conterrà sei oggetti --> Cartella: matrici 3X9'''
        self.lista_cartelle=[]
        self.numero_max_cartelle=numero_max_cartelle
        for i in range(0,6):
            cartella= Cartella.Cartella()
            self.lista_cartelle.append(cartella)
    
    '''dato l'indice della cartella desiderata ne permette la selezione'''
    def singola_cartella(self,i):
        return self.lista_cartelle[i]
    
    '''tale metodo fa si che la prima cartella del gruppo sia quella con il 90 nella posizione individuata dagli indici(2,8)
        e verifica che la somma degli elementi sulla prima colonna sia uguale a 9 (condition == True)'''
    def verifica_posizioni_gruppo_prima_colonna(self):
        self.singola_cartella(0).genera90()
        for i in range(1,6):
            self.singola_cartella(i).verifica_pos_90()

        l=[]
        for k in range(6):
            somma_elementi_colonna = 0
            somma_elementi_colonna = somma_elementi_colonna + self.singola_cartella(k).conta_elementi_colonne(0)
            l.append(somma_elementi_colonna)
            c=sum(l)
            if c==9:
                condition = True
            else:
                condition=False 

        return condition

    '''tale metodo garantisce che il gruppo creato abbia 9 elementi sulla prima colonna'''
    def genera_gruppo1(self):
        exitcondition = self.verifica_posizioni_gruppo_prima_colonna()
        while exitcondition == False:
            exitcondition=self.verifica_posizioni_gruppo_prima_colonna()
            
        return self.lista_cartelle
    
    '''dato il gruppo di cartelle che rispetta la condizione sulla prima colonna si impone analogamente che venga rispettata la condizione sull' ultima colonna (11 elementi totali tra le sei cartelle del gruppo)'''
    def verifica_posizioni_gruppo_ultima_colonna(self):
        self.genera_gruppo1()
        l=[]
        for k in range(6):
            somma_elementi_colonna = 0
            somma_elementi_colonna = somma_elementi_colonna + self.singola_cartella(k).conta_elementi_colonne(8)
            l.append(somma_elementi_colonna)
            c=sum(l)
            if c==11:
                condition = True
            else:
                condition=False 

        return condition
    
    '''si genera il gruppo che rispetta anche la condizione sull' ultima cartella'''
    def genera_gruppo2(self):
        exitcondition = self.verifica_posizioni_gruppo_ultima_colonna()
        while exitcondition == False:
            exitcondition=self.verifica_posizioni_gruppo_ultima_colonna()
            
        return self.lista_cartelle


    '''il metodo verifica che ciascuna colonna: dalla 2 alla 8 dell' intero gruppo siano formate esattamente da 10 elementi'''
    def conta_colonne_gruppo(self):
        
        l1=[]
        l2=[]
        col_non=[]
        col10=0
        for j in range(1,8):
            l1=[]
            for i in self.lista_cartelle:
                somma_elementi_colonna = 0
                somma_elementi_colonna = somma_elementi_colonna + i.conta_elementi_colonne(j)
                l1.append(somma_elementi_colonna)
            c=sum(l1)
            l2.append(c)

        for i in range(len(l2)):
            if l2[i]==10:
                col10+=1
            else:
                col_non.append(i)
        
        if col10!=7:
            condition=False
        else:
            condition=True

        return condition

    '''tale metodo effettua delle modifiche casuali sugli elementi delle cartelle'''
    def permuta_gruppo(self):
        i=random.randint(1,5)
        j=random.randint(0,2)
        self.singola_cartella(i).altera_posizione_righa(j)
        return self.lista_cartelle

    '''finchè non si rispettano tutti i vincoli cartella si ripetono delle permutazioni casuali'''
    def genera_posizioni_gruppo(self):
        self.genera_gruppo2() #genera un gruppo in cui la somma degli elementi sulla prima colonna è pari a 6
        exitcondition = self.conta_colonne_gruppo()
        #se il gruppo generato (genera_gruppo1) non rispetta le altre condizioni exitcondition == False
        while exitcondition == False:
            self.permuta_gruppo()
            exitcondition=self.conta_colonne_gruppo()
            
        return self.lista_cartelle


    '''stabilito un gruppo di cartelle che rispetta i requisiti si assegnano i numeri ad ogni posizione, assicurando che un numero non venga ripetuto all' interno del gruppo.'''
    def assegna_numeri(self):
        decine={0:[1,2,3,4,5,6,7,8,9],
                1:[10,11,12,13,14,15,16,17,18,19],
                2:[20,21,22,23,24,25,26,27,28,29],
                3:[30,31,32,33,34,35,36,37,38,39],
                4:[40,41,42,43,44,45,46,47,48,49],
                5:[50,51,52,53,54,55,56,57,58,59],
                6:[60,61,62,63,64,65,66,67,68,69],
                7:[70,71,72,73,74,75,76,77,78,79],
                8:[80,81,82,83,84,85,86,87,88,89,90]}

        self.genera_posizioni_gruppo()
        for i in range(6):
            #si azzerano i contatori poichè la generazione della posizione (che avviene con l'inserimento del numero 1), altera il reale numero di elementi riga/colonna
            self.singola_cartella(i).azzera_contatori()
            #aggiorno il dizionario, sottraendo i numeri già estratti.
            decine = self.singola_cartella(i).assegna_numeri_cartella(decine)[1]
            
        return self.lista_cartelle #l'output finale è un gruppo di 6 cartelle contente tutti i numeri da 1 a 90 senza ripetizioni che rispetta i vincoli cartella (somma elementi sulle righe = 5 e che ogni colonna di ogni cartella abbbia almento un numero)

        
        

    
    
