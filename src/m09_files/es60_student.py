# # Esercizio 60: Gestione Studenti (Menu CLI) - Versione Semplificata

# ## Obiettivo
# Realizzare una applicazione interattiva a menu per gestire una lista di studenti
# salvata in file JSON. Uso menu in console, cicli for espliciti, separazione tra 
# logica (funzioni che ritornano valori) e presentazione (print nel main).

# ## Requisiti
# - **Storage**: file `studenti.json` (UTF-8, indentato)
# - **Comandi via menu**: aggiungi, visualizza, cerca, filtra, aggiorna, cancella, statistiche
# - **Identificatori**: indice progressivo (posizione nella lista)
# - **Persistenza**: carica/salva JSON automaticamente
# - **Sintassi semplice**: cicli for, senza list comprehension, niente argparse
# - **Architettura**: funzioni ritornano dati/messaggi, main gestisce output

# ## Struttura dati
# ```python
# studenti = [
#     {"nome": "Alice", "voto": 8.5},
#     {"nome": "Bob", "voto": 7.0},
#     {"nome": "Carlo", "voto": 9.0}
# ]
# ```

# ## Funzioni - Validazione

# ```python
# def valida_voto(voto_str) -> tuple[bool, float | str]
#     """Validate vote. Returns (is_valid, value_or_error)."""
# ```

# **Esempi return:**
# - `valida_voto("7.5")` → `(True, 7.5)`
# - `valida_voto("10")` → `(True, 10.0)`
# - `valida_voto("0")` → `(True, 0.0)`
# - `valida_voto("11")` → `(False, "...")`  [messaggio errore]
# - `valida_voto("-1")` → `(False, "...")`  [messaggio errore]
# - `valida_voto("abc")` → `(False, "...")`  [messaggio errore]

# ## Funzioni - I/O Formattazione

# ```python
# def formatta_lista(studenti) -> str
#     """Format student list as string. Returns formatted output."""

# def mostra_dettaglio(studenti, indice) -> tuple[bool, str, dict | None]
#     """Show detail for one student. Returns (success, message, data)."""
# ```

# **Esempi return:**

# `formatta_lista([])` → `"Nessuno studente."`

# `formatta_lista([{"nome": "Alice", "voto": 8.5}, {"nome": "Bob", "voto": 7.0}])` →
# ```
# 0. Alice - Voto: 8.5
# 1. Bob - Voto: 7.0
# ```

# `mostra_dettaglio(studenti, 0)` → `(True, "Alice - Voto: 8.5", {"nome": "Alice", "voto": 8.5})`

# `mostra_dettaglio(studenti, 999)` → `(False, "Indice non valido", None)`

# ## Funzioni - Operazioni CRUD

# ```python
# def aggiungi_studente(studenti) -> tuple[bool, str, dict | None]
#     """Add student. Returns (success, message, new_student)."""

# def cancella_studente(studenti) -> tuple[bool, str]
#     """Delete student by index. Returns (success, message)."""

# def aggiorna_studente(studenti) -> tuple[bool, str]
#     """Update student voto. Returns (success, message)."""
# ```

# **Esempi return:**

# `aggiungi_studente(studenti)` → `(True, "Studente aggiunto: Alice con voto 8.5", {"nome": "Alice", "voto": 8.5})`

# `cancella_studente(studenti)` → `(True, "Studente cancellato")`  oppure  `(False, "Indice non valido")`

# `aggiorna_studente(studenti)` → `(True, "Voto aggiornato")`  oppure  `(False, "Voto non valido")`

# ## Funzioni - Ricerca e Filtro

# ```python
# def ricerca_per_nome(studenti, termine=None) -> list[dict]
#     """Search students by name. Returns list of results."""

# def filtra_per_voto(studenti, min_voto=None, max_voto=None) -> list[dict]
#     """Filter by grade range. Returns list of results."""
# ```

# **Esempi return:**

# `ricerca_per_nome(studenti, "alice")` → `[{"nome": "Alice", "voto": 8.5}]`

# `ricerca_per_nome(studenti, "And")` → `[{"nome": "Andrea", "voto": 9.0}]`  (substring, case-insensitive)

# `ricerca_per_nome(studenti, "xyz")` → `[]`

# `filtra_per_voto(studenti, 7.0, 8.5)` → `[{"nome": "Alice", "voto": 8.5}, {"nome": "Bob", "voto": 7.0}]`

# `filtra_per_voto(studenti, 9.0, 10.0)` → `[]`

# ## Funzioni - Statistiche

# ```python
# def calcola_media(studenti) -> float
#     """Calculate average grade. Returns float."""

# def trova_migliore(studenti) -> dict | None
#     """Find best student. Returns student dict or None."""

# def trova_peggiore(studenti) -> dict | None
#     """Find worst student. Returns student dict or None."""
# ```

# **Esempi return:**

# `calcola_media([])` → `0.0`

# `calcola_media([{"nome": "A", "voto": 6.0}, {"nome": "B", "voto": 8.0}, {"nome": "C", "voto": 10.0}])` → `8.0`

# `trova_migliore([])` → `None` 
# `trova_migliore(studenti)` → `{"nome": "Carlo", "voto": 9.0}`

# `trova_peggiore([])` → `None`

# `trova_peggiore(studenti)` → `{"nome": "Bob", "voto": 7.0}`

# ## Funzioni - I/O e Main

# ```python
# def load_studenti(path=STORAGE_FILE) -> list[dict]
#     """Load from JSON. Return empty list if not found."""

# def save_studenti(studenti, path=STORAGE_FILE) -> None
#     """Save to JSON file."""

# def main() -> None
#     """Main menu loop - handles all output."""
# ```

# **Esempi return:**

# `load_studenti("studenti.json")` → `[{"nome": "Alice", "voto": 8.5}, ...]`

# `load_studenti("/tmp/nonexistent.json")` → `[]`  (se file non esiste)

# `save_studenti([...], "studenti.json")` → `None`  (crea/aggiorna file)

# ## Menu principale
# ```
# === GESTIONE STUDENTI ===
# 1. Aggiungi studente
# 2. Visualizza lista
# 3. Visualizza dettaglio (per indice)
# 4. Aggiorna voto
# 5. Cancella studente
# 6. Ricerca per nome
# 7. Filtra per voto (range)
# 8. Statistiche (media, migliore, peggiore)
# 9. Esci
# Scelta:
# ```

# ## Comandi dettaglio

# **Aggiungi**: chiede nome e voto, valida (voto 0-10), ritorna (success, msg, student).

# **Visualizza lista**: formatta e stampa tutti con indice.
# ```
# 0. Alice - Voto: 8.5
# 1. Bob - Voto: 7.0
# 2. Carlo - Voto: 9.0
# ```

# **Visualizza dettaglio**: chiede indice, mostra nome e voto.

# **Aggiorna**: chiede indice e nuovo voto, valida, aggiorna. Ricorda di mostrare lista prima.

# **Cancella**: chiede indice, rimuove studente.

# **Ricerca**: chiede termine, cerca substring in nomi (case-insensitive). Ritorna lista di risultati.

# **Filtra**: chiede min/max voto, ritorna lista di studenti in range.

# **Statistiche**: mostra
# - Numero totale studenti
# - Media voti (formato: `media:.2f`)
# - Voto più alto (nome + voto)
# - Voto più basso (nome + voto)

# **Esci**: salva automaticamente in JSON e termina.

# ## Esempio di Output
# ```
# === GESTIONE STUDENTI ===
# 1. Aggiungi studente
# 2. Visualizza lista
# 3. Visualizza dettaglio (per indice)
# 4. Aggiorna voto
# 5. Cancella studente
# 6. Ricerca per nome
# 7. Filtra per voto (range)
# 8. Statistiche (media, migliore, peggiore)
# 9. Esci
# Scelta: 1
# Inserisci nome: Alice
# Inserisci voto (0-10): 8.5
# ✓ Studente aggiunto: Alice con voto 8.5

# === GESTIONE STUDENTI ===
# ...
# Scelta: 2
# 0. Alice - Voto: 8.5
# 1. Bob - Voto: 7.0
# 2. Carlo - Voto: 9.0

# === GESTIONE STUDENTI ===
# ...
# Scelta: 8
# --- STATISTICHE ---
# Numero studenti: 3
# Media voti: 8.17
# Voto più alto: Carlo con 9.0
# Voto più basso: Bob con 7.0

# === GESTIONE STUDENTI ===
# ...
# Scelta: 9
# Salvataggio in corso... Dati salvati su studenti.json
# ```

# ## Validazione
# - Nome obbligatorio (non vuoto)
# - Voto numerico tra 0 e 10
# - Indice deve essere valido
# - Funzione `valida_voto()` centralizza la logica di validazione

# ## Note Architettura
# - **Separazione logica/presentazione**: funzioni ritornano (success, msg, data) o liste
# - **Main gestisce output**: tutti i print sono nel main, non nelle funzioni
# - **Testabilità**: funzioni senza side-effect I/O sono facili da testare
# - **Riusabilità**: funzioni logiche usabili da API, GUI, CLI, ecc.
# - Niente UUID, niente argparse
# - Usare `for` loop, niente list comprehension
# - Messaggi chiari e user-friendly


import json
import os

STORAGE_FILE = "studenti.json"


# =========================
# VALIDAZIONE
# =========================

def valida_voto(voto_str) -> tuple[bool, float | str]:
    try:
        voto = float(voto_str)
    except ValueError:
        return False, "Il voto deve essere numerico."

    if voto < 0 or voto > 10:
        return False, "Il voto deve essere compreso tra 0 e 10."

    return True, voto


# =========================
# FORMATTAZIONE
# =========================

def formatta_lista(studenti) -> str:
    if len(studenti) == 0:
        return "Nessuno studente."

    output = ""
    for i in range(len(studenti)):
        studente = studenti[i]
        output += f"{i}. {studente['nome']} - Voto: {studente['voto']}\n"

    return output.strip()


def mostra_dettaglio(studenti, indice) -> tuple[bool, str, dict | None]:
    if indice < 0 or indice >= len(studenti):
        return False, "Indice non valido", None

    studente = studenti[indice]
    messaggio = f"{studente['nome']} - Voto: {studente['voto']}"
    return True, messaggio, studente


# =========================
# CRUD
# =========================

def aggiungi_studente(studenti) -> tuple[bool, str, dict | None]:
    nome = input("Inserisci nome: ").strip()
    if nome == "":
        return False, "Il nome non può essere vuoto.", None

    voto_str = input("Inserisci voto (0-10): ").strip()
    valido, risultato = valida_voto(voto_str)

    if not valido:
        return False, risultato, None

    nuovo = {"nome": nome, "voto": risultato}
    studenti.append(nuovo)

    return True, f"Studente aggiunto: {nome} con voto {risultato}", nuovo


def cancella_studente(studenti) -> tuple[bool, str]:
    indice_str = input("Inserisci indice da cancellare: ").strip()

    if not indice_str.isdigit():
        return False, "Indice non valido."

    indice = int(indice_str)

    if indice < 0 or indice >= len(studenti):
        return False, "Indice non valido."

    studenti.pop(indice)
    return True, "Studente cancellato."


def aggiorna_studente(studenti) -> tuple[bool, str]:
    indice_str = input("Inserisci indice da aggiornare: ").strip()

    if not indice_str.isdigit():
        return False, "Indice non valido."

    indice = int(indice_str)

    if indice < 0 or indice >= len(studenti):
        return False, "Indice non valido."

    voto_str = input("Inserisci nuovo voto (0-10): ").strip()
    valido, risultato = valida_voto(voto_str)

    if not valido:
        return False, risultato

    studenti[indice]["voto"] = risultato
    return True, "Voto aggiornato."




def ricerca_per_nome(studenti, termine=None) -> list[dict]:
    risultati = []

    if termine is None:
        termine = input("Inserisci nome da cercare: ").strip()

    termine = termine.lower()

    for studente in studenti:
        if termine in studente["nome"].lower():
            risultati.append(studente)

    return risultati


def filtra_per_voto(studenti, min_voto=None, max_voto=None) -> list[dict]:
    risultati = []

    if min_voto is None:
        min_str = input("Voto minimo: ").strip()
        valido, min_voto = valida_voto(min_str)
        if not valido:
            return []

    if max_voto is None:
        max_str = input("Voto massimo: ").strip()
        valido, max_voto = valida_voto(max_str)
        if not valido:
            return []

    for studente in studenti:
        voto = studente["voto"]
        if voto >= min_voto and voto <= max_voto:
            risultati.append(studente)

    return risultati




def calcola_media(studenti) -> float:
    if len(studenti) == 0:
        return 0.0

    totale = 0
    for studente in studenti:
        totale += studente["voto"]

    return totale / len(studenti)


def trova_migliore(studenti) -> dict | None:
    if len(studenti) == 0:
        return None

    migliore = studenti[0]

    for studente in studenti:
        if studente["voto"] > migliore["voto"]:
            migliore = studente

    return migliore


def trova_peggiore(studenti) -> dict | None:
    if len(studenti) == 0:
        return None

    peggiore = studenti[0]

    for studente in studenti:
        if studente["voto"] < peggiore["voto"]:
            peggiore = studente

    return peggiore




def load_studenti(path=STORAGE_FILE) -> list[dict]:
    if not os.path.exists(path):
        return []

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_studenti(studenti, path=STORAGE_FILE) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(studenti, f, indent=4, ensure_ascii=False)




def main() -> None:
    studenti = load_studenti()

    while True:
        print("\n=== GESTIONE STUDENTI ===")
        print("1. Aggiungi studente")
        print("2. Visualizza lista")
        print("3. Visualizza dettaglio (per indice)")
        print("4. Aggiorna voto")
        print("5. Cancella studente")
        print("6. Ricerca per nome")
        print("7. Filtra per voto (range)")
        print("8. Statistiche (media, migliore, peggiore)")
        print("9. Esci")

        scelta = input("Scelta: ").strip()

        if scelta == "1":
            success, msg, _ = aggiungi_studente(studenti)
            print(("✓ " if success else "✗ ") + msg)

        elif scelta == "2":
            print(formatta_lista(studenti))

        elif scelta == "3":
            indice_str = input("Indice: ").strip()
            if indice_str.isdigit():
                success, msg, _ = mostra_dettaglio(studenti, int(indice_str))
                print(msg)
            else:
                print("Indice non valido.")

        elif scelta == "4":
            print(formatta_lista(studenti))
            success, msg = aggiorna_studente(studenti)
            print(("✓ " if success else "✗ ") + msg)

        elif scelta == "5":
            print(formatta_lista(studenti))
            success, msg = cancella_studente(studenti)
            print(("✓ " if success else "✗ ") + msg)

        elif scelta == "6":
            risultati = ricerca_per_nome(studenti)
            print(formatta_lista(risultati))

        elif scelta == "7":
            risultati = filtra_per_voto(studenti)
            print(formatta_lista(risultati))

        elif scelta == "8":
            print("\n--- STATISTICHE ---")
            print(f"Numero studenti: {len(studenti)}")
            media = calcola_media(studenti)
            print(f"Media voti: {media:.2f}")

            migliore = trova_migliore(studenti)
            peggiore = trova_peggiore(studenti)

            if migliore:
                print(f"Voto più alto: {migliore['nome']} con {migliore['voto']}")
            if peggiore:
                print(f"Voto più basso: {peggiore['nome']} con {peggiore['voto']}")

        elif scelta == "9":
            print("Salvataggio in corso...")
            save_studenti(studenti)
            print("Dati salvati su studenti.json")
            break

        else:
            print("Scelta non valida.")


if __name__ == "__main__":
    main()