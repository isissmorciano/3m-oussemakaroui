# # Esercizio 59: Gestione Inventario Prodotti

# ## Obiettivo
# Gestire un inventario di prodotti in formato JSON, con funzioni per filtrare per categoria e calcolare il valore totale.

# ## Dati forniti
# Una lista di prodotti hardcoded:
# ```python
# prodotti = [
#     {"nome": "Mela", "categoria": "Frutta", "prezzo": 2.5, "quantita": 10},
#     {"nome": "Pane", "categoria": "Pane", "prezzo": 1.0, "quantita": 5},
#     {"nome": "Banana", "categoria": "Frutta", "prezzo": 1.8, "quantita": 8}
# ]
# ```

# ## Istruzioni

# 1. **Definire `salva_inventario(prodotti, nome_file)`**: Accetta una lista di dizionari e un nome file. Salva la lista in JSON con indentazione.

# 2. **Definire `carica_inventario(nome_file)`**: Accetta un nome file e restituisce la lista di dizionari caricata da JSON.

# 3. **Definire `filtra_per_categoria(prodotti, categoria)`**: Accetta la lista prodotti e una stringa categoria. Restituisce una lista con i prodotti di quella categoria.

# 4. **Definire `calcola_totale_categoria(prodotti, categoria)`**: Accetta la lista prodotti e una categoria. Calcola e restituisce il valore totale (prezzo * quantita) per i prodotti di quella categoria.

# 5. **Definire `main()`**: 
#    - Definisce `prodotti` (dati hardcoded)
#    - Chiama `salva_inventario` su "inventario.json"
#    - Chiama `carica_inventario` per ottenere i dati
#    - Filtra per "Frutta" e calcola il totale
#    - Stampa i prodotti filtrati e il totale

# ## Suggerimenti
# - Importa `json`
# - Usa `json.dump` e `json.load` come negli esercizi precedenti
# - Per filtrare: usa un ciclo for e append se categoria corrisponde
# - Per totale: somma prezzo*quantita solo per prodotti filtrati
# - Gestisci errori di file (FileNotFoundError)

# ## Esempio di output atteso
# ```
# File 'inventario.json' salvato con successo.
# Prodotti Frutta: [{'nome': 'Mela', 'categoria': 'Frutta', 'prezzo': 2.5, 'quantita': 10}, {'nome': 'Banana', 'categoria': 'Frutta', 'prezzo': 1.8, 'quantita': 8}]
# Totale valore Frutta: 39.4
# ```

import json

def salva_inventario(prodotti, nome_file):
    try:
        with open(nome_file, "w", encoding="utf-8") as file:
            json.dump(prodotti, file, indent=4)
        print(f"File '{nome_file}' salvato con successo.")
    except Exception as e:
        print(f"Errore durante il salvataggio: {e}")


def carica_inventario(nome_file):
    try:
        with open(nome_file, "r", encoding="utf-8") as file:
            prodotti = json.load(file)
        return prodotti
    except FileNotFoundError:
        print(f"Errore: il file '{nome_file}' non esiste.")
        return []
    except Exception as e:
        print(f"Errore durante il caricamento: {e}")
        return []


def filtra_per_categoria(prodotti, categoria):
    filtrati = []
    for prodotto in prodotti:
        if prodotto["categoria"] == categoria:
            filtrati.append(prodotto)
    return filtrati


def calcola_totale_categoria(prodotti, categoria):
    totale = 0
    for prodotto in prodotti:
        if prodotto["categoria"] == categoria:
            totale += prodotto["prezzo"] * prodotto["quantita"]
    return totale


def main():
    
    prodotti = [
        {"nome": "Mela", "categoria": "Frutta", "prezzo": 2.5, "quantita": 10},
        {"nome": "Pane", "categoria": "Pane", "prezzo": 1.0, "quantita": 5},
        {"nome": "Banana", "categoria": "Frutta", "prezzo": 1.8, "quantita": 8}
    ]

    nome_file = "inventario.json"

   
    salva_inventario(prodotti, nome_file)

   
    prodotti_caricati = carica_inventario(nome_file)

    
    categoria = "Frutta"
    prodotti_filtrati = filtra_per_categoria(prodotti_caricati, categoria)
    totale = calcola_totale_categoria(prodotti_caricati, categoria)

   
    print(f"Prodotti {categoria}:", prodotti_filtrati)
    print(f"Totale valore {categoria}:", totale)


if __name__ == "__main__":
    main()
