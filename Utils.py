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
        print('il numero di giocatori deve essere almeno maggiore di 1')
        sys.exit()
    else:
        return True


def confronta_lista_cartelle(numero_giocatori, lista_cartelle):

    if len(lista_cartelle)==numero_giocatori:
        return True
    
    else:
        print('il numero di cartelle deve corrispondere al numero di giocatori')
        exit()  

def numero_cartelle(lista_cartelle):

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


