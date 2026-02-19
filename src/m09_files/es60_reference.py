#!/usr/bin/env python3
"""Simple interactive menu for managing students (JSON storage).

No UUID, no argparse, no CSV. Pure menu-driven with for loops.
"""

import json
import os

STORAGE_FILE = "studenti.json"


def load_studenti(path=STORAGE_FILE):
    """Load students from JSON file. Return empty list if not found."""
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, IOError):
        return []


def save_studenti(studenti, path=STORAGE_FILE):
    """Save students to JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(studenti, f, ensure_ascii=False, indent=4)


def mostra_lista(studenti):
    """Display all students with index."""
    if not studenti:
        print("Nessuno studente.")
        return
    for i in range(len(studenti)):
        s = studenti[i]
        print(f"{i}. {s['nome']} - Voto: {s['voto']}")


def mostra_dettaglio(studenti, indice):
    """Show detail for one student by index."""
    if indice < 0 or indice >= len(studenti):
        print(f"Indice non valido: {indice}")
        return
    s = studenti[indice]
    print(f"Nome: {s['nome']}")
    print(f"Voto: {s['voto']}")


def aggiungi_studente(studenti):
    """Add a new student (ask nome and voto)."""
    nome = input("Nome studente: ").strip()
    if not nome:
        print("Errore: nome non può essere vuoto.")
        return

    voto_str = input("Voto (0-10): ")
    try:
        voto = float(voto_str)
    except ValueError:
        print("Errore: voto deve essere un numero.")
        return

    if voto < 0 or voto > 10:
        print("Errore: voto deve essere tra 0 e 10.")
        return

    studente = {"nome": nome, "voto": voto}
    studenti.append(studente)
    print(f"Aggiunto: {nome} con voto {voto}")


def cancella_studente(studenti):
    """Delete a student by index."""
    mostra_lista(studenti)
    indice_str = input("Indice da cancellare: ")
    try:
        indice = int(indice_str)
    except ValueError:
        print("Errore: indice deve essere un numero.")
        return

    if indice < 0 or indice >= len(studenti):
        print("Errore: indice non valido.")
        return

    nome = studenti[indice]["nome"]
    studenti.pop(indice)
    print(f"Cancellato: {nome}")


def aggiorna_studente(studenti):
    """Update a student's voto by index."""
    mostra_lista(studenti)
    indice_str = input("Indice da aggiornare: ")
    try:
        indice = int(indice_str)
    except ValueError:
        print("Errore: indice deve essere un numero.")
        return

    if indice < 0 or indice >= len(studenti):
        print("Errore: indice non valido.")
        return

    voto_str = input("Nuovo voto (0-10): ")
    try:
        voto = float(voto_str)
    except ValueError:
        print("Errore: voto deve essere un numero.")
        return

    if voto < 0 or voto > 10:
        print("Errore: voto deve essere tra 0 e 10.")
        return

    studenti[indice]["voto"] = voto
    print(f"Aggiornato: {studenti[indice]['nome']} con voto {voto}")


def ricerca_per_nome(studenti):
    """Search students by name (substring, case-insensitive)."""
    termine = input("Termine di ricerca: ").strip().lower()
    if not termine:
        print("Errore: termine non può essere vuoto.")
        return

    risultati = []
    for s in studenti:
        nome_lower = s["nome"].lower()
        if termine in nome_lower:
            risultati.append(s)

    if not risultati:
        print("Nessuno studente trovato.")
        return

    print(f"Trovato(i) {len(risultati)} risultato(i):")
    for s in risultati:
        print(f"  {s['nome']} - Voto: {s['voto']}")


def filtra_per_voto(studenti):
    """Filter students by voto range."""
    min_str = input("Voto minimo (0-10): ")
    try:
        min_voto = float(min_str)
    except ValueError:
        print("Errore: numero non valido.")
        return

    max_str = input("Voto massimo (0-10): ")
    try:
        max_voto = float(max_str)
    except ValueError:
        print("Errore: numero non valido.")
        return

    if min_voto < 0 or min_voto > 10 or max_voto < 0 or max_voto > 10:
        print("Errore: voti devono essere tra 0 e 10.")
        return

    if min_voto > max_voto:
        print("Errore: voto minimo > voto massimo.")
        return

    risultati = []
    for s in studenti:
        if min_voto <= s["voto"] <= max_voto:
            risultati.append(s)

    if not risultati:
        print("Nessuno studente in questo range.")
        return

    print(f"Trovato(i) {len(risultati)} risultato(i):")
    for s in risultati:
        print(f"  {s['nome']} - Voto: {s['voto']}")


def main():
    """Main menu loop."""
    studenti = load_studenti()

    while True:
        print("\n=== GESTIONE STUDENTI ===")
        print("1. Aggiungi studente")
        print("2. Visualizza lista")
        print("3. Visualizza dettaglio")
        print("4. Aggiorna voto")
        print("5. Cancella studente")
        print("6. Ricerca per nome")
        print("7. Filtra per voto")
        print("8. Esci")

        scelta = input("\nScelta (1-8): ").strip()

        if scelta == "1":
            aggiungi_studente(studenti)
        elif scelta == "2":
            mostra_lista(studenti)
        elif scelta == "3":
            mostra_lista(studenti)
            indice_str = input("Indice: ")
            try:
                indice = int(indice_str)
                mostra_dettaglio(studenti, indice)
            except ValueError:
                print("Errore: indice deve essere un numero.")
        elif scelta == "4":
            aggiorna_studente(studenti)
        elif scelta == "5":
            cancella_studente(studenti)
        elif scelta == "6":
            ricerca_per_nome(studenti)
        elif scelta == "7":
            filtra_per_voto(studenti)
        elif scelta == "8":
            save_studenti(studenti)
            print("Salvato. Arrivederci!")
            break
        else:
            print("Scelta non valida. Riprova.")


if __name__ == "__main__":
    main()
