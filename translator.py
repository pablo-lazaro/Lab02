class Translator:

    def __init__(self):
        self.dizionario = {}

    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit
        print("\n" + "-"*20)
        print("1. Aggiungi nuova parola")
        print("2. Cerca una Traduzione")
        print("3. Cerca con wildcard")
        print("4. Stampa tutto il dizionario")
        print("5. Exit")
        print("-"*20)


    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        with open(dict, "r", encoding="utf-8") as file:
            for riga in file:
                riga_pulita = riga.strip().lower()
                if riga_pulita != "":
                    self.handleAdd(riga_pulita)

        return self.dizionario


    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        parti = entry.split(" ")
        parola_aliena = parti[0]
        nuove_traduzioni = parti[1:]

        # Se parola non esiste, creo lista vuota
        if parola_aliena not in self.dizionario.keys():
            self.dizionario[parola_aliena] = []
        # Aggiungo traduzioni alla lista (Es 2)
        for tr in nuove_traduzioni:
            if tr not in self.dizionario[parola_aliena]:
                self.dizionario[parola_aliena].appenf(tr)

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        if query in self.dizionario:
            return self.dizionario[query]

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass

    def handleMultipleTranslations(self, parole):
        pass
