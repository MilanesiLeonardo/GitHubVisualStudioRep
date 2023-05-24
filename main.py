import os
from time import sleep

file = open("rifiuti.txt", "r")
stringa = ""

for line in file:
  stringa = stringa + line.strip()

rifiuti = stringa.split(";")
file.close()
listaR1 = rifiuti[0].split(',')
listaR2 = rifiuti[1].split(',')
listaR3 = rifiuti[2].split(',')
listaR4 = rifiuti[3].split(',')
listaR5= rifiuti[4].split(',')

def r1(rifiuto):
    if rifiuto in listaR1:
        return True
    return False


def r2(rifiuto):
    if rifiuto in listaR2:
        return True
    return False

def r3(rifiuto):
    if rifiuto in listaR3:
        return True
    return False

def r4(rifiuto):
    if rifiuto in listaR4:
        return True
    return False

def r5(rifiuto):
    if rifiuto in listaR5:
        return True
    return False

def normativa(user):
    os.system('cls')
    print(f"""
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                Benvenuto {user} nel progetto RAE                                                                           
    La normativa individua 5 raggruppamentidi Raee in base alle tecnologie necessarie al loro corretto trattamento:
                    
    \tR1)-Grande bianco freddo -grandi elettrodomestici per la refrigerazione: frigoriferi, congelatori, condizionatori
    \tR2)-Grande bianco non freddo -grandi elettrodomestici come lavatrici, lavastoviglie.
    \tR3)-TV Monitor a tubo catodico
    \tR4)-Elettronica di consumo, Telecomunicazioni, Informatica, piccoli elettrodomestici, elettroutensili, giocattoli, apparecchi di illuminazione, dispositivi medici.
    \tR5)-Sorgenti luminose a scarica: lampade fluorescenti e sorgenti luminose compatte. 
    """)

def manuale(user):
    os.system('cls')
    scelta=input("""
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+    
    Scegli tra quali di queste categorie appartiene il tuo elettrodomestico (Inserire un numero fra quelli indicati qui sotto):

    1) Grandi elettrodomestici;
    2) Piccoli elettrodomestici;
    3) Apparecchiature informatiche e per telecomunicazioni;
    4) Apparecchiature di consumo e pannelli fotovoltaici;
    5) Apparecchiature di illuminazione;
    6) Utensili elettrici  ed elettronici (ad eccezione degli utensili industriali fissi di grandi dimensioni);
    7) Giocattoli e apparecchiature per il tempo libero e lo sport;
    8) Dispositivi medici (ad eccezione di tutti i prodotti impiantati ed infettati;
    9) Strumenti di monitoraggio e di controllo;
    10) Distributori automatici.
    11) TV Monitor a tubo catodico
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+         

""")
    sleep(2)
    os.system('cls')    
    if scelta == "1" or scelta == "10":
        scelta=input("Se il tuo grande elettrodomestico è freddo? (s/n): ")
        if scelta =="s":
            print(f"""
+---------------------------------------------------------------+
    {user}, il tuo rifiuto viene smaltito con l'ausilio
    delle tecnologie relative categoria R1          
      
""")
        else:
            print(f"""
+---------------------------------------------------------------+
    {user}, il tuo rifiuto viene smaltito con l'ausilio
    delle tecnologie relative categoria R2         
      
""")
                      
    elif (scelta =="2") or (scelta == "3") or (scelta == "4") or (scelta =="6") or (scelta=="7")  or (scelta=="8"):
            print(f"""
+---------------------------------------------------------------+
    {user}, il tuo rifiuto viene smaltito con l'ausilio
    delle tecnologie relative categoria R4
      
""")        
    elif (scelta == "11"):
        print(f"""
+---------------------------------------------------------------+
    {user}, il tuo rifiuto viene smaltito con l'ausilio
    delle tecnologie relative categoria R3
      
""")
          
    else:
        print(f"""
+---------------------------------------------------------------+
    {user}, il tuo rifiuto viene smaltito con l'ausilio
    delle tecnologie relative categoria R5
      
""")  


def gui(user):
    while True:
        os.system('cls')
        print(
f"""
+---------------------------------------------------------------+

    Progetto “RAEE”

    Benvenuto {user}, 
    Inserire un singolo apparecchio elettronico o elettrico
    da smaltire o \"normativa\" per visualizzare
    i criteri di smaltimento
    (Deve essere singolare e non abbreviato es.Frigo):
    
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
        elif rifiuto == "normativa":
            normativa(user)
        else:
            print(
f"""
+---------------------------------------------------------------+

    {user}, il tuo rifiuto non appartiene a nessuna categoria
    controlla che l'inserimento sia corretto e rispetti
    tutte le condizioni elencate
    Vuoi provare ad trovare la categoria di appartenenza
    manualmente? (s/n)

+---------------------------------------------------------------+            
            
            """)
            scelta=input()
            match scelta:
                case "s":
                    manuale(user)
                case "n":
                    continue
                case _:
                    continue
                    
            sleep(6)
        continuare = input("Desideri continuare? per uscire digitare \"n\": ")
        if continuare.lower() == "n":
            break
        sleep(2)



