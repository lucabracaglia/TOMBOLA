import Utils
import sys


parser = Utils.initialize_parser()
n_giocatori=parser.g
n_cartelle=parser.n
if n_giocatori==None or n_cartelle==None:
    print('Digita -h per vedere gli argomenti da inserire sulla linea di comando')
    sys.exit()
if (Utils.numero_giocatori(n_giocatori)) and (Utils.confronta_lista_cartelle(n_giocatori,n_cartelle)) and (Utils.numero_cartelle(n_cartelle)):
    print('Si può iniziare')
else:
    sys.exit()



