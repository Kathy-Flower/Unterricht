"""Stunde 12 (Do 08.10.2026, 90 min): DIN-A-Papier, Zahlbereiche, Kubikwurzel und n-te Wurzel."""
import sys; sys.path.insert(0, "werkzeuge")
from docx_bausteine import *
from docx_bausteine import _rahmen, _schattierung, _text

ORDNER = "reihen/01-wurzeln/"


def zahlbereiche_diagramm(d, beispiele=True):
    """Verschachtelte Kästen ℝ ⊃ ℚ ⊃ ℤ ⊃ ℕ (in Word bearbeitbar)."""
    ebenen = [
        ("ℝ  reelle Zahlen", "irrational: √2, π, √17, 1,0100100001…", "FFFFFF"),
        ("ℚ  rationale Zahlen", "3/4, −2,5, 0,3̅", "F2F2F2"),
        ("ℤ  ganze Zahlen", "−3, −√9", "E0E0E0"),
        ("ℕ  natürliche Zahlen", "1, 7, √16", "CFCFCF"),
    ]
    behaelter = d
    for i, (name, bsp, farbe) in enumerate(ebenen):
        t = behaelter.add_table(rows=1, cols=1)
        _rahmen(t, staerke=10)
        z = t.cell(0, 0); _schattierung(z, farbe)
        _text(z.paragraphs[0], f"**{name}**" + (f"   {bsp}" if beispiele else ""))
        behaelter = z
    d.add_paragraph()


# ============================================================ Entwurf
d = neues_dokument(schriftgroesse=11)
titel(d, "Stundenentwurf: Vom DIN-A4-Blatt zum Minecraft-Würfel – reelle Zahlen und n-te Wurzeln",
      "Reihe „Wurzeln“, Stunde 12 · Donnerstag, 08.10.2026 · 90 Minuten · Klasse 9 (31 SuS)")

ueberschrift(d, "Einordnung in die Reihe", 3)
absatz(d, "In Stunde 11 haben die SuS begründet, dass √2 kein Bruch ist, und den Begriff „irrationale Zahl“ "
          "kennengelernt. Diese Doppelstunde zeigt zuerst, dass √2 im Alltag wirklich vorkommt (DIN-A-Papier), "
          "und ordnet alle bekannten Zahlen in Zahlbereiche ein. Im zweiten Teil wird das Wurzelziehen auf "
          "dritte und höhere Potenzen erweitert. Am 14.10. folgt die Wiederholung „Terme“.")

ueberschrift(d, "Kompetenzen", 3)
absatz(d, "**Kernanliegen**: Die SuS ordnen Zahlen den Zahlbereichen ℕ, ℤ, ℚ und ℝ zu und wenden das Radizieren "
          "als Umkehrung des Potenzierens an, indem sie das Seitenverhältnis von DIN-A-Papier herleiten und "
          "Kantenlängen von Würfeln sowie Wachstumsfaktoren bestimmen.")
liste(d, [
    "**Inhaltsbezogen**: Arithmetik/Algebra (2) rationale und irrationale Zahlen unterscheiden, Beispiele angeben; "
    "(9) Radizieren als Umkehrung des Potenzierens anwenden.",
    "**Prozessbezogen**: Arg-4 (Relationen zwischen Fachbegriffen: Ober-/Unterbegriff bei Zahlbereichen), "
    "Ope-4 (Rechenoperationen auf Grundlage inhaltlichen Verständnisses), Mod-7 (Lösungen auf die Realität beziehen), "
    "Kom-3 (Begriffsinhalte an Anwendungssituationen erläutern).",
    "**Teilziele**: Die SuS … (1) erkennen √2 als Seitenverhältnis von DIN-A-Papier und begründen es (★★); "
    "(2) ordnen Zahlen dem kleinsten passenden Zahlbereich zu; (3) berechnen Kubikwurzeln und n-te Wurzeln im Kopf "
    "und mit dem TR; (4) nutzen n-te Wurzeln in Sachsituationen (Würfel, Wachstum).",
])

ueberschrift(d, "Problemorientierung und Lebensweltbezug", 3)
liste(d, [
    "**DIN-A4-Blatt**: Jede*r hat es in der Hand. Die Frage „Warum gerade 21,0 cm × 29,7 cm?“ ist echt und überraschend. "
    "Die Antwort (halbiertes Blatt hat dieselbe Form) führt direkt auf x² = 2.",
    "**Minecraft**: Die Spielwelt besteht aus Würfeln mit 1 m Kantenlänge – Würfelvolumen und Kantenlänge sind "
    "für viele SuS anschaulich und motivierend. Nicht-Spieler*innen verstehen den Kontext ohne Vorwissen.",
    "**Follower-Wachstum**: Social Media ist Alltag der SuS; die Aufgabe bezieht den Wachstumsfaktor auf eine "
    "Realitätsprüfung („Ist das realistisch?“, Mod-7). Die Zahlen sind ausdrücklich fiktiv.",
])

ueberschrift(d, "Didaktisch-methodischer Kommentar", 3)
liste(d, [
    "**Zwei Hälften mit eigener Problemfrage**: Nach ca. 45 min Sozialform- und Themenwechsel (Placemat → Lerntempoduett) "
    "hält die Konzentration in der Doppelstunde.",
    "**Messen vor Rechnen**: Die SuS messen A4, A5, A6 selbst (Falten) und entdecken den Quotienten ≈ 1,41 – erst dann "
    "wird hergeleitet (★★) bzw. reflektiert (★★★: „297/210 ist doch ein Bruch!“).",
    "**Placemat Zahlbereiche**: Jede*r sortiert zuerst allein die Zahlkarten, in der Gruppe wird ein Konsens gebildet. "
    "Diskussionsanlässe sind eingebaut: 22/7 vs. π, 1,4142 vs. √2, √16 und −√9 (sehen „irrational“ aus, sind es aber nicht).",
    "**Lerntempoduett**: Die Basisaufgaben (★) sichern den Mindeststandard ³√ im Kopf. Wer fertig ist, geht zur "
    "„Bushaltestelle“ und vergleicht mit dem/der nächsten Mitschüler*in, dann Weiterarbeit an ★★/★★★. Lösungen liegen am Pult.",
    "**Antizipierte Schwierigkeiten**: Verwechslung ³√8 mit 8 : 3 · 22/7 = π („steht so im Internet“) · 1,4142 wird für "
    "irrational gehalten · TR-Bedienung für ³√ und n-te Wurzel (vorab an der Tafel zeigen, ggf. Schnelle als Helfer) · "
    "³√(a + b) = ³√a + ³√b.",
    "**Hinweis**: n-te Wurzeln werden hier – wie üblich in Klasse 9 – nur für Radikanden a ≥ 0 betrachtet.",
])

ueberschrift(d, "Verlaufsplan", 3)
verlaufsplan(d, [
    ("Einstieg I", "0–8'",
     "L hält ein A4-Blatt hoch, faltet es einmal (A5) und noch einmal (A6): „Alle Blätter sehen gleich aus – nur kleiner. Zufall?“\n"
     "Rückgriff HA Stunde 11 („√2 im Alltag?“).\n"
     "Stundenfrage 1: **Warum hat ein DIN-A4-Blatt genau diese Maße?**",
     "Plenum", "A4-Blätter, Lineal"),
    ("Erarbeitung I", "8–25'",
     "AB 1: A1 ★ messen und Quotienten berechnen (EA, 5'), A2 ★★ Herleitung x² = 2 in PA, A3 ★★★ Stellungnahme. "
     "Tippkarten am Pult.\nKurze Besprechung im Plenum (1 Paar stellt A2 vor): Seitenverhältnis = √2 ≈ 1,414.",
     "Think-Pair-Share", "AB 1, Lineal, TR"),
    ("Erarbeitung II", "25–40'",
     "„Wir kennen jetzt Zahlen, die keine Brüche sind. Welche Zahlenarten gibt es eigentlich alle?“\n"
     "Placemat (4er): Jede*r sortiert die 16 Zahlkarten zuerst allein in seinem Feld (5'), dann Konsens in der Mitte "
     "(kleinster passender Zahlbereich).",
     "Placemat", "Zahlkarten, Placemat-Bogen A3"),
    ("Sicherung I", "40–48'",
     "Zwei Gruppen stellen strittige Karten vor (22/7, 1,4142, −√9). Tafelbild Zahlbereiche (verschachtelte Kästen), "
     "Merkkasten ins Heft.",
     "UG", "Tafel, Heft"),
    ("Einstieg II", "48–55'",
     "Beamer: Minecraft-Szene „Würfelförmiger Wasserspeicher aus 1000 Wasserblöcken – wie lang ist eine Kante?“ "
     "→ 10 (10³ = 1000). „Und bei 2000 Blöcken?“ → zwischen 12 und 13.\n"
     "Stundenfrage 2: **Wie kann man das Potenzieren rückgängig machen?** Begriff ³√, TR-Bedienung zeigen.",
     "UG", "Beamer, TR"),
    ("Erarbeitung III", "55–80'",
     "AB 2 im Lerntempoduett: A1–A2 ★ einzeln → Bushaltestelle, Partnervergleich → A3–A5 ★★, A6–A7 ★★★. "
     "Lösungen zur Selbstkontrolle am Pult.\nL unterstützt gezielt leistungsschwächere SuS bei A1/A2.",
     "Lerntempoduett", "AB 2, TR, Lösungen"),
    ("Sicherung II", "80–87'",
     "Merkkasten n-te Wurzel. Blitzlicht am Beamer: ³√27 = ? · ⁴√81 = ? · „Ist ³√10 rational?“ (Daumen hoch/runter).\n"
     "Rückbezug auf beide Stundenfragen.",
     "UG, Blitzlicht", "Beamer"),
    ("Abschluss", "87–90'",
     "Hausaufgabe: AB 2 bis einschließlich A5. Ausblick: Mittwoch Wiederholung Terme (für die Klassenarbeit).",
     "Plenum", ""),
])

ueberschrift(d, "Tafelbild / Merkkästen", 3)
absatz(d, "**Stundenfrage 1: Warum hat ein DIN-A4-Blatt genau diese Maße?**  → Halbiert man ein DIN-A-Blatt, hat die "
          "Hälfte dieselbe Form. Dafür muss gelten: lange Seite : kurze Seite = √2 ≈ 1,414. (Echte Blätter: auf mm gerundet.)")
zahlbereiche_diagramm(d)
merkkasten(d, "Zahlbereiche", [
    "ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ   (jeder Zahlbereich ist im nächsten enthalten)",
    "ℚ: alle Zahlen, die sich als Bruch schreiben lassen (abbrechende oder periodische Dezimalzahlen).",
    "ℝ: rationale **und** irrationale Zahlen. Jedem Punkt auf dem Zahlenstrahl entspricht genau eine reelle Zahl.",
])
merkkasten(d, "n-te Wurzel", [
    "Für a ≥ 0 ist ⁿ√a die nichtnegative Zahl, deren n-te Potenz a ergibt:   ⁿ√a = b  ⇔  bⁿ = a  (b ≥ 0)",
    "Beispiele: ³√8 = 2, weil 2³ = 8 · ⁴√81 = 3, weil 3⁴ = 81 · ³√0,001 = 0,1, weil 0,1³ = 0,001",
    "Das Wurzelziehen (**Radizieren**) macht das Potenzieren rückgängig.  ²√a schreibt man kurz √a.",
])

ueberschrift(d, "Erwartete Schülerlösungen (Auszug)", 3)
liste(d, [
    "AB 1, A1: A4 29,7 : 21,0 ≈ 1,414 · A5 21,0 : 14,8 ≈ 1,419 · A6 14,8 : 10,5 ≈ 1,410 – immer ungefähr 1,41.",
    "AB 1, A2: Kurze Seite 1, lange Seite x. Halbes Blatt: lange Seite 1, kurze Seite x/2. Gleiche Form: x : 1 = 1 : (x/2), "
    "also x = 2/x, also x² = 2, also x = √2.",
    "AB 1, A3: 297/210 ist nur der auf Millimeter gerundete Wert. Das ideale Verhältnis ist √2 und damit irrational; "
    "ein echtes Blatt kann nie exakt √2 haben.",
    "Placemat: ℕ: 7, √16 · ℤ: −3, −√9 · ℚ: 3/4, −2,5, 0,3̅, √(1/4), 22/7, 1,4142, 0,6̅ · irrational: π, √17, √2, √0,1, 1,0100100001…",
    "AB 2: siehe Lösungsblatt im Material.",
])

ueberschrift(d, "Didaktische Reserve und Hausaufgabe", 3)
liste(d, [
    "**Reserve**: „Ein Würfel-Lautsprecher soll das doppelte Volumen haben wie das alte Modell (Kante 8 cm). "
    "Wie lang muss die neue Kante sein?“ (8 · ³√2 ≈ 10,1 cm – nicht 16 cm!)",
    "**Hausaufgabe**: AB 2 bis einschließlich A5; Schnelle: A6.",
])

d.save(ORDNER + "12-stunde-reelle-zahlen-n-te-wurzel.docx")

# ============================================================ Material
m = neues_dokument()

# ---------- AB 1
titel(m, "Warum hat ein DIN-A4-Blatt genau diese Maße?")
absatz(m, "Wenn man ein DIN-A4-Blatt in der Mitte faltet, entsteht DIN A5. Faltet man noch einmal, entsteht DIN A6. "
          "Alle Blätter haben dieselbe Form – nur kleiner.")
aufgabe(m, 1, "**Miss** die Seiten (in cm, auf mm genau) und **berechne** jeweils lange Seite : kurze Seite "
              "(auf drei Nachkommastellen). Was fällt dir auf?", sterne=1)
tabelle(m, ["Format", "lange Seite", "kurze Seite", "lange Seite : kurze Seite"],
        [["DIN A4", "", "", ""], ["DIN A5", "", "", ""], ["DIN A6", "", "", ""]],
        breiten_cm=[3.4, 4.2, 4.2, 5.6])

aufgabe(m, 2, "Damit das halbierte Blatt dieselbe Form hat, muss das Seitenverhältnis gleich bleiben. "
              "Wir nehmen ein Blatt mit der kurzen Seite **1** und der langen Seite **x**.", sterne=2,
        teile=["**Gib** die lange und die kurze Seite des **halben** Blattes an. (Skizze!)",
               "Für gleiche Form gilt:  x : 1 = (lange Seite des halben Blattes) : (kurze Seite des halben Blattes). "
               "**Stelle** die Gleichung auf und **zeige**, dass x² = 2 gilt.",
               "**Gib** x an. Vergleiche mit deinem Messergebnis aus Aufgabe 1."],
        platz=6)

aufgabe(m, 3, "Jonas sagt: „Ein A4-Blatt ist 29,7 cm lang und 21 cm breit. 29,7 : 21 = 297/210 – das ist ein Bruch. "
              "Also ist das Seitenverhältnis rational und nicht √2.“  **Nimm Stellung.**", sterne=3, platz=4)

# ---------- Placemat
seitenumbruch(m)
titel(m, "Placemat: Welche Zahlen gibt es?")
absatz(m, "**Auftrag**: (1) Schneidet die Zahlkarten aus. (2) Jede*r ordnet in seinem Feld zuerst **allein** jede Zahl dem "
          "**kleinsten** passenden Zahlbereich zu (5 min). (3) Einigt euch dann in der Mitte auf eine gemeinsame Lösung "
          "und markiert Karten, bei denen ihr unsicher wart.")
karten = ["7", "−3", "3/4", "−2,5", "0,3̅", "√16", "√17", "π",
          "−√9", "√(1/4)", "22/7", "1,4142", "√2", "√0,1", "0,6̅", "1,0100100001…"]
t = m.add_table(rows=4, cols=4); _rahmen(t, art="dashed", staerke=6)
for k, z in enumerate(karten):
    c = t.cell(k // 4, k % 4)
    p = c.paragraphs[0]; p.alignment = 1
    r = p.add_run(z); r.font.size = Pt(20 if len(z) < 8 else 15)
    p.paragraph_format.space_before = Pt(10); p.paragraph_format.space_after = Pt(10)
m.add_paragraph()
absatz(m, "**Ergebnisfeld (Mitte des Placemats)** – kleinster passender Zahlbereich:", abstand_nach=4)
tabelle(m, ["ℕ (natürlich)", "ℤ (ganz, aber nicht natürlich)", "ℚ (rational, aber nicht ganz)", "irrational"],
        [["\n\n\n\n\n", "", "", ""]], breiten_cm=[4.3, 4.3, 4.3, 4.3])
absatz(m, "_Hinweis: 22/7 und 1,4142 genau anschauen!_", groesse=10)

# ---------- AB 2
seitenumbruch(m)
titel(m, "Wie macht man das Potenzieren rückgängig?")
merkkasten(m, "Erinnerung", [
    "√25 = 5, weil 5² = 25.   Genauso:  ³√8 = 2, weil 2³ = 8  (sprich: „dritte Wurzel aus 8“ oder „Kubikwurzel aus 8“).",
    "Allgemein: ⁿ√a = b, wenn bⁿ = a (für a ≥ 0, b ≥ 0).",
])
aufgabe(m, 1, "**Berechne** im Kopf.", sterne=1,
        teile=["³√8", "³√27", "³√125", "³√1000", "³√0,001", "⁴√16", "⁴√10 000", "⁵√32"], spalten=4, platz=1)
aufgabe(m, 2, "**Ergänze** wie im Beispiel.   Beispiel: 2⁵ = 32  ⇔  ⁵√32 = 2", sterne=1,
        teile=["3⁴ = 81  ⇔  ______", "10³ = 1000  ⇔  ______", "______  ⇔  ³√64 = 4", "______  ⇔  ⁶√1 = 1"],
        spalten=2)
aufgabe(m, 3, "**Minecraft**: Ein Würfel aus Blöcken soll komplett gefüllt sein (jeder Block ist 1 m × 1 m × 1 m).", sterne=2,
        teile=["Du hast 512 Blöcke. **Bestimme** die Kantenlänge des größten Würfels, den du genau damit bauen kannst.",
               "Ein riesiger Würfel besteht aus 3375 Blöcken. **Berechne** seine Kantenlänge.",
               "Du hast 5000 Blöcke. **Berechne** ³√5000 mit dem TR und **entscheide**: Wie lang ist die Kante des größten "
               "vollständigen Würfels? Wie viele Blöcke bleiben übrig?"], platz=4)
aufgabe(m, 4, "**Social Media** (fiktive Zahlen): Ein Kanal hatte 2000 Follower. Nach 3 Jahren sind es 54 000. "
              "Wir nehmen an, dass sich die Followerzahl jedes Jahr mit demselben Faktor q vervielfacht.", sterne=2,
        teile=["**Zeige**, dass gilt: q³ = 27. **Bestimme** q.",
               "Ein anderer Kanal verzehnfacht seine Followerzahl in 4 Jahren. **Berechne** den jährlichen Faktor q = ⁴√10 "
               "mit dem TR (zwei Nachkommastellen) und **gib** das Wachstum pro Jahr in Prozent an.",
               "**Beurteile**, ob ein solches Wachstum über viele Jahre realistisch ist."], platz=5)
aufgabe(m, 5, "**Gib** an, zwischen welchen aufeinanderfolgenden natürlichen Zahlen die Wurzel liegt, ohne TR. "
              "**Begründe** und **überprüfe** dann mit dem TR.", sterne=2,
        teile=["³√50", "³√200", "⁴√100"], spalten=3, platz=3)
aufgabe(m, 6, "**DIN A0** ist das Ausgangsformat: Es hat den Flächeninhalt **1 m²** und – wie alle DIN-A-Formate – "
              "das Seitenverhältnis lange : kurze Seite = √2.", sterne=3,
        teile=["Die kurze Seite sei b, die lange Seite √2 · b. **Zeige**, dass gilt: b² = 1/√2, und **berechne** b und "
               "die lange Seite in mm (Tipp: 1/√2 = ... und ⁴√2 mit dem TR).",
               "**Bestimme** daraus durch Halbieren die Maße von A1, A2, A3 und A4. Passt das zu deinem A4-Blatt?"], platz=6)
aufgabe(m, 7, "**Untersuche** an mindestens zwei Beispielen, ob die Wurzelgesetze auch für dritte Wurzeln gelten:", sterne=3,
        teile=["³√a · ³√b = ³√(a · b)", "³√a + ³√b = ³√(a + b)"], spalten=2, platz=4)

# ---------- Tippkarten
seitenumbruch(m)
tippkarten(m, [
    ("Tipp 1 zu AB 1, Aufgabe 2", "Halbiert wird immer die **lange** Seite x.\nDas halbe Blatt hat also die Seiten 1 und x/2.\nWelche davon ist jetzt die längere?"),
    ("Tipp 2 zu AB 1, Aufgabe 2", "x : 1 = 1 : (x/2)\nLinks steht x. Rechts: 1 : (x/2) = 2/x.\nAlso x = 2/x. Multipliziere mit x."),
    ("Tipp zu AB 1, Aufgabe 3", "Wie genau kann man mit dem Lineal messen?\nIst 1,4142857… dasselbe wie √2 = 1,4142135…?\nWas sagt die Rechnung aus Aufgabe 2 über das **ideale** Verhältnis?"),
    ("Tipp zu AB 2, Aufgabe 3c", "Probiere: 17³ = ?  und  18³ = ?\nWelcher Würfel passt mit 5000 Blöcken noch?"),
    ("Tipp zu AB 2, Aufgabe 4a", "Nach 1 Jahr: 2000 · q\nNach 2 Jahren: 2000 · q · q = 2000 · q²\nNach 3 Jahren: …  = 54 000. Teile durch 2000."),
    ("Tipp zu AB 2, Aufgabe 6", "b · √2 · b = 1, also √2 · b² = 1.\nb² = 1/√2, also b = √(1/√2) = 1/⁴√2.\nRechne mit dem TR in m und dann in mm."),
], titel_text="Tippkarten (ausschneiden, am Pult auslegen)")

# ---------- Lösungen
seitenumbruch(m)
titel(m, "Lösungen zur Selbstkontrolle")
absatz(m, "**AB 1, Aufgabe 1**: A4 29,7 : 21,0 ≈ 1,414 · A5 21,0 : 14,8 ≈ 1,419 · A6 14,8 : 10,5 ≈ 1,410 "
          "(kleine Abweichungen durch Messen sind normal). Das Verhältnis ist immer ungefähr 1,41.")
absatz(m, "**AB 1, Aufgabe 2**: a) halbes Blatt: lange Seite 1, kurze Seite x/2.  b) x : 1 = 1 : (x/2) ⇒ x = 2/x ⇒ x² = 2.  "
          "c) x = √2 ≈ 1,414 – passt zu den Messwerten.")
absatz(m, "**AB 1, Aufgabe 3**: Jonas hat nicht recht. 29,7 cm und 21 cm sind auf Millimeter **gerundete** Maße. "
          "Das ideale Verhältnis muss x² = 2 erfüllen, also x = √2 – und √2 ist irrational. 297/210 ≈ 1,41429 ist nur ein "
          "Näherungswert für √2 ≈ 1,41421.")
absatz(m, "**Placemat**: ℕ: 7, √16 = 4 · ℤ: −3, −√9 = −3 · ℚ: 3/4, −2,5, 0,3̅, √(1/4) = 1/2, 22/7, 1,4142, 0,6̅ · "
          "irrational: π, √17, √2, √0,1, 1,0100100001…  (22/7 ≈ 3,1429 und 1,4142 sind nur **Näherungswerte** für π und √2.)")
absatz(m, "**AB 2, Aufgabe 1**: a) 2  b) 3  c) 5  d) 10  e) 0,1  f) 2  g) 10  h) 2")
absatz(m, "**AB 2, Aufgabe 2**: a) ⁴√81 = 3  b) ³√1000 = 10  c) 4³ = 64  d) 1⁶ = 1")
absatz(m, "**AB 2, Aufgabe 3**: a) ³√512 = 8, also 8 Blöcke Kantenlänge (8 m).  b) ³√3375 = 15 → 15 m.  "
          "c) ³√5000 ≈ 17,1. 17³ = 4913 ≤ 5000 < 5832 = 18³. Größter Würfel: Kante 17 Blöcke, 5000 − 4913 = 87 Blöcke bleiben übrig.")
absatz(m, "**AB 2, Aufgabe 4**: a) 2000 · q³ = 54 000 ⇒ q³ = 27 ⇒ q = ³√27 = 3 (Verdreifachung pro Jahr).  "
          "b) q = ⁴√10 ≈ 1,78 ⇒ ca. +78 % pro Jahr.  c) Nicht dauerhaft realistisch: Bei q = 3 hätte der Kanal nach "
          "10 Jahren 2000 · 3¹⁰ ≈ 118 Millionen Follower; irgendwann gibt es nicht genug Nutzer*innen.")
absatz(m, "**AB 2, Aufgabe 5**: a) 3³ = 27 < 50 < 64 = 4³ ⇒ zwischen 3 und 4 (TR: 3,68)  "
          "b) 5³ = 125 < 200 < 216 = 6³ ⇒ zwischen 5 und 6 (TR: 5,85)  c) 3⁴ = 81 < 100 < 256 = 4⁴ ⇒ zwischen 3 und 4 (TR: 3,16)")
absatz(m, "**AB 2, Aufgabe 6**: a) b · √2 · b = 1 ⇒ b² = 1/√2 ⇒ b = 1/⁴√2 ≈ 0,8409 m = 841 mm; lange Seite √2 · b = ⁴√2 ≈ 1,1892 m "
          "= 1189 mm. A0: 841 mm × 1189 mm.  b) Halbieren der langen Seite: A1 594 × 841 · A2 420 × 594 · "
          "A3 297 × 420 · A4 210 × 297 (mm, gerundet) – passt genau zum A4-Blatt!")
absatz(m, "**AB 2, Aufgabe 7**: a) gilt, z. B. ³√8 · ³√27 = 2 · 3 = 6 = ³√216.  b) gilt **nicht**, z. B. ³√1 + ³√1 = 2, "
          "aber ³√2 ≈ 1,26; oder ³√8 + ³√27 = 5, aber ³√35 ≈ 3,27.")

m.save(ORDNER + "12-material-reelle-zahlen-n-te-wurzel.docx")
print("ok")
