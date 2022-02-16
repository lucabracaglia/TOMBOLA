import argparse
import random
import sys


def initialize_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("-g", type=int, help="Numero di giocatori")
    parser.add_argument("-n", nargs='*', type=int, help="Numero di cartelle per giocatore")

    return parser.parse_args()

def numero_giocatori(numero_giocatori):
    '''
    Vado a verificare che il numero di giocatori non sia minore di 2
    altrimenti il gioco non può iniziare

    Input=numero di giocatori

    Output=numero di giocatori oppure un messaggio di avviso che fa notare che il numero di giocatori
    non pùè sufficiente
    '''
    if numero_giocatori <= 1:
        print('il numero di giocatori deve essere almeno maggiore di 1')
        sys.exit()
    else:
        return numero_giocatori


def confronta_lista_cartelle(numero_giocatori, lista_cartelle):

    '''
    Verificare che il numero di cartelle sia uguale a quello dei giocatori.

    Input=Numero di giocatori e una lista in cui ci sono le cartelle assegnate a ogni giocatore.

    '''

    if len(lista_cartelle)==numero_giocatori:
        return True
    else:
        print('il numero di cartelle deve corrispondere al numero di giocatori')
        exit()  

def numero_cartelle(lista_cartelle):

    '''
    Vincolo sul numero di cartelle per ogni giocatore.

    Input=lista di cartelle.

    Output=numero di cartelle per ogni giocatore oppure dei messaggi che avvisano che il numero di cartelle per ogni giocatore
    non sono sufficienti oppure sono troppe.

    '''

    for i in range (lista_cartelle):
        if lista_cartelle[i]<1:
            print('prendi una cartella')
            exit() 
        elif lista_cartelle[i]>=8:
            print('troppe cartelle')
            exit() 
        else:
            return lista_cartelle


def estrazione(estratti):
    
    numero_estratto = random.randint(1, 90)
    if numero_estratto not in estratti:    
        print("il numero estratto è:", numero_estratto)
        estratti.append(numero_estratto)
    else: 
        numero_estratto = estrazione(estratti)
    
    return estratti


