import Utils


parser = Utils.initialize_parser()
n_giocatori=parser.g
n_cartelle=parser.n
print(n_giocatori, n_cartelle)
if (Utils.numero_giocatori(n_giocatori)) and (Utils.confronta_lista_cartelle(n_giocatori,n_cartelle)):
    print('ok')

else:
    exit()



