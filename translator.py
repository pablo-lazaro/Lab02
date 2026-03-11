class Translator:
    def __init__(self):
        self.dizionario = dict()

    def printMenu(self):
        print("-" * 30)
        print("   Translator Alien-Italian")
        print("-" * 30)
        print("1. Aggiungi nuova parola")
        print("2. Cerca traduzione")
        print("3. Cerca con wildcard")
        print("4. Stampa tutto il Dizionario")
        print("5. Exit")
        print("-" * 30)

    def loadDictionary(self, file_name):
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                for line in file:
                    parti = line.strip().lower().split(" ")
                    if len(parti) >= 2:
                        aliena = parti[0]
                        traduzioni = parti[1:]
                        if aliena in self.dizionario:
                            self.dizionario[aliena].extend(traduzioni)
                        else:
                            self.dizionario[aliena] = traduzioni
        except FileNotFoundError:
            pass

    def handleAdd(self, entry):
        # entry è [parola, trad1, trad2...]
        parola_aliena = entry[0].strip().lower()
        nuove_traduzioni = [t.strip().lower() for t in entry[1:]]

        if parola_aliena in self.dizionario:
            self.dizionario[parola_aliena].extend(nuove_traduzioni)
        else:
            self.dizionario[parola_aliena] = nuove_traduzioni

    def handleTranslate(self, query):
        return self.dizionario.get(query.lower().strip())

    def handleWildcard(self, query):
        query = query.lower().strip()
        risultati = []
        # Cerchiamo tutte le chiavi che corrispondono al pattern
        for parola_aliena in self.dizionario.keys():
            if len(parola_aliena) == len(query):
                match = True
                for i in range(len(query)):
                    if query[i] != '?' and query[i] != parola_aliena[i]:
                        match = False
                        break
                if match:
                    risultati.append(self.dizionario[parola_aliena])
        return risultati

    def printAll(self):
        for aliena, traduzioni in sorted(self.dizionario.items()):
            print(f"{aliena} -> {', '.join(traduzioni)}")