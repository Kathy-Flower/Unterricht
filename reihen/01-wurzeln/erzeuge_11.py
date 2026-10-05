"""Stunde 11 (Mi 07.10.2026, 45 min): Irrationale Zahlen – Entwurf und Material."""
import sys; sys.path.insert(0, "werkzeuge")
from docx_bausteine import *

ORDNER = "reihen/01-wurzeln/"

# ============================================================ Entwurf
d = neues_dokument(schriftgroesse=11)
titel(d, "Stundenentwurf: Ist √2 ein Bruch? – Irrationale Zahlen",
      "Reihe „Wurzeln“, Stunde 11 · Mittwoch, 07.10.2026 · 45 Minuten · Klasse 9 (31 SuS)")

ueberschrift(d, "Einordnung in die Reihe", 3)
absatz(d, "Die SuS können Quadratwurzeln berechnen, sie mit Intervallschachtelung und Heron-Verfahren "
          "näherungsweise bestimmen und die Wurzelgesetze anwenden. Dabei sind sie immer wieder auf Wurzeln "
          "gestoßen, deren Dezimaldarstellung „nicht aufhört“. Diese Stunde klärt, warum das so ist, und "
          "führt den Begriff der irrationalen Zahl ein. In der Folgestunde (Do 08.10.) werden die "
          "Zahlbereiche zu ℝ erweitert und das Radizieren als Umkehrung des Potenzierens verallgemeinert.")

ueberschrift(d, "Kompetenzen", 3)
absatz(d, "**Kernanliegen**: Die SuS unterscheiden rationale und irrationale Zahlen und geben Beispiele "
          "für irrationale Zahlen an, indem sie an √2 begründen, dass sich diese Zahl nicht als Bruch "
          "schreiben lässt.")
liste(d, [
    "**Inhaltsbezogen**: Arithmetik/Algebra (2) – unterscheiden rationale und irrationale Zahlen und geben Beispiele an.",
    "**Prozessbezogen**: Arg-2 (Beispiele für vermutete Zusammenhänge benennen), Arg-7 (Argumentationsstrategie Widerspruch, ★★/★★★), Kom-3 (Begriffsinhalte erläutern).",
    "**Teilziele**: Die SuS … (1) prüfen durch Quadrieren, dass Näherungsbrüche nicht genau 2 ergeben; "
    "(2) vollziehen das Endziffern-Argument nach (★★) bzw. übertragen es auf √3 (★★★); "
    "(3) ordnen Zahlen begründet als rational oder irrational ein.",
])

ueberschrift(d, "Didaktisch-methodischer Kommentar", 3)
liste(d, [
    "**Einstieg mit kognitivem Konflikt**: Der Taschenrechner zeigt für √2 eine abbrechende Zahl, "
    "zwei Schüleraussagen behaupten einen exakten Wert. Das Nachprüfen durch Quadrieren widerlegt beide "
    "und erzeugt die Stundenfrage.",
    "**Endziffern-Argument statt klassischem Paritätsbeweis**: Es kommt ohne „gerade/ungerade“-Kette "
    "aus, ist mit einer Tabelle handlungsorientiert und für die Breite der Lerngruppe nachvollziehbar. "
    "Der klassische Beweis kann als Expertenaufgabe angeboten werden.",
    "**Think-Pair-Share**: Die Einzelphase sichert, dass alle SuS (auch leistungsschwache) die Tabelle "
    "selbst ausfüllen; im Pair wird das Argument versprachlicht (Wortspeicher), im Share von 1–2 Paaren "
    "vorgestellt.",
    "**Differenzierung**: A1 ★ (Brüche testen) ist Mindeststandard, A2 ★★ (Lückentext-Argument) mit "
    "Tippkarten, A3 ★★★ (√3 und √4 – warum klappt es bei √4 nicht?) für Schnelle.",
    "**Antizipierte Fehlvorstellungen**: „Der TR zeigt eine endliche Zahl, also ist √2 ein Bruch“ · "
    "„Irrational heißt: sehr viele Nachkommastellen“ · „Jede Wurzel ist irrational“ (√49, √0,09) · "
    "„Periodische Zahlen sind irrational“. → werden im Exit-Ticket gezielt geprüft.",
])

ueberschrift(d, "Verlaufsplan", 3)
verlaufsplan(d, [
    ("Einstieg", "0–7'",
     "Beamer: TR-Anzeige √2 = 1,414213562. Lea: „√2 ist genau 1,414213562.“ Tom: „√2 ist genau 99/70.“\n"
     "SuS prüfen kurz mit TR (Quadrieren) → beide falsch.\n"
     "Stundenfrage an die Tafel: **Kann man √2 exakt als Bruch schreiben?** Kurze Vermutungen sammeln (Daumenprobe).",
     "Plenum, Blitzlicht", "Beamer, TR"),
    ("Erarbeitung", "7–22'",
     "**Think** (5'): A1 ★ einzeln; Schnelle beginnen A2.\n"
     "**Pair** (8'): A2 ★★ gemeinsam (Tabelle, Lückentext), Wortspeicher nutzen; Tippkarten liegen am Pult. Schnelle Paare: A3 ★★★.\n"
     "L beobachtet, gibt gezielt Tipps, wählt 1–2 Paare für die Präsentation aus.",
     "Think-Pair-Share", "AB, TR, Tippkarten"),
    ("Sicherung", "22–33'",
     "**Share**: Ein Paar erklärt das Endziffern-Argument an der Dokumentenkamera / Tafel; Klasse ergänzt.\n"
     "Rückbezug Stundenfrage: Nein – √2 ist **kein** Bruch.\n"
     "Merkkasten gemeinsam ins Heft: Definition irrationale Zahl, rational ⇔ Dezimaldarstellung abbrechend oder periodisch; Beispiele.",
     "UG, Schülervortrag", "Tafel, Heft"),
    ("Übung / Diagnose", "33–41'",
     "**Exit-Ticket**: 6 Zahlen rational/irrational ankreuzen und eine Begründung formulieren. Einsammeln.",
     "EA", "Exit-Ticket"),
    ("Abschluss", "41–45'",
     "Kurzer Ausblick: „Welche Zahlen gibt es eigentlich alle?“ → Do: reelle Zahlen. Hausaufgabe.",
     "Plenum", ""),
])

ueberschrift(d, "Tafelbild / Merkkasten", 3)
merkkasten(d, "Irrationale Zahlen", [
    "Eine Zahl, die sich **nicht** als Bruch p/q (p, q ganze Zahlen, q ≠ 0) schreiben lässt, heißt **irrational**.",
    "Rationale Zahlen haben eine **abbrechende** (0,25) oder **periodische** (0,3̅) Dezimaldarstellung.",
    "Irrationale Zahlen haben eine **unendliche, nicht periodische** Dezimaldarstellung.",
    "Beispiele: √2, √3, √50, π, 0,1010010001…   Gegenbeispiele (rational): √49 = 7, √0,09 = 0,3, √(9/25) = 3/5",
    "Der Taschenrechner zeigt immer nur einen **gerundeten** Wert: √2 ≈ 1,414213562.",
])

ueberschrift(d, "Erwartete Schülerlösungen", 3)
liste(d, [
    "A1: (7/5)² = 49/25 = 1,96 · (17/12)² = 289/144 ≈ 2,0069 · (41/29)² = 1681/841 ≈ 1,9988 · (99/70)² = 9801/4900 ≈ 2,0002 – nah an 2, aber nie genau 2.",
    "A2: Endziffern von q² sind 0, 1, 4, 5, 6, 9; Endziffern von 2q² nur 0, 2, 8. Gemeinsam ist nur die 0. "
    "Also endet p² auf 0 → p endet auf 0. 2q² endet auf 0 → q² endet auf 0 oder 5 → q endet auf 0 oder 5. "
    "Dann sind p und q durch 5 teilbar – Widerspruch zu „vollständig gekürzt“.",
    "A3 a): 3q² hat die Endziffern 0, 2, 3, 5, 7, 8; gemeinsam mit p²: 0 und 5. In beiden Fällen enden p und q auf dieselbe Ziffer (0 oder 5) → beide durch 5 teilbar → Widerspruch.",
    "A3 b): 4q² hat die Endziffern 0, 4, 6 – alle kommen auch bei p² vor. Es entsteht kein Widerspruch; tatsächlich ist √4 = 2 = 2/1 rational.",
])

ueberschrift(d, "Didaktische Reserve und Hausaufgabe", 3)
liste(d, [
    "**Reserve**: „Finde eine irrationale Zahl zwischen 3 und 4 – und eine, die keine Wurzel ist.“ (z. B. √10, π, 3,1011011101111…)",
    "**Hausaufgabe**: AB Aufgabe 4 (Zahlen einordnen) und LS 9, Kap. 3: S. __ Nr. __ (bitte eintragen).",
])

d.save(ORDNER + "11-stunde-irrationale-zahlen.docx")

# ============================================================ Material
m = neues_dokument()
titel(m, "Ist √2 ein Bruch?")

absatz(m, "Lea behauptet: „√2 ist **genau** 1,414213562 – das zeigt der Taschenrechner.“   "
          "Tom meint: „√2 ist **genau** 99/70.“")

aufgabe(m, 1, "**Überprüfe** die Aussagen von Lea und Tom, indem du quadrierst. **Berechne** dann die "
              "Quadrate der folgenden Brüche. Was fällt dir auf?", sterne=1,
        teile=["1,414213562²", "(99/70)²", "(7/5)²", "(17/12)²", "(41/29)²"], spalten=2, platz=3)

aufgabe(m, 2, "Wir nehmen an, √2 ließe sich doch als **vollständig gekürzter** Bruch p/q schreiben. "
              "Dann gilt 2 = p²/q², also **p² = 2 · q²**. Die Zahlen p² und 2 · q² müssen also auch "
              "auf dieselbe Ziffer enden.", sterne=2)
absatz(m, "a) **Vervollständige** die Tabelle. (Es kommt nur auf die letzte Ziffer an.)")
tabelle(m, ["Endziffer von q", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], [
    ["Endziffer von q²", "0", "1", "4", "", "", "", "", "", "", ""],
    ["Endziffer von 2 · q²", "0", "2", "8", "", "", "", "", "", "", ""],
], breiten_cm=[4.1] + [1.3] * 10)
absatz(m, "b) **Ergänze** den Lückentext.")
for z in [
    "Eine Quadratzahl p² kann nur auf die Ziffern ______________________ enden.",
    "Die Zahl 2 · q² kann nur auf die Ziffern ______________________ enden.",
    "Wegen p² = 2 · q² müssen beide auf die Ziffer ______ enden.",
    "Wenn p² auf 0 endet, dann endet p auf ______ .",
    "Wenn 2 · q² auf 0 endet, dann endet q² auf ______ oder ______ , also endet q auf ______ oder ______ .",
    "Dann sind p und q beide durch ______ teilbar. Das ist ein __________________ , "
    "denn der Bruch p/q war vollständig gekürzt.",
    "Also: √2 lässt sich ______________ als Bruch schreiben.",
]:
    absatz(m, z, abstand_nach=8)
merkkasten(m, "Wortspeicher", ["Annahme · vollständig gekürzt · Endziffer · teilbar · Widerspruch · folglich · "
                               "Es kann nicht sein, dass … · Daraus folgt, dass …"])

aufgabe(m, 3, "Für Expertinnen und Experten:", sterne=3,
        teile=["**Zeige** mit derselben Idee, dass √3 kein Bruch ist.  (Ansatz: p² = 3 · q²)",
               "**Erkläre**, warum das Argument bei √4 nicht funktioniert. Ist das ein Problem?"],
        platz=5)

aufgabe(m, 4, "**Ordne** die Zahlen in die Tabelle ein (Hausaufgabe):  √36 · √37 · 0,7̅ · −√81 · π · "
              "√(4/9) · √0,4 · √0,04 · 5,121121112…", sterne=1)
tabelle(m, ["rational", "irrational"], [["\n\n\n", "\n\n\n"]], breiten_cm=[8.6, 8.6])

seitenumbruch(m)
tippkarten(m, [
    ("Tipp 1 zu Aufgabe 2a", "Rechne nur mit der letzten Ziffer.\nBeispiel q = …3:  3 · 3 = 9, also endet q² auf 9.\nDann 2 · 9 = 18, also endet 2 · q² auf 8."),
    ("Tipp 2 zu Aufgabe 2a", "Die Zeile „Endziffer von q²“ lautet vollständig:\n0, 1, 4, 9, 6, 5, 6, 9, 4, 1"),
    ("Tipp 1 zu Aufgabe 2b", "Schau dir die beiden unteren Zeilen der Tabelle an.\nWelche Ziffern stehen in Zeile 2 und welche in Zeile 3?\nWelche Ziffer kommt in **beiden** Zeilen vor?"),
    ("Tipp 2 zu Aufgabe 2b", "Nur die 0 kommt in beiden Zeilen vor.\nIn welchen Spalten steht in Zeile 3 eine 0? (bei q = 0 und q = 5)\nWelche Zahl teilt dann sowohl p als auch q?"),
    ("Tipp zu Aufgabe 3a", "Mache eine neue Tabelle mit der Zeile „Endziffer von 3 · q²“.\nWelche Ziffern kommen bei p² **und** 3 · q² vor? Es sind zwei. Untersuche beide Fälle."),
    ("Tipp zu Aufgabe 3b", "Mache die Tabelle für 4 · q².\nGibt es diesmal einen Widerspruch? Was ist √4?"),
], titel_text="Tippkarten (ausschneiden, am Pult auslegen)")

seitenumbruch(m)
for kopie in range(2):  # zwei Exit-Tickets pro Seite
    if kopie:
        absatz(m, "✂ " + "- " * 60, groesse=8, abstand_nach=14)
    absatz(m, "**Exit-Ticket: rational oder irrational?**", groesse=14)
    tabelle(m, ["Zahl", "rational", "irrational"], [
        ["√49", "☐", "☐"], ["√50", "☐", "☐"], ["0,4̅ = 0,444…", "☐", "☐"],
        ["√0,09", "☐", "☐"], ["√0,9", "☐", "☐"], ["2,1010010001… (immer eine 0 mehr)", "☐", "☐"],
    ], breiten_cm=[9, 4, 4])
    absatz(m, "**Begründe** bei einer Zahl deiner Wahl deine Entscheidung:")
    schreibplatz(m, 3)
    absatz(m, "")

seitenumbruch(m)
titel(m, "Lösungen zur Selbstkontrolle")
absatz(m, "**Aufgabe 1**: 1,414213562² ≈ 1,999999999 (nicht 2) · (99/70)² = 9801/4900 ≈ 2,0002 · "
          "(7/5)² = 49/25 = 1,96 · (17/12)² = 289/144 ≈ 2,0069 · (41/29)² = 1681/841 ≈ 1,9988. "
          "Die Quadrate liegen nah an 2, sind aber nie genau 2. Lea und Tom haben beide nicht recht.")
absatz(m, "**Aufgabe 2a**")
tabelle(m, ["Endziffer von q", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], [
    ["Endziffer von q²", "0", "1", "4", "9", "6", "5", "6", "9", "4", "1"],
    ["Endziffer von 2 · q²", "0", "2", "8", "8", "2", "0", "2", "8", "8", "2"],
], breiten_cm=[4.1] + [1.3] * 10)
absatz(m, "**Aufgabe 2b**: p² endet auf 0, 1, 4, 5, 6 oder 9. 2 · q² endet auf 0, 2 oder 8. Beide müssen auf **0** "
          "enden. Wenn p² auf 0 endet, endet p auf **0**. Wenn 2 · q² auf 0 endet, endet q² auf **0 oder 5**, "
          "also endet q auf **0 oder 5**. Dann sind p und q durch **5** teilbar. Das ist ein **Widerspruch**, "
          "denn p/q war vollständig gekürzt. Also lässt sich √2 **nicht** als Bruch schreiben.")
absatz(m, "**Aufgabe 3a**: 3 · q² endet auf 0, 3, 2, 7, 8, 5, 8, 7, 2, 3 (für q = 0 … 9). Gemeinsam mit p² "
          "sind nur 0 und 5. Fall 0: p und q enden beide auf 0. Fall 5: p und q enden beide auf 5. In beiden "
          "Fällen sind p und q durch 5 teilbar → Widerspruch → √3 ist irrational.")
absatz(m, "**Aufgabe 3b**: 4 · q² endet auf 0, 4 oder 6 – diese Ziffern kommen auch bei Quadratzahlen vor. "
          "Es entsteht kein Widerspruch. Das ist kein Problem, denn √4 = 2 = 2/1 ist tatsächlich rational.")
absatz(m, "**Aufgabe 4**: rational: √36 = 6, 0,7̅ = 7/9, −√81 = −9, √(4/9) = 2/3, √0,04 = 0,2 · "
          "irrational: √37, π, √0,4, 5,121121112…")
absatz(m, "**Exit-Ticket**: rational: √49 = 7, 0,4̅ = 4/9, √0,09 = 0,3 · irrational: √50, √0,9, 2,1010010001…")

m.save(ORDNER + "11-material-irrationale-zahlen.docx")
print("ok")
