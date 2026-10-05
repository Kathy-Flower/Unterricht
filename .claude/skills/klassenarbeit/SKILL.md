---
name: klassenarbeit
description: Klassenarbeit Mathe Klasse 9 (60 min, Gruppe A/B) mit Erwartungshorizont, Punkteverteilung nach AFB 30/50/20 und Notenschlüssel als Word erstellen. Nutzen bei "Klassenarbeit", "KA", "Test", "Erwartungshorizont", "/klassenarbeit <Themen>".
---

# Klassenarbeit mit Erwartungshorizont

**Eingabe**: Themen/Kapitel. Nachfragen nur, wenn nicht klar: Datum, ob ein
hilfsmittelfreier Teil gewünscht ist (Standard: **ja**, ca. 15 min, ohne Taschenrechner,
wird danach eingesammelt), ob Gruppe A/B gewünscht ist (Standard: **ja**).

## Vorgaben

- Dauer **60 Minuten**; Umfang realistisch (Faustregel: Lehrerin braucht ≤ 1/3 der Zeit).
- **AFB I 30 % · AFB II 50 % · AFB III 20 %** der Punkte (±3 Prozentpunkte).
  Operatoren nach `grundlagen/operatoren.md`.
- Inhalts- und prozessbezogene Kompetenzen aus `grundlagen/curriculum-klasse9.md` abdecken,
  auch mindestens eine Aufgabe mit Argumentieren/Kommunizieren und eine mit Modellieren
  (sofern das Thema es hergibt).
- **Gruppe A/B**: gleiche Struktur, gleiche Schwierigkeit, andere Zahlen/Kontexte.
- Punkte ganzzahlig oder halbe Punkte; Gesamtpunktzahl „rund“ (z. B. 40, 45, 50).

## Geheimhaltung (wichtig!)

Das Repository ist öffentlich. Klassenarbeiten und Erwartungshorizonte **niemals committen**.
Alles nur in `klassenarbeiten/` ablegen (steht in `.gitignore`) und per `SendUserFile`
schicken. Vor dem Commit mit `git status` prüfen, dass nichts davon dabei ist.

## Dateien (in `klassenarbeiten/`)

1. `ka<n>-gruppe-a.docx`, `ka<n>-gruppe-b.docx` – Schülerfassung: Titel, Hinweise
   (Hilfsmittel, Zeit, „Lösungsweg muss nachvollziehbar sein“), Aufgaben mit Punkten rechts,
   Platz zum Rechnen nur wenn auf dem Blatt gerechnet wird.
2. `ka<n>-erwartungshorizont.docx` – für A und B:
   - Tabelle je Aufgabe: Teilaufgabe · erwartete Leistung (Lösung mit Zwischenschritten) ·
     AFB · Punkte · Teilpunkte-Hinweise (wofür gibt es Teilpunkte, typische Fehler)
   - Übersicht: Punkte je AFB mit Prozentanteil (Kontrolle 30/50/20)
   - Kompetenzübersicht (welche Aufgabe prüft welche Kompetenzerwartung)
   - **Notentabelle** mit `notentabelle(d, gesamt)` (Fachschaftsschlüssel)
   - Leere Bewertungstabelle pro Schüler*in (Aufgabe · erreicht · möglich) zum Anheften
3. Erzeugungsskript daneben speichern.

## Vorgehen

1. Aufgaben entwerfen, AFB zuordnen, Punkte vergeben, Verteilung prüfen (in Python
   summieren). **Alle Lösungen in Python nachrechnen**, auch für Gruppe B.
2. Dateien erzeugen, Vorschau rendern und prüfen (Seitenumbrüche!).
3. **Nicht committen.** Per `SendUserFile` schicken und darauf hinweisen, die Dateien
   herunterzuladen (die Sitzung wird später gelöscht). Zusammenfassen: Punkte, AFB-Verteilung,
   Zeitschätzung.
