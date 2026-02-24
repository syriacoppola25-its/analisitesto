import tkinter as tk

root = tk.Tk()
root.title("Analisi testo")

tk.Label(root, text="Inserisci il percorso del file:").pack(pady=5)
percorso = tk.Entry(root)
percorso.pack()

#Trovare il numero di parole e caratteri:
def conteggioparole (testodato, paroledate):
    nparole = len(paroledate)
    ncaratteri = len(testodato)
    return nparole, ncaratteri

#Trovare la parola più lunga, corta e frequente:
def parolakpi (paroledate):
    listaparole = []
    dizionario = {}
    for a in paroledate:
        p_pulita = a.strip(".,:;!?") #toglie la punteggiatura dalla parola
        p_pulita = p_pulita.replace("\n", " ") #mette tutto su un'unica linea
        listaparole.append(p_pulita)
        if "" in listaparole:
            listaparole.remove("") #il programma mi dava stringhe vuote nella lista, quindi le rimuovo
        if p_pulita in dizionario:
            dizionario[p_pulita] += 1
        else:
            dizionario[p_pulita] = 1
    p_corta = min(listaparole, key=len)
    p_lunga = max(listaparole, key=len)
    frequente = max(dizionario, key=dizionario.get)
    return p_corta, p_lunga, frequente

#Trovare il numero di spazi e segni di punteggiatura:
def spaziepunti (testodato):
    punteggiatura = [".", ",", ":", ";", "!", "?"]
    p = 0 #un contatore per i punti
    s = 0 #un contatore per gli spazi
    for i in testodato:
        if i in punteggiatura:
            p += 1
        elif i == " ":
            s += 1
    return s, p
            

def leggi ():
    percorsofile = percorso.get()
    with open(percorsofile, "r") as file:
        testo = file.read()
        parole = testo.split()

        numparole, numcaratteri = conteggioparole(testo, parole)
        numspazi, numpunti = spaziepunti(testo)
        pcorta, plunga, pfrequente = parolakpi(parole)

        nparole_res.config(text=f"Parole: {numparole}, Caratteri: {numcaratteri}")
        nspazi_res.config(text=f"Spazi: {numspazi}, Punteggiatura: {numpunti}")
        pcorta_res.config(text=f"Parola più corta: {pcorta}")
        plunga_res.config(text=f"Parola più lunga: {plunga}")
        pfrequente_res.config(text=f"Parola più frequente: {pfrequente}")



bottone = tk.Button(root, text="Analizza file", command=leggi)
bottone.pack()

nparole_res = tk.Label(root, text="I risultati appariranno qui")
nparole_res.pack()
nspazi_res = tk.Label(root, text="")
nspazi_res.pack()
pcorta_res = tk.Label(root, text="")
pcorta_res.pack()
plunga_res = tk.Label(root, text="")
plunga_res.pack()
pfrequente_res = tk.Label(root, text="")
pfrequente_res.pack()

root.mainloop()















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
