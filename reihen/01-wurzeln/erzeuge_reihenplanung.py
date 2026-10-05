import sys; sys.path.insert(0, "werkzeuge")
from docx_bausteine import *

d = neues_dokument(quer=True, rand_cm=1.5, schriftgroesse=11)
titel(d, "Reihenplanung: Wurzeln (Klasse 9)",
      "Unterrichtsvorhaben 1 · Beginn 02.09.2026 · Mi 45 min / Do 90 min")

absatz(d, "**Kompetenzerwartungen (Curriculum)**: (2) rationale und irrationale Zahlen unterscheiden · "
          "(6) Quadratwurzeln näherungsweise bestimmen (Algorithmus nutzen und beschreiben) · "
          "(7) Quadratwurzeln mit Wurzelgesetzen auch ohne digitale Werkzeuge berechnen · "
          "(9) Radizieren als Umkehrung des Potenzierens. Zusätzlich: **Wiederholung Terme** (10 % der Klassenarbeit).")
absatz(d, "**Status**: ✔ = bereits unterrichtet (nachträglich strukturiert, bitte mit deinen Notizen abgleichen) · "
          "▶ = als Nächstes · ○ = geplant")

KOPF = ["", "Datum", "min", "Thema / Kernanliegen", "Methode", "Kompetenzen", "Material · Hausaufgabe"]
B = [0.8, 1.9, 1.2, 8.8, 4.0, 3.0, 6.8]

ueberschrift(d, "Teil 1: bereits behandelt (02.09. – 01.10.)", 3)
tabelle(d, KOPF, [
    ["✔", "Mi 02.09.", "45", "**Einstieg & Vorwissen**: Quadratzahlen bis 25², Quadrieren, Flächeninhalt von Quadraten. Kurze Diagnose.",
     "Kugellager (Kopfrechnen), Ich-Du-Wir", "Ope-1", "Diagnosetest Wurzeln (wurzeln.html)"],
    ["✔", "Do 03.09.", "90", "**Quadratwurzeln**: Aus dem Flächeninhalt die Seitenlänge bestimmen. Definition √a (a ≥ 0) als nichtnegative Zahl, deren Quadrat a ist; Radizieren als Umkehrung des Quadrierens.",
     "Think-Pair-Share, Merkkasten", "(9), Ope-4, Kom-3", "Merkkasten"],
    ["✔", "Mi 09.09.", "45", "**Übung Quadratwurzeln**: Wurzeln aus Dezimalzahlen und Brüchen (√0,04; √(9/16)), Gleichungen x² = a.",
     "Lerntempoduett", "(7), Ope-1", "–"],
    ["✔", "Do 10.09.", "90", "**Wurzeln näherungsweise bestimmen I**: Intervallschachtelung für √2 – „Zwischen welchen Zahlen liegt √2?“",
     "Partnerarbeit, Tabelle", "(6), Ope-8, Pro-5", "–"],
    ["✔", "Mi 16.09.", "45", "**Wurzeln näherungsweise bestimmen II**: Heron-Verfahren, Algorithmus mit eigenen Worten beschreiben; ggf. Tabellenkalkulation auf dem iPad.",
     "Think-Pair-Share", "(6), Kom-4", "iPads"],
    ["✔", "Do 17.09.", "90", "**Übung Näherungsverfahren** und Taschenrechner; Vergleich der Verfahren (Schnelligkeit, Genauigkeit).",
     "Stationen / Lerntempoduett", "(6), Pro-5, Kom-4", "–"],
    ["✔", "Mi 23.09.", "45", "**Wurzelgesetze entdecken**: √a · √b = √(a·b) und √a : √b = √(a:b) an Beispielen; Gegenbeispiel √(a+b) ≠ √a + √b.",
     "Think-Pair-Share", "(7), Ope-5, Arg-2", "–"],
    ["✔", "Do 24.09.", "90", "**Geschickt mit Wurzeln rechnen**: teilweises Wurzelziehen (√50 = 5√2), gleichartige Wurzeln zusammenfassen.",
     "Lerntempoduett", "(7), Ope-1, Ope-5", "–"],
    ["✔", "Mi 30.09.", "45", "**Übung Wurzelgesetze**", "Partnerkontrolle", "(7)", "–"],
    ["✔", "Do 01.10.", "90", "**Vertiefung Wurzelterme**: Terme mit Wurzeln vereinfachen, Fehler finden.",
     "Fehlerdetektiv", "(7), Ope-5", "–"],
], breiten_cm=B, schrift=9)

ueberschrift(d, "Teil 2: bis zu den Herbstferien (07.10. – 15.10.)", 3)
tabelle(d, KOPF, [
    ["▶", "Mi 07.10.", "45", "**Irrationale Zahlen**: Stundenfrage „Kann man √2 exakt als Bruch schreiben?“ – Brüche testen, Endziffern-Argument, Begriff irrationale Zahl, rational ⇔ abbrechend oder periodisch.",
     "Think-Pair-Share, Exit-Ticket", "(2), Arg-2, Arg-7, Kom-3", "Entwurf + Material Stunde 11 (liegt bei)"],
    ["○", "Do 08.10.", "90", "**Warum hat ein DIN-A4-Blatt genau diese Maße? / Wie lang ist die Kante meines Minecraft-Würfels?** "
     "Teil 1: √2 als Seitenverhältnis von DIN-A-Papier, Zahlbereiche ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ. "
     "Teil 2: Kubikwurzel und n-te Wurzel als Umkehrung des Potenzierens (Minecraft, Follower-Wachstum, DIN A0).",
     "Think-Pair-Share, Placemat, Lerntempoduett", "(2), (9), Arg-4, Ope-4, Mod-7", "Entwurf + Material Stunde 12 (liegt bei)"],
    ["○", "Mi 14.10.", "45", "**Wiederholung Terme** (für die KA): zusammenfassen, ausmultiplizieren, ausklammern, **binomische Formeln**; Brücke zu Wurzeltermen: (2 + √3)², (√5 − 1)(√5 + 1).",
     "Fehlerdetektiv, Partnerkontrolle", "Ope-5", "AB Terme (★/★★/★★★)"],
    ["○", "Do 15.10.", "90", "**Vertiefung & Diagnose**: Lerntheke mit Pflicht- und Wahlstationen (Wurzeln, Näherung, irrationale Zahlen, Terme); „Ich kann …“-Checkliste zur Selbsteinschätzung.",
     "Lerntheke / Stationen", "alle", "Stationen, Checkliste · **Übungswebsite** für die Ferien"],
], breiten_cm=B, schrift=9)

absatz(d, "**Herbstferien 17.10. – 31.10.2026** – freiwillig: Übungswebsite (Selbstkontrolle mit Note).", abstand_nach=8)

ueberschrift(d, "Teil 3: nach den Ferien (Vorschlag)", 3)
tabelle(d, KOPF, [
    ["○", "Mi 04.11.", "45", "**Fragestunde / Wiederholung**: Fragen klären, hilfsmittelfreie Aufgaben trainieren (Kopfrechnen Wurzeln, Wurzelgesetze, Terme).",
     "Kugellager, Ich-Du-Wir", "Ope-1, Ope-5", "Probeaufgaben"],
    ["○", "Do 05.11.", "90", "**Klassenarbeit 1** (60 min): Teil A hilfsmittelfrei (20 min), Teil B mit Taschenrechner (40 min); ca. 10 % Terme. Restzeit: Start „Quadratische Funktionen“ (Wiederholung lineare Funktionen).",
     "–", "(2), (6), (7), (9), Ope-5", "Klassenarbeit A/B + Erwartungshorizont"],
], breiten_cm=B, schrift=9)

ueberschrift(d, "Planungshinweise", 3)
liste(d, [
    "**Differenzierung** durchgehend: ★ Mindeststandard (Quadratwurzeln im Kopf, einfache Wurzelgesetze), ★★ Standard, ★★★ Begründen/Beweisen (z. B. √3 ist irrational).",
    "**Typische Fehlvorstellungen**: √(a + b) = √a + √b · „Der Taschenrechner zeigt eine endliche Zahl, also ist √2 rational“ · „Jede Wurzel ist irrational“ (√49) · √(−4) = −2.",
    "**Klassenarbeit**: Termin 05.11. ist ein Vorschlag. Alternativ vor den Ferien am 15.10.; dann entfällt die Lerntheke als eigene Stunde.",
    "**Terme**: Wiederholung inkl. binomischer Formeln (aus Klasse 8 bekannt), verknüpft mit Wurzeltermen.",
    "**Lebensweltbezug** in jeder Stunde (DIN-A-Papier, Minecraft, Social Media …); das Lehrbuch wird nur ergänzend genutzt.",
])

d.save("reihen/01-wurzeln/00-reihenplanung.docx")
print("ok")
