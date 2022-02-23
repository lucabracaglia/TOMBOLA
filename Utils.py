import argparse
import random
import sys


def initialize_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("-g", type=int, help="Numero di giocatori")
    parser.add_argument("-n", nargs='*', type=int, help="Numero di cartelle per giocatore")
    

    return parser.parse_args()


def numero_giocatori(numero_giocatori):
    if numero_giocatori <= 1:
        print('Il numero di giocatori deve essere almeno maggiore di 1')
        sys.exit()
    else:
        return True

'''l'utente deve fornire al programma un numero di gioctori e un numero equivalente di cartelle per giocatore'''
def confronta_lista_cartelle(numero_giocatori, lista_cartelle):

    if len(lista_cartelle)==numero_giocatori:
        return True
    
    elif len(lista_cartelle)<=numero_giocatori:
        print('A ogni giocatore deve essere assegnata almeno una cartella')
        sys.exit()
    
    else:
        print('I giocatori sono '+ str(numero_giocatori) +' , hai assegnato troppe cartelle, inseriscine '+ str(len(lista_cartelle)-numero_giocatori) + ' di meno')
        sys.exit()


'''verifica che ogni giocatore abbia un numero congruo di cartelle (almeno 1, massimo 6)'''
def numero_cartelle(lista_cartelle):
    for i in lista_cartelle:
        if i<1:
            print('Ogni giocatore deve avere una o più cartelle')
            sys.exit() 
        elif i>7:
            print('Ogni singolo giocatore non può avere più di 7 cartelle')
            sys.exit() 
    return lista_cartelle

'''si estrae un numero casual finchè no se ne estrae uno che non è mai stato estratto'''
def estrazione(estratti):
    
    numero_estratto = random.randint(1, 90)
    if numero_estratto not in estratti:    
        print("Il numero estratto è:", numero_estratto)
        estratti.append(numero_estratto)
    else: 
        numero_estratto = estrazione(estratti)
    
    return estratti



