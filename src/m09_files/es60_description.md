# Esercizio 60: Gestione Studenti (Menu CLI) - Versione Semplificata

## Obiettivo
Realizzare una applicazione interattiva a menu per gestire una lista di studenti
salvata in file JSON. Uso menu in console, cicli for espliciti, sintassi semplice.

## Requisiti
- **Storage**: file `studenti.json` (UTF-8, indentato)
- **Comandi via menu**: aggiungi, visualizza, cerca, filtra, aggiorna, cancella
- **Identificatori**: indice progressivo (posizione nella lista)
- **Persistenza**: carica/salva JSON automaticamente
- **Sintassi semplice**: cicli for, senza list comprehension, niente argparse

## Struttura dati
```python
studenti = [
    {"nome": "Alice", "voto": 8.5},
    {"nome": "Bob", "voto": 7.0},
    {"nome": "Carlo", "voto": 9.0}
]
```

## Menu principale
```
=== GESTIONE STUDENTI ===
1. Aggiungi studente
2. Visualizza lista
3. Visualizza dettaglio (per indice)
4. Aggiorna voto
5. Cancella studente
6. Ricerca per nome
7. Filtra per voto (range)
8. Esci
Scelta:
```

## Comandi dettaglio

**Aggiungi**: chiede nome e voto, valida (voto 0-10), aggiunge alla lista.

**Visualizza lista**: stampa tutti gli studenti con indice:
```
0. Alice - Voto: 8.5
1. Bob - Voto: 7.0
2. Carlo - Voto: 9.0
```

**Visualizza dettaglio**: chiede indice, stampa nome e voto.

**Aggiorna**: chiede indice e nuovo voto, valida, aggiorna.

**Cancella**: chiede indice, rimuove studente.

**Ricerca**: chiede termine, cerca substring in nomi (case-insensitive).

**Filtra**: chiede min/max voto, stampa studenti in range.

**Esci**: salva automaticamente in JSON e termina.

## Validazione
- Nome obbligatorio (non vuoto)
- Voto numerico tra 0 e 10
- Indice deve essere valido
- Gestire input non valido con loop di richiesta

## Note
- Carica `studenti.json` all'avvio (o crea lista vuota se non esiste)
- Salva automaticamente all'uscita
- Niente UUID, niente argparse
- Usare `for` loop, niente list comprehension
- Messaggi chiari e user-friendly
