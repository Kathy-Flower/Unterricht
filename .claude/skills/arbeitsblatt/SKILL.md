---
name: arbeitsblatt
description: Differenziertes Mathe-Arbeitsblatt Klasse 9 als Word erstellen – Niveaus ★/★★/★★★, Tippkarten, Lösungen zur Selbstkontrolle. Nutzen bei "Arbeitsblatt", "AB", "Übungsblatt", "/arbeitsblatt <Thema>".
---

# Arbeitsblatt

**Eingabe**: Thema/Lernziel, ggf. Zweck (Erarbeitung, Übung, Wiederholung) und Umfang.
Standard: 1–2 Seiten Aufgaben, Übungszweck.

## Regeln

- **Keine Kopfzeile**, kein Name/Datum-Feld. Titel = Thema.
- Schwarz-weiß-tauglich (Graustufen); Farbe nur, wenn ausdrücklich für den Beamer gewünscht.
- Jede Aufgabe beginnt mit einem **Operator** (`grundlagen/operatoren.md`).
- Niveaus: ★ Basis (AFB I, Mindeststandard für alle) · ★★ Standard (AFB II) ·
  ★★★ Experte (AFB III / Transfer). Mindestens eine Aufgabe je Niveau; ★-Aufgaben
  so, dass schwache SuS sie sicher schaffen.
- Eine Begründungs-/Erklär-Aufgabe mit **Wortspeicher** oder Satzanfängen.
- Ggf. kurzer **Merkkasten** oben (bei Erarbeitung) oder „Erinnerung“-Kasten (bei Übung).
- **Tippkarten** (eigene Seite, zum Ausschneiden): pro schwieriger Aufgabe Tipp 1
  (Strategie) und Tipp 2 (konkreter Ansatz).
- **Lösungen** (eigene Seite, zur Selbstkontrolle, mit Rechenweg bei ★★/★★★).
- Zahlen so wählen, dass sie ohne Taschenrechner aufgehen, wo das Thema das verlangt.

## Vorgehen

1. Lies `CLAUDE.md` und die Grundlagen.
2. Aufgaben entwerfen, **alle Lösungen in Python nachrechnen**.
3. Erzeugungsskript `reihen/<nr>-<thema>/erzeuge_ab_<kurz>.py` mit
   `werkzeuge/docx_bausteine.py` schreiben, ausführen → `ab-<kurz>.docx`.
4. Vorschau rendern (siehe `/reihe`) und Layout prüfen (Seitenumbrüche, Platz zum Schreiben).
5. Committen, pushen, per `SendUserFile` schicken.
