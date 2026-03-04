import translator as tr

t = tr.Translator()

while(True):

    t.printMenu()

    dizionario = t.loadDictionary("dictionary.txt")

    txtIn = int(input())

    # Add input control here!

    if int(txtIn) == 1:
        print("Ok, quale parola vuoi aggiungere? ")
        parola_da_aggiungere = input().lower()
        t.handleAdd(parola_da_aggiungere)
        print("Aggiunta!")

    if int(txtIn) == 2:

        print("Ok, quale traduzione devo cercare?")
        parola_da_cercare = input().lower()
        traduzione = t.handleTranslate(parola_da_cercare)
        print(traduzione)

    if int(txtIn) == 3:
        pass
    if int(txtIn) == 4:
        print(dizionario)

    break
    # commit

# una parola --> multiple traduzioni
