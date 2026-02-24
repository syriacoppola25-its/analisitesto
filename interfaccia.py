import tkinter as tk

root = tk.Tk()
root.title("Analisi testo")

percorso = tk.Entry(root)
percorso.pack(padx=10, pady=20)

def conteggioparole (testodato, paroledate):
    nparole = len(paroledate)
    ncaratteri = len(testodato)
    print("Conteggio parole: ", nparole)
    print("Conteggio caratteri: ", ncaratteri)

def parolakpi (paroledate):
    listaparole = []
    dizionario = {}
    for a in paroledate:
        p_pulita = a.strip(".,:;!?") #toglie la punteggiatura dalla parola
        p_pulita = p_pulita.replace("\n", " ") #mette tutto su un'unica linea
        listaparole.appent(p_pulita)
        if "" in listaparole:
            listaparole.remove("") #il programma mi dava stringhe vuote nella lista, quindi le rimuovo
        if p_pulita in dizionario:
            dizionario[p_pulita] += 1
        else:
            dizionario[p_pulita] = 1
    p_corta = min(listaparole, key=len)
    p_lunga = max(listaparole, key=len)
    frequente = max(dizionario, key=dizionario.get)
    print("La parola più corta è: ", p_corta)
    print("La parola più lunga è: ", p_lunga)
    print("La parola più frequente è: ", frequente)

def spaziepunti (testodato):
    punteggiatura = [".", ",", ":", ";", "!", "?"]
    p = 0
    s = 0
    for i in testodato:
        if i in punteggiatura:
            p += 1
        elif i == " ":
            s += 1
    print ("Numero di spazi: ", s)
    print("Numero di segni di punteggiatura: ", p)
            

def leggi (percorsofile):
    with open(percorsofile, "r") as file:
        testo = file.read()
        parole = testo.split()
        



bottone = tk.Button(root, text="Analizza file", command=somma)
bottone.pack()
















'''punteggiatura = [".", ",", ":", ";", "!", "?"]
listaparole = []
dizionario = {}

#Funzione di lettura:
def lettura():
    percorso = str(input("Inserisci il percorso file: "))
    with open (percorso, "r") as file:
        testo = file.read()

def conteggio_parole(testoinput):
    parole = testoinput.split()
    nparole = len(parole)
    ncaratteri = len(testoinput)'''
