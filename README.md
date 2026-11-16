# Csempeszámoló program

**Hallgató neve:** Nagy Bence
**Neptun-kód:** D9LK0P

## Feladat leírása

A program a szoba és a csempe méretéből (cm) kiszámolja, hány csempe kell a burkoláshoz.
Ezután összeveti a meglévő csempék számával, és visszajelzi, mennyi marad, vagy mennyit kell még vásárolni.

### Felhasználói leírás

- Nem kell semmit telepíteni, csak Python 3 szükséges (a `tkinter` a Python része).
- Indítás: `python main.py`
- Töltsd ki az öt mezőt egész számokkal, majd kattints a **Számol** gombra.
- A **Törlés** gomb kiüríti a mezőket, a **Kilépés** gomb bezárja a programot.

## Felépítés

### Modul
- `nb_modul.py` – a saját modul
- `tkinter` – a grafikus felülethez

### Függvények (`nb_modul.py`)
- `nb_felfele(a, b)` – felfelé kerekített osztás
- `nb_csempe_darab(szoba_a, szoba_b, csempe_a, csempe_b)` – a szükséges csempék száma
- `nb_visszajelzes(szukseges, meglevo)` – szöveges visszajelzés (marad / vásárolni kell)

### Osztály (`nb_modul.py`)
- `NBCsempeSzamolo` – az ablak és a működés
  - `szamol()` – beolvassa a mezőket, ellenőriz, kiszámolja az eredményt
  - `torol()` – törli a mezőket
  - `kiir(szoveg)` – kiírja a szöveget az eredmény címkébe

### Eseménykezelés
- a gombok kattintása (`command=`)
