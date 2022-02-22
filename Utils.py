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

'''l'utente deve fornire al programma un numero di gioctori e un numero equivalente di cartelle per giocatore'''
def confronta_lista_cartelle(numero_giocatori, lista_cartelle):

    if len(lista_cartelle)==numero_giocatori:
        return True
    
    else:
        print('il numero di cartelle deve corrispondere al numero di giocatori')
        exit()  

'''verifica che ogni giocatore abbia un numero congruo di cartelle (almeno 1, massimo 6)'''
def numero_cartelle(lista_cartelle):
    contatore=0
    for i in lista_cartelle:
        if i<1:
            contatore=contatore +1
        elif i >=7:
            contatore=contatore +1
        else:
            pass

    if contatore!=0:
        print('ogni giocatore deve disporre almeno di una cartella e un massimo di 6 cartelle')
        return False
    else:
        return True

'''si estrae un numero casual finchè no se ne estrae uno che non è mai stato estratto'''
def estrazione(estratti):
    
    numero_estratto = random.randint(1, 90)
    if numero_estratto not in estratti:    
        print("il numero estratto è:", numero_estratto)
        estratti.append(numero_estratto)
    else: 
        numero_estratto = estrazione(estratti)
    
    return estratti



