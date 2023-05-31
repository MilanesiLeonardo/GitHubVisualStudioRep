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
                                                                Benvenuto {user} nel progetto RAEE                                                                           
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


def gui(rifiuto):
    rifiuto = rifiuto.lower()
    
    if r1(rifiuto):
        return """
        Il tuo rifiuto viene smaltito con l'ausilio delle tecnologie relative alla categoria R1, 
        che comprende i grandi elettrodomestici freddi. Queste tecnologie sono specificamente progettate per la gestione 
        e lo smaltimento adeguato di dispositivi come frigoriferi, congelatori, e altri grandi elettrodomestici utilizzati 
        per la conservazione e il raffreddamento di alimenti e bevande. 
        Questi dispositivi vengono trattati secondo procedure specializzate, garantendo il rispetto delle normative ambientali 
        e la massima sicurezza durante il processo di smaltimento. Grazie all'utilizzo di queste tecnologie avanzate, 
        il tuo rifiuto viene gestito in modo responsabile, 
        promuovendo il riciclo dei materiali e contribuendo alla riduzione dell'impatto ambientale causato dai rifiuti elettronici.
        """
    elif r2(rifiuto):
        return """
        Il tuo rifiuto viene smaltito con l'ausilio delle tecnologie relative alla categoria R2, 
        che riguarda i grandi elettrodomestici non freddi. Queste tecnologie sono appositamente progettate per la gestione 
        e lo smaltimento adeguato di dispositivi come lavatrici, asciugatrici, lavastoviglie, fornelli, forni 
        e altri grandi elettrodomestici utilizzati per scopi diversi dalla refrigerazione. 
        Questi dispositivi vengono trattati in conformità alle procedure specifiche, garantendo il rispetto delle normative ambientali 
        e la sicurezza durante il processo di smaltimento. Attraverso l'impiego di queste tecnologie avanzate, 
        il tuo rifiuto viene gestito in modo responsabile, promuovendo il riciclo dei materiali e contribuendo alla riduzione dell'impatto ambientale 
        derivante dai rifiuti elettronici.
        """
    elif r3(rifiuto):
        return """
        Il tuo rifiuto viene smaltito con l'ausilio delle tecnologie relative alla categoria R3, 
        che riguarda i TV e i monitor a tubo catodico. Queste tecnologie sono specificamente sviluppate 
        per la gestione e lo smaltimento adeguato di dispositivi che utilizzano tubi catodici 
        per la visualizzazione delle immagini. I TV e i monitor a tubo catodico sono sottoposti a procedure specializzate 
        per garantire il corretto trattamento dei materiali e il rispetto delle normative ambientali vigenti. 
        L'utilizzo di queste tecnologie avanzate consente di gestire in modo responsabile il tuo rifiuto, 
        promuovendo il riciclo dei materiali e contribuendo alla riduzione dell'impatto ambientale derivante 
        dai rifiuti elettronici associati ai TV e ai monitor a tubo catodico.
        """
    elif r4(rifiuto):
        return """
        Il tuo rifiuto viene smaltito con l'ausilio delle tecnologie relative alla categoria R4, 
        che comprende l'elettronica di consumo, le telecomunicazioni, l'informatica, i piccoli elettrodomestici, 
        gli elettroutensili, i giocattoli, gli apparecchi di illuminazione e i dispositivi medici. 
        Grazie all'utilizzo di queste tecnologie, il tuo rifiuto viene adeguatamente smaltito, rispettando le normative ambientali vigenti 
        e contribuendo alla riduzione dell'impatto ambientale. I dispositivi di questa categoria, come i telefoni cellulari, 
        i computer, le stampanti, gli elettrodomestici di piccole dimensioni, gli elettroutensili, i giocattoli e gli apparecchi di illuminazione, 
        sono gestiti tramite processi specializzati che consentono di recuperare materiali preziosi e di minimizzare l'impatto sull'ambiente. 
        """
    elif r5(rifiuto):
        return """
        Il tuo rifiuto viene smaltito con l'ausilio delle tecnologie relative alla categoria R5, 
        che riguarda le sorgenti luminose a scarica, come le lampade fluorescenti e le sorgenti luminose compatte. 
        Grazie all'utilizzo di tecnologie avanzate, il tuo rifiuto viene gestito in modo sicuro e responsabile. 
        Le lampade fluorescenti e le sorgenti luminose compatte vengono smaltite attraverso processi specializzati 
        che mirano alla separazione dei materiali e al recupero delle sostanze pericolose. 
        Questo approccio garantisce il rispetto delle normative ambientali e la riduzione dell'impatto negativo 
        sulla salute umana e sull'ambiente.
        """
    elif rifiuto=="normativa":
        return """
        
NORMATIVA
La normativa individua 5 raggruppamentidi Raee in base alle tecnologie necessarie al loro corretto trattamento:
                
R1)-Grande bianco freddo -grandi elettrodomestici per la refrigerazione: frigoriferi, congelatori, condizionatori
R2)-Grande bianco non freddo -grandi elettrodomestici come lavatrici, lavastoviglie.
R3)-TV Monitor a tubo catodico
R4)-Elettronica di consumo, Telecomunicazioni, Informatica, piccoli elettrodomestici, elettroutensili, 
        giocattoli, apparecchi di illuminazione, dispositivi medici.
R5)-Sorgenti luminose a scarica: lampade fluorescenti e sorgenti luminose compatte. 
    """
    else:
        return """
        Mi dispiace, ma non è possibile identificare la categoria di smaltimento del rifiuto specificato. 
        Assicurati di fornire informazioni accurate e dettagliate sul tipo di dispositivo di cui stai cercando la categoria di smaltimento. 
        """



