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
        print('Il numero di giocatori deve essere almeno maggiore di 1')
        sys.exit()
    else:
        return numero_giocatori


def confronta_lista_cartelle(numero_giocatori,lista_cartelle):

    '''
    Verificare che il numero di cartelle sia uguale a quello dei giocatori.

    Input=Numero di giocatori e una lista in cui ci sono le cartelle assegnate a ogni giocatore.

    '''
    if len(lista_cartelle)==numero_giocatori:
        return True
    elif len(lista_cartelle)<=numero_giocatori:
        print('A ogni giocatore deve essere assegnata almeno una cartella')
        sys.exit()
    else:
        print('I giocatori sono '+ str(numero_giocatori) +' , hai assegnato troppe cartelle, inseriscine '+ str(len(lista_cartelle)-numero_giocatori) + ' di meno')
        sys.exit()


def numero_cartelle(lista_cartelle):

    '''
    Vincolo sul numero di cartelle per ogni giocatore.

    Input=lista di cartelle.

    Output=numero di cartelle per ogni giocatore oppure dei messaggi che avvisano che il numero di cartelle per ogni giocatore
    non sono sufficienti oppure sono troppe.

    '''
    for i in lista_cartelle:
        if i<1:
            print('Ogni giocatore deve avere una o più cartelle')
            sys.exit() 
        elif i>5:
            print('Ogni singolo giocatore non può avere più di 5 cartelle')
            sys.exit() 
    return lista_cartelle
