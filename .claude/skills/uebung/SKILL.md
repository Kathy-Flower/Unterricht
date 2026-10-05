---
name: uebung
description: Übungswebsite für Schüler erstellen (GitHub Pages) – Aufgaben mit Sofortauswertung, Lösungen, Prozent und Note 1+ bis 6, ohne Datenerfassung. Nutzen bei "Übungsseite", "Online-Übung", "Website zum Üben", "/uebung <Thema>".
---

# Übungswebsite

**Eingabe**: Thema, ggf. Anzahl Aufgaben (Standard 10–15) und Zweck (Übung, Vorbereitung
Klassenarbeit).

## Regeln

- Basis ist **immer** `werkzeuge/uebung-vorlage.html`: kopieren nach `uebungen/<thema>-<nr>.html`
  und nur den Block `INHALT` (TITEL, UNTERTITEL, AUFGABEN) ändern.
- **Keine Datenerfassung**, kein Google-Formular, keine Namen. Auswertung nur im Browser:
  Lösung + Erklärung je Aufgabe, Prozent, Note nach `grundlagen/notenschluessel.md`
  (Tendenzen) – ist in der Vorlage eingebaut.
- Mischung: ca. 40 % ★, 40 % ★★, 20 % ★★★. Typen `zahl`, `mc`, `text`; bei `zahl`
  sinnvolle `alternativen`/`toleranz` (z. B. Rundung auf zwei Nachkommastellen: toleranz 0.005).
- Mathe in KaTeX: `$\\sqrt{2}$` (im JS-String Backslashes verdoppeln).
- Erklärungen kurz und hilfreich (der Rechenweg in einer Zeile).

## Vorgehen

1. Aufgaben entwerfen, **alle Lösungen in Python nachrechnen**.
2. Datei erstellen, dann mit Playwright testen (Chromium unter `/opt/pw-browsers`):
   einmal alles richtig ausfüllen → muss 100 % / 1+ zeigen; leer auswerten → 0 % / 6;
   keine Konsolenfehler.
3. In `README.md` unter „Übungen“ verlinken.
4. Committen, auf `main` pushen. Link nennen:
   `https://kathy-flower.github.io/Unterricht/uebungen/<datei>.html`
   (erscheint 1–2 Minuten nach dem Push). Hinweis: Lösungen stehen im Quelltext.
