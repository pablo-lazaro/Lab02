import translator as tr

t = tr.Translator()
t.loadDictionary("dictionary.txt")

while True:
    t.printMenu()
    txtIn = input("Inserisci un numero: ")

    if not txtIn.isdigit():
        print("Per favore, inserisci un numero valido.")
        continue

    scelta = int(txtIn)

    if scelta == 1:
        txtIn = input("Inserisci <parola aliena> <traduzione>: ").lower()
        parti = txtIn.split()
        if len(parti) >= 2:
            t.handleAdd(parti)
            print("Aggiunta con successo!")
        else:
            print("Errore: inserisci almeno una traduzione.")

    elif scelta == 2:
        parola = input("Quale parola vuoi tradurre? ").lower()
        res = t.handleTranslate(parola)
        if res:
            print(f"Traduzioni: {', '.join(res)}")
        else:
            print("Parola non trovata.")

    elif scelta == 3:
        query = input("Inserisci ricerca con '?' (es. ali?no): ").lower()
        if '?' in query:
            res_liste = t.handleWildcard(query)
            if res_liste:
                for lista in res_liste:
                    print(f"Trovata: {', '.join(lista)}")
            else:
                print("Nessuna corrispondenza trovata.")
        else:
            print("Errore: la ricerca deve contenere un '?'")

    elif scelta == 4:
        t.printAll()

    elif scelta == 5:
        print("Arrivederci!")
        break