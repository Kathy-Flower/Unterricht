---
name: stunde
description: Einzelne Mathestunde Klasse 9 planen – Stundenentwurf mit Kompetenzen, didaktischem Kommentar, Verlaufsplan, Tafelbild und allen Materialien als Word. Nutzen bei "plane die Stunde", "Stundenentwurf", "Verlaufsplan", "/stunde <Thema>".
---

# Stundenplanung

**Eingabe**: Thema bzw. Nummer der Stunde in der Reihe, Tag (Mi 45 min / Do 90 min).
Fehlt der Tag, frage kurz nach. Gibt es eine Reihenplanung in `reihen/`, übernimm die Einordnung.

## Vorgehen

1. Lies `CLAUDE.md`, `grundlagen/unterrichtsplanung.md`, `grundlagen/methoden.md`,
   `grundlagen/operatoren.md`, den Curriculum-Abschnitt und ggf. die Reihenplanung.
2. Entwirf die Stunde nach der Struktur in `grundlagen/unterrichtsplanung.md`:
   - kognitiv aktivierender Einstieg (Problem / Vermutung / Widerspruch / Schätzen)
   - Stundenfrage für die Tafel
   - kooperative Methode passend zur Phase (Ich-Du-Wir), realistische Zeiten für 31 SuS
   - Differenzierung ★/★★/★★★, Tippkarten, Lösungen zur Selbstkontrolle
   - Sicherung mit Merkkasten + Exit-Ticket
   - antizipierte Fehlvorstellungen und Reaktion darauf
3. Erstelle **zwei** Word-Dateien in `reihen/<nr>-<thema>/`:
   - `<nn>-stunde-<kurztitel>.docx` – Entwurf (Kopf, Kompetenzen, Kommentar, Verlaufsplan,
     Tafelbild, erwartete Lösungen, Reserve, Hausaufgabe)
   - `<nn>-material-<kurztitel>.docx` – druckfertiges Schülermaterial (AB, Tippkarten,
     Exit-Ticket) und auf neuer Seite die Lösungen. Regeln wie in `/arbeitsblatt`.
   Erzeugungsskript daneben speichern (`erzeuge_<nn>.py`).
4. Alle Lösungen nachrechnen (Python). Vorschau rendern und prüfen (siehe `/reihe`).
5. Wenn sinnvoll: Beamer-Folie/Einstiegsimpuls als Text im Entwurf; GeoGebra-Auftrag
   konkret beschreiben (was einstellen, was beobachten).
6. Committen, pushen, beide Dateien per `SendUserFile` schicken. In 3–5 Zeilen
   zusammenfassen: Einstieg, Methode, Differenzierung, was sie vorbereiten muss (kopieren,
   ausschneiden, iPads).
