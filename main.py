import Utils
import Tabellone
import Giocatori
import Regolamento

try:
    parser = Utils.initialize_parser()
    n_giocatori=parser.g
    n_cartelle=parser.n
    if (Utils.numero_giocatori(n_giocatori)) and (Utils.confronta_lista_cartelle(n_giocatori,n_cartelle) and Utils.numero_cartelle(n_cartelle)): #si verifica che i parametri passati dall utente siano conformi con le prerogative del programma
        '''nella fase preliminare del gioco si assegnano le cartelle ai giocatori'''
        lista_giocatori=[]
        for i in range(n_giocatori):
            giocatore=Giocatori.Giocatori(n_cartelle[i]) #ad ogni giocatore si fa corrispondere il numero di cartelle scelto
            giocatore.assegnazione()
            lista_giocatori.append(giocatore)
        
        

        tabellone=Tabellone.Tabellone() #istanzo il tabellone

        '''permette le visualizzazione delle cartelle assegnate ai vari giocatori'''
        for i in range(len(lista_giocatori)):
            n=n_cartelle[i]
            print('Giocatore ', i+1)
            for j in range(n):
                lista_giocatori[i].visualizza_cartella(j).stampa()

        regole=Regolamento.Regolamento() #istanzo il regolamento

        input("iniziare il gioco della tombola?")

        estratti = list() #lista che contiene tutti i numeri estratti
        utlimi_estratti = list() #lista che contiene unicamente gli ultimi 6 numeri estratti
        exitcond=False # verrà trasformata in True quando uno dei giocatori effettua la tombola
        vincite=[0,1] #il riconoscimento della vincita si basa sull' numero di '-1' presenti su una cartella, vanno esclusi i casi in cui ci siano zero '-1' e un solo '-1' in quanto non vincenti 

        while exitcond == False:
            estratti= Utils.estrazione(estratti)
            if len(utlimi_estratti)<=5: # finchè la lista numeri estratti è minore più piccola di 6 continuo aggiungo l' ultimo numero estratto
                utlimi_estratti.append(estratti[-1])
            else:
                utlimi_estratti.pop(0) # nel caso la lista sia già composta da 6 elementi devo eliminare il primo elemento della lista prima di aggiungerne una nuovo
                utlimi_estratti.append(estratti[-1])
            
            print('gli ultimi estratti sono:',utlimi_estratti,'\n\n')

            '''ad ogni estrazione si verifica se in tutte le cartelle è presente tale numere e in caso lo si sostituisce con un -1 (per convenzione)'''
            for i in range(len(lista_giocatori)):
                n=n_cartelle[i]
                for j in range(n):
                    '''si effettua una ricerca dell'ultimo numero estratto all'interno delle cartelle assegnate ai vari giocatori e come risultato se ne ricavano gli indici di posizione'''
                    indici=lista_giocatori[i].visualizza_cartella(j).cerca_numero(estratti[-1])

                    if len(indici[0]) !=0: # se esistono tali indici di posizione e quindi il numero è presente all intero di una tale cartella, si usano gli indici per sostituire in tale cartella il -1
                        lista_giocatori[i].visualizza_cartella(j).inserisci_numero(indici[0],indici[1],-1)
                    else:
                        pass

            '''analogamente si fa per il tabellone: si ricavano gli indici di posizione del numeri estratto e si usano per sostituirli con un '-1' 
            NB: sono necessari 3 indici il primo per specificare quale la cartella in cui si trova il numero estratto, i restanti per individuare all' interno della cartella (una matrice) la posizione del numero estratto
            '''
            indici_tab = tabellone.pos_numero_estratto_tabellone(estratti[-1])
            tabellone.sostituisci_numero_tabellone(indici_tab[0],indici_tab[1],indici_tab[2])

            '''per ciascun giocatore i si verificano le possibili vincite'''   
            for i in range(len(lista_giocatori)): 
                n=n_cartelle[i]
                for j in range(n):
                    exitcond=regole.verifica_vincite(lista_giocatori[i].visualizza_cartella(j))[1]
                    if(exitcond == True): #se un giocatore ha effettuato la tombola termina il gioco
                        print('FINE PARTITA: il giocatore',i+1,'ha fatto Tombola nella cartella', j+1)
                        for i in range(len(lista_giocatori)):
                                    n=n_cartelle[i]
                                    print('Giocatore ', i+1)
                                    for j in range(n):
                                        lista_giocatori[i].visualizza_cartella(j).stampa()
                        exit()

                    vincita=regole.verifica_vincite(lista_giocatori[i].visualizza_cartella(j))[0]
                    if vincita not in vincite: #si verifica che tale vincita non sia stata già effettuata
                        vincite.append(vincita)# se il giocatore è il primo ad effettuare una certa vincita si memorizza e si stampa il tipo di vincita
                        if vincita == 2:
                            print('il Giocatore',i+1,'ha fatto ambo, nella cartella', j+1 )
                        elif vincita == 3:
                            print('il Giocatore',i+1,'ha fatto terna, nella cartella', j+1 )
                        elif vincita == 4:
                            print('il Giocatore',i+1,'ha fatto quaterna, nella cartella', j+1 )
                        elif vincita == 5:
                            print('il Giocatore',i+1,'ha fatto cinquina, nella cartella', j+1 )
                        
                        '''quando viene effettuata una nuova vincita si da l'opportunità all'utente di visualizzare le cartelle dei giocatori o di visualizzare i numeri estratti sul tabellone'''
                        try:
                            while True:
                                print('Digita: \n -1 per visualizzare le cartelle dei giocatori \n -2 per visuializzare il cartellone \n -premere invio per continuare a giocare\n ')
                                handle_richiesta= int(input('>'))
                                if handle_richiesta==1:
                                    for i in range(len(lista_giocatori)):
                                        n=n_cartelle[i]
                                        print('Giocatore ', i+1)
                                        for j in range(n):
                                            lista_giocatori[i].visualizza_cartella(j).stampa()

                                elif handle_richiesta==2:
                                    tabellone.visualizza_tabellone()
                                else:
                                    break #qualunque valore diverso da 1 e 2 fa uscire del ciclo while   
                        except:
                            pass
                                    
                else:
                    pass

            '''finchè un giocatore non realizza la tombola il programma domandi di effettuare nuove estrazioni'''        
            input("Procedo con una nuova estrazione?")
        print("Fine partita.")


    else:
        print('istruzioni per l uso \ndigitare main.py [-h] [-g G] [-n [N ...]] \nin cui -h fornisce più dettagli sull utilizzo \n-g si sostituisce con il numero di giocatori desiderato \n-n è una sequenza di numeri che indicano le cartelle per giocatore corrispondete')
        exit()
except:
    print('istruzioni per l uso \ndigitare main.py [-h] [-g G] [-n [N ...]] \nin cui -h fornisce più dettagli sull utilizzo \n-g si sostituisce con il numero di giocatori desiderato \n-n è una sequenza di numeri che indicano le cartelle per giocatore corrispondete')



    

