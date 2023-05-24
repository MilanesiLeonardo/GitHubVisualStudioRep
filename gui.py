from tkinter import *
from tkinter import ttk
from time import sleep
import main1



def show(button):
    try:
        if (entry.get()).strip() != "" and len(entry.get()) >= 3:
            global label2
            global label3
            global entry1
            label2 = Label(root, text=f"""
    --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                    Benvenuto {entry.get().capitalize()} nel progetto RAE                                                                           

Grazie per averci contattato per il corretto smaltimento del tuo apparecchio elettronico o elettrico. 
Per poterti fornire informazioni dettagliate sul criterio di smaltimento corretto, 
ti chiediamo di inserire il nome del singolo apparecchio che desideri smaltire. 
Assicurati di inserire il nome completo dell'apparecchio, senza abbreviazioni. 
Ad esempio, se desideri smaltire un frigorifero, ti invitiamo a digitare 'frigorifero' senza alcuna abbreviazione.
Se, invece, desideri ottenere informazioni sulla normativa generale riguardante lo smaltimento dei rifiuti elettronici, 
ti preghiamo di digitare la parola 'normativa'.
                                                                    
""", justify=CENTER, background='#242424', fg="white", font=('sans-serif', 12), pady=10)
            
            label2.pack()
            label3 = Label(root, 
    text=
    f"""             
        Inserire un singolo apparecchio elettronico o elettrico da smaltire o \"normativa\" per visualizzare i criteri di smaltimento 
        (Deve essere singolare e non abbreviato es.Frigo):

    """, justify=LEFT, background='#242424', fg="white", font=('sans-serif', 12), pady=10)
            label3.pack()
            entry1 = Entry(root, font=('sans-serif', 18), relief=FLAT, width=40)
            label1.destroy()
            entry.destroy()
            text1 = entry1.get()
            entry1.pack()
            entry1.focus()
            enterCom1 = root.bind('<Return>', lambda event: show_text(entry1.get()))
    except:
        return False

def show_text(text):
    if text != "":
        entry1.delete(0, END)
        entry1.configure(state='disabled')
        label4 = Label(root, text=f"""
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    {main1.gui(text)}

""", justify=CENTER, background='#242424', fg="white", font=('sans-serif', 12), pady=10)
        
        label4.pack()
        label4.after(5000, lambda: (label4.destroy(), entry1.configure(state='normal'), entry1.focus()))


root = Tk()
root.iconbitmap('icon.ico')
root.title('Progetto RAEE')
root.geometry("1000x800")
root.minsize(925, 700)
root.config(background='#242424')
label1 = Label(root, text=f"Inserisci il tuo nickname: ", background='#242424', fg="white", font=('sans-serif', 18), pady=20)
label1.pack()
entry = Entry(root, font=('sans-serif', 18), relief=FLAT, width=40)
entry.focus()
enterCom = root.bind('<Return>', show)
text = entry.get()
entry.pack()

root.mainloop()












