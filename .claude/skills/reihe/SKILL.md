---
name: reihe
description: Reihenplanung (Unterrichtsvorhaben) für Mathe Klasse 9 erstellen – Stundenübersicht der ganzen Einheit als Word-Datei. Nutzen bei "plane die Reihe", "Reihenplanung", "Unterrichtsvorhaben", "/reihe <Thema>".
---

# Reihenplanung

**Eingabe**: Thema (z. B. „Wurzeln“). Nur nachfragen, falls unklar: Startdatum und Anzahl
verfügbarer Wochen (sonst: Platzhalter-Daten, Rhythmus Mi 45 min / Do 90 min, ca. 3 Wochen).

## Vorgehen

1. Lies `CLAUDE.md`, `grundlagen/curriculum-klasse9.md` (Abschnitt zum Thema),
   `grundlagen/unterrichtsplanung.md`, `grundlagen/methoden.md`.
2. Plane die Abfolge entlang der Curriculum-Kapitel und der Kompetenzerwartungen
   (keine Buchverweise; jede Stunde mit Problem und Lebensweltbezug). Jede Kompetenzerwartung muss mindestens einer Stunde zugeordnet sein.
3. Pro Stunde: Nr. · Tag/Dauer · Thema · Kernanliegen (1 Satz) · zentrale Methode ·
   Kompetenzen (Kürzel) · Material/Medien · Hausaufgabe/Übung.
4. Einplanen: Diagnose zu Beginn (Vorwissen), Übungs-/Vertiefungsstunde(n),
   Übungswebsite vor der Klassenarbeit, Wiederholungsstunde, ggf. Klassenarbeit.
5. Word-Datei mit `werkzeuge/docx_bausteine.py` (Querformat: `neues_dokument(quer=True)`)
   nach `reihen/<nr>-<thema>/00-reihenplanung.docx`. Erzeugungsskript daneben als
   `erzeuge_reihenplanung.py` speichern (damit später Änderungen leicht sind).
6. Als PDF rendern (LibreOffice, siehe unten), Seiten ansehen, Layout korrigieren.
7. Committen, pushen, per `SendUserFile` schicken. Kurz zusammenfassen und anbieten,
   die erste Stunde mit `/stunde` auszuarbeiten.

Vorschau: `soffice --headless --convert-to pdf --outdir <scratchpad> <datei>.docx`, dann
`pdftoppm -png -r 60`. Ist LibreOffice Writer nicht installiert:
`apt-get install -y --no-install-recommends libreoffice-writer`.
