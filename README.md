
#  WANNABE AIMLAB

Jednoduchá aim-trainer hra vytvořená v **Pythonu** pomocí knihovny **Pygame**. Hráč má za úkol co nejrychleji a nejpřesněji zasahovat náhodně generované terče a dosáhnout co nejvyššího skóre.

---

##  O projektu

WANNABE AIMLAB je školní projekt inspirovaný populárními aim tréninkovými aplikacemi. Hra slouží k procvičování rychlosti reakcí a přesnosti míření pomocí myši.

### Hlavní funkce

-  Náhodně generované terče
-  Časový limit 30 sekund
-  Výpočet přesnosti zásahů
-  Bodovací systém
-  Fullscreen režim
-  Závěrečná výsledková obrazovka

---

##  Použité technologie

- Python 3
- Pygame

---

##  Struktura projektu

```text
wannabe-aimlab/
│
├── aimlab.py
├── README.md
├── requirements.txt
└── docs/
    └── dokumentace.md
```

---

##  Instalace

### 1. Naklonování repozitáře

```bash
git clone https://github.com/uzivatel/wannabe-aimlab.git
cd wannabe-aimlab
```

### 2. Instalace závislostí

```bash
pip install -r requirements.txt
```

nebo

```bash
pip install pygame
```

---

##  Spuštění hry

```bash
python aimlab.py
```

---

##  Ovládání

| Klávesa / Tlačítko | Funkce |
|-------------------|---------|
| Levé tlačítko myši | Střelba |
| ESC | Přepnutí fullscreen režimu |
| Zavření okna | Ukončení hry |

---

##  Herní princip

Po spuštění hry se zobrazí hlavní menu.

Po kliknutí na tlačítko **START**:

- začne běžet časovač,
- zobrazí se první terč,
- hráč získává body za zásahy.

Každý terč:

- se objeví na náhodném místě,
- zůstane na obrazovce 2 sekundy,
- po zásahu nebo vypršení času je nahrazen novým.

Po uplynutí 30 sekund se zobrazí výsledková obrazovka.

---

##  Bodování

| Akce | Body |
|--------|--------|
| Zásah terče | +100 |

Přesnost se počítá podle vzorce:

```text
Přesnost = (Zásahy / Výstřely) × 100
```

---

##  Implementace

### Třída `Terc`

Třída reprezentuje jeden herní terč.

Obsahuje:

- náhodnou pozici na obrazovce,
- poloměr terče,
- čas vytvoření,
- životnost terče.

Metody:

```python
nakresli()
```

Vykreslí terč na obrazovku.

```python
zkontroluj_klik(mx, my)
```

Vrací `True`, pokud hráč klikl do oblasti terče.

---

##  Herní stavy

Program využívá tři stavy:

### Menu

Zobrazení úvodní obrazovky a tlačítka START.

### Hra

Aktivní hraní, vykreslování terčů a počítání skóre.

### Výsledky

Zobrazení konečného skóre a přesnosti.

---

##  Screenshoty

### Menu

![Menu](assets/menu.png)

### Hra

![Gameplay](assets/gameplay.png)

### Výsledky

![Results](assets/results.png)

> Screenshoty je potřeba doplnit do složky `assets`.

---

##  Možná vylepšení

- Zvukové efekty
- Ukládání rekordů
- Více obtížností
- Různé typy terčů
- Lepší grafika a animace
- Statistiky hráče
- Online žebříček

---

##  Autor

Vytvořeno jako projekt v Pythonu s využitím knihovny Pygame.

---

## 📜 Licence

Tento projekt je určen pro vzdělávací účely.
