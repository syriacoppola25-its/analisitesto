#for i in range(21): print(i, end=" ")

'''for i in range(31):
    if (i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    elif (i % 3 == 0):
        print("Fizz")
    elif (i % 5 == 0):
        print("Buzz")
    else:
        print(i)'''


#for i in range (1, 31): print("Fizzbuzz" if i % 3 == 0 and i % 5 == 0 else ("Fizz" if i % 3 == 0 else ("Buzz" if i % 5 == 0 else (i))))

#INPUT NELLA FUNZIONE, NO FUORI:
'''n = int(input("Inserisci un numero: ")) 
def paridispari (numero):
    if numero % 2 == 0:
        return True
    else:
        return False

print(paridispari(n))'''

'''with open("esempio.txt", "x") as f:
    f.write("ciao")
    f.close()'''



'''Dare il percorso di un file di testo e trovare:
1) Numero di parole
2) Numero di lettere
3) Numero di segni di punteggiatura
4) Numero di spazi
5) Parola più lunga
6) Parola più corta
7) Parola più frequente'''
punteggiatura = [".", ",", ":", ";", "!", "?"]
p = 0 #contatore punteggiatura
s = 0 #contatore spazi
listaparole = [] #per trovare la parola più corta e lunga
dizionario = {}
#niente = ""

percorsofile = str(input("Inserisci il percorso del file: "))
with open(percorsofile, "r") as file:
    testo = file.read()
    parole = testo.split()
    nparole = len(parole)
    ncaratteri = len(testo)
    print("Numero caratteri nel testo: ", ncaratteri)
    print("Numero parole nel testo: ", nparole)

    for i in testo:
        if i in punteggiatura:
            p += 1
        elif i == " ":
            s += 1
    print("Numero segni di punteggiatura: ", p)
    print("Numero spazi: ", s)

    '''for b in parole:
        p_no_punti = b.strip('.,.;!?')
        if len(p_no_punti) > len(c_parola_lunga):
            c_parola_lunga = p_no_punti
    print("La parola più lunga è: ", c_parola_lunga)'''

    for a in parole:
        no_punti = a.strip(".,:;!?")
        no_punti = no_punti.replace("\n", " ")
        listaparole.append(no_punti)
        if "" in listaparole:
            listaparole.remove("")
        if no_punti in dizionario:
            dizionario[no_punti] += 1
        else:
            dizionario[no_punti] = 1
    
    p_corta = min(listaparole, key=len)
    p_lunga = max(listaparole, key=len)
    frequente = max(dizionario, key=dizionario.get)
    print("La parola più corta è: ", p_corta)
    print("La parola più lunga è: ", p_lunga)
    print("La parola più frequente è: ", frequente)
