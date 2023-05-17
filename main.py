import os
from time import sleep

def r1(rifiuto):
    listaR1=[
    "frigorifero",
    "congelatore",
    "condizionatore",
    "deumidificatore",
    "pompa di calore",
    "radiatore a olio",
    "asciugatrice con pompa di calore"]
    if rifiuto in listaR1:
        return True
    return False


def r2(rifiuto):
    listaR2 = [
    "lavatrice",
    "lavastoviglie",
    "apparecchio di cottura",
    "stufa elettrica",
    "piastra riscaldante"]
    if rifiuto in listaR2:
        return True
    return False

def r3(rifiuto):
    listaR3 = [ 
    "televisore",
    "schermo",
    "schermo lcd",
    "monitor",
    "laptop",
    "notebook"
    ]
    if rifiuto in listaR3:
        return True
    return False

def r4(rifiuto):
    listaR4 = [
    "mainframe",
    "aspirapolvere",
    "scopa meccanica",
    "macchina per cucire",
    "apparecchio di illuminazione",
    "forno a microonde",
    "ventilatore",
    "ferro da stiro",
    "tostapane",
    "bollitore",
    "sveglia",
    "orologio",
    "bilancia",
    "calcolatrice",
    "apparecchio radio",
    "videocamera", 
    "videoregistratore",
    "giocattolo elettrico",
    "giocattolo elettronico",
    "rilevatore di fumo", 
    "regolatore di calore", 
    "termostato",
    "apparecchio di cottura",
    "stufa elettrica",
    "piastra riscaldante",
    "friggitrice", 
    "frullatore", 
    "macina caffè",
    "asciugacapelli", 
    "spazzolino da denti", 
    "rasoio", 
    "telefono",
    "cellulare",
    "navigatore satellitare",
    "calcolatrice",
    "router",
    "pc",
    "stampante",
    "telefono"
]
    if rifiuto in listaR4:
        return True
    return False

def r5(rifiuto):
    listaR5 = [    
    "tubi fluorescenti",
    "lampade fluorescenti compatte",
    "lampade fluorescenti",
    "lampade a scarica ad alta densità",
    "lampade a vapori di sodio ad alta pressione",
    "lampade ad algoritmo metallico",
    "lampade a vapori di sodio a bassa pressione",
    "led"
    ]
    if rifiuto in listaR5:
        return True
    return False

def gui(user):
    while True:
        os.system('cls')
        print(
f"""
+---------------------------------------------------------------+

    Progetto “RAEE”

    Benvenuto {user}, 
    Inserire la tipologia di
    apparecchio elettronico elettrico
    da smaltire (Deve essere singolare e non abbreviato es.Frigo):
    
    """)
        rifiuto = input().lower()
        os.system('cls')
        if r1(rifiuto):
            print(
f"""
+---------------------------------------------------------------+

    {user}, il tuo rifiuto viene smaltito con l'ausilio
    delle tecnologie relative categoria R1 
 
""")
            sleep(3)
        elif r2(rifiuto):
            print(
f"""
+---------------------------------------------------------------+

    {user}, il tuo rifiuto viene smaltito con l'ausilio
    delle tecnologie relative categoria R2 

""")
            sleep(3)
        elif r3(rifiuto):
            print(
f"""
+---------------------------------------------------------------+

    {user}, il tuo rifiuto viene smaltito con l'ausilio
    delle tecnologie relative categoria R3

""")
            sleep(3)
        elif r4(rifiuto):
            print(
f"""
+---------------------------------------------------------------+

    {user}, il tuo rifiuto viene smaltito con l'ausilio
    delle tecnologie relative categoria R4

""")
            sleep(3)

        elif r5(rifiuto):
            print(
f"""
+---------------------------------------------------------------+

    {user}, il tuo rifiuto viene smaltito con l'ausilio
    delle tecnologie relative categoria R5

""")
            sleep(3)
        else:
            print(
f"""
+---------------------------------------------------------------+

    {user}, il tuo rifiuto non appartiene a nessuna categoria
    controlla che l'inserimento sia corretto e rispetti
    tutte le condizioni elencate

+---------------------------------------------------------------+
""")
            
            sleep(6)
        continuare = input("Desideri continuare? (s/n): ")
        if continuare.lower() == "n":
            break
        sleep(2)

user = input("Inserire un nome utente: ")
gui(user)