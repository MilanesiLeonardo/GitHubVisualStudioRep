import os

def gui(user):
    while True:
        os.system('cls')
        print(
f"""
+----------------------------------------+
            Progetto “RAEE”

    Benvenuto {user}, 
    Inserire la tipologia di
    apparecchio elettronico elettrico
    da smaltire:
    """)
        rifiuto = input()
        os.system('cls')
        print(
"""
+----------------------------------------+            

    I RAEE sono suddivisi secondo il Dlgs n.49/2014 in 10 categorie:

    R1) Grande bianco freddo -grandi elettrodomestici per la refrigerazione: frigoriferi, congelatori, condizionatori
    R2) Grande bianco non freddo -grandi elettrodomestici come lavatrici, lavastoviglie.
    R3) TV Monitor a tubo catodico
    R4) Elettronica di consumo, Telecomunicazioni, Informatica, piccoli elettrodomestici, elettroutensili, 
        giocattoli, apparecchi di illuminazione, dispositivi medici.
    R5) Sorgenti luminose a scarica: lampade fluorescenti e sorgenti luminose compatte.
            
    Inserire la categoria più ideonea al rifiuto:
""")
        categoria1 = input()
user = input("Inserire un nome utente: ")
gui(user)