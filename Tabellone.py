import numpy as np
'''La classe tabellone conterrà 6 cartelle e tutti i numeri da 1 a 90 ordinati in maniera crescente.
    Tuttavia per migliorare la visualizzazione del tabellone saranno utilizzate coppie di cartelle adiacenti'''
class Tabellone():

    def __init__(self):
        
        self.cartellone=[]
        self.cartellone_sx=[]
        self.cartellone_dx=[]
        self.cartellone_dx_sx=[]

        '''Il tabellone è composto da 6 cartelle 5X3, in cui ogni riga è composta da sequenze ordinate di numeri
        Le cartelle nel tabellone reale vangono disposte a coppie una accanto all'altra e pertanto si avranno 3 cartelle sul lato sinistro e 3 cartelle sul lato destro.
        '''

        c=[]
        for i in range(5):      
            l=len(range(i))+1 
            c.append(l) # alla fine la lista c avrà i seguenti valori: 1 2 3 4 5

        c1=[]
        for i in range(5):      
            l=c[i]+5
            c1.append(l) # 6 7 8 9 10

        c2=[]
        for i in range(5):      
            l=c[i]+10
            c2.append(l) # 11 12 13 14 15

        c3=[]
        for i in range(5):      
            l=c[i]+15
            c3.append(l)  # 16 17 18 19 20

        c4=[]
        for i in range(5):      
            l=c[i]+20
            c4.append(l) # 21 22 23 24 25

        c5=[]
        for i in range(5):      
            l=c[i]+25
            c5.append(l)

        c6=[]
        for i in range(5):      
            l=c[i]+30
            c6.append(l)

        c7=[]
        for i in range(5):      
            l=c[i]+35
            c7.append(l)

        c8=[]
        for i in range(5):      
            l=c[i]+40
            c8.append(l)

        c9=[]
        for i in range(5):      
            l=c[i]+45
            c9.append(l)

        c10=[]
        for i in range(5):      
            l=c[i]+50
            c10.append(l)

        c11=[]
        for i in range(5):      
            l=c[i]+55
            c11.append(l)

        c12=[]
        for i in range(5):      
            l=c[i]+60
            c12.append(l)

        c13=[]
        for i in range(5):      
            l=c[i]+65
            c13.append(l)

        c14=[]
        for i in range(5):      
            l=c[i]+70
            c14.append(l)

        c15=[]
        for i in range(5):      
            l=c[i]+75
            c15.append(l)

        c16=[]
        for i in range(5):      
            l=c[i]+80
            c16.append(l)

        c17=[]
        for i in range(5):      
            l=c[i]+85
            c17.append(l)

        '''Viene realizzate la prima cartella del tabellone che ha i segenti valori:
        1 2 3 4 5
        11 12 13 14 15
        21 22 23 24 25
        '''
        'Cartella in alto a sinistra'
        cartella_tabellone1=np.zeros((3,5))
        cartella_tabellone1[0]=c #1,2,3,4,5
        cartella_tabellone1[1]=c2 #11,12,13,14,15
        cartella_tabellone1[2]=c4 #21,22,23,24,25
        'Analogamente si procede per le altre cartelle del tabellone'
        'Cartella in alto a destra del tabellone'
        cartella_tabellone2=np.zeros((3,5))
        cartella_tabellone2[0]=c1
        cartella_tabellone2[1]=c3
        cartella_tabellone2[2]=c5 
        'Si procede valutando la cartella centrale a sinistra del tabellone e così via per le altre'
        cartella_tabellone3=np.zeros((3,5))
        cartella_tabellone3[0]=c6
        cartella_tabellone3[1]=c8
        cartella_tabellone3[2]=c10

        cartella_tabellone4=np.zeros((3,5))
        cartella_tabellone4[0]=c7
        cartella_tabellone4[1]=c9
        cartella_tabellone4[2]=c11

        cartella_tabellone5=np.zeros((3,5))
        cartella_tabellone5[0]=c12
        cartella_tabellone5[1]=c14
        cartella_tabellone5[2]=c16

        cartella_tabellone6=np.zeros((3,5))
        cartella_tabellone6[0]=c13
        cartella_tabellone6[1]=c15
        cartella_tabellone6[2]=c17 

        '''Per permettere una visualizzazione migliore del tabellone si affiancano le cartelle adiacenti, in modo da formare 3 coppie di cartelle'''
        coppia1=np.zeros((3,10))
        coppia1[0]=c+c1
        coppia1[1]=c2+c3
        coppia1[2]=c4+c5

        coppia2=np.zeros((3,10))
        coppia2[0]=c6+c7
        coppia2[1]=c8+c9
        coppia2[2]=c10+c11

        coppia3=np.zeros((3,10))
        coppia3[0]=c12+c13
        coppia3[1]=c14+c15
        coppia3[2]=c16+c17

        '''Si realizzano delle liste contenenti tutte le cartelle del cartellone per permettere agevolmente una verifica dei numeri estratti.
        Nel cartellone sx avremo le cartelle situate sulla sinistra del tabellone, lo stesso per quella di destra'''

        self.cartellone_sx.append(cartella_tabellone1)
        self.cartellone_dx.append(cartella_tabellone2)
        self.cartellone_sx.append(cartella_tabellone3)
        self.cartellone_dx.append(cartella_tabellone4)
        self.cartellone_sx.append(cartella_tabellone5)
        self.cartellone_dx.append(cartella_tabellone6)
        
        '''Cartellone_dx_sx contiene tutte le cartelle del tabellone'''
        self.cartellone_dx_sx=self.cartellone_sx+self.cartellone_dx

        '''Si realizzano tre liste contententi ciascuna 2 cartelle per permettere una visualizzazione migliore'''
        self.cartellone.append(coppia1)
        self.cartellone.append(coppia2)
        self.cartellone.append(coppia3)

    '''Metodo che permette la visualizzazione di un singolo elemento del tabellone noti gli indici di posizione
        NB: poichè risulta che il cartellone sia una lista di matrici 3X5 vanno specificati tre indici:
        - pos_cartella indica la cartella a cui ci riferiamo 
        - index_riga e index_colonna fanno riferimento agli indici di posizione all'interno della matrice specificata.
    '''
    def visualizza_elemento_tabellone(self,pos_cartella,index_riga,index_colonna):
        return self.cartellone[pos_cartella][index_riga][index_colonna]

    '''Effettua la stampa del tabellone'''   
    def visualizza_tabellone(self):
        for p in range(3):
            for r in range(3):
                print('[ ',end='')
                for c in range(10):
                    if self.visualizza_elemento_tabellone(p,r,c) == 0:
                        print(' ',end=' ')
                    elif self.visualizza_elemento_tabellone(p,r,c) == -1:
                        print('*',end=' ')
                    else:
                        print(int(self.visualizza_elemento_tabellone(p,r,c)),end=' ')
                print(']')
            
            pass
        
    '''Dato in ingresso l'indice i della cartella nel tab_sx viene restituita tale cartella'''
    def singola_cartella_tab_sx(self,i):
        return self.cartellone_sx[i]

    '''Analogo al precedente per le cartelle di dx del tabellone'''
    def singola_cartella_tab_dx(self,i):
        return self.cartellone_dx[i]

    '''Dato in ingresso l'indice della cartella iesima , questa volta i=(0,5) mi restituisce la cartella associata a quell'indice'''
    def singola_cartella_tab_dx_sx(self,i):
        return self.cartellone_dx_sx[i]

    '''Dato in ingresso un certo numero, mi viene restituito l'indice k della cartella in cui trovo n e gli indici di posizione nella matrice'''
    def pos_numero_estratto(self,n):
        for i in range(3):
            for j in range(5):
                for k in range(6):
                    if self.singola_cartella_tab_dx_sx(k)[i][j]==n:
                        return k,i,j

    '''Dati in ingresso gli stessi parametri che erano in uscita per pos numero estratto, sostitusico -1 nella posizione individuata dagli indici i,j nella cartella k'''
    def sostituisci_numero(self, k, i, j):
        self.singola_cartella_tab_dx_sx(k)[i][j]=-1

    
    '''Metodo analogo a pos numero estratto, solamente che mi viene restituita la kesima cartella con k=(0,1,2), avendo considerato per self.cartellone le coppie di cartelle, e degli indici i,j
    diversi da quelli ottenuti per pos numero estratto'''
    def pos_numero_estratto_tabellone(self,n):
        for i in range(3):
            for j in range(10):
                for k in range(3):
                    if self.cartellone[k][i][j]==n:
                        return k,i,j
    
    '''Dati in ingresso k,i,j sostituisco -1 al posto del numero presente negli indici specificati'''
    def sostituisci_numero_tabellone(self,k,i,j):
        self.cartellone[k][i][j]=-1

    '''Dati in ingresso la cartella k, con k=(0,6), e la riga iesima, vado a verificare quante volte compare -1 per ognmi singola riga.
    Tale metodo sarà utilizzato per verificare le vincite del tabellone'''
    def conta_elementi_estratti_tabellone(self,k,i):
        c=0
        for j in range(5):
            if self.singola_cartella_tab_dx_sx(k)[i][j]==-1:
                c+=1
            else:
                pass

        return c
        
                                    

    

